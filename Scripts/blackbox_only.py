#!/usr/bin/env python3

import os
import subprocess 
import time
import sys
from collections import defaultdict
import argparse
from pycparser import c_parser, c_ast
import itertools


def find_declared_variables(node):
    declared_vars = set()


    if isinstance(node, c_ast.Decl):
        declared_vars.add(node.name)


    for _, child in node.children():
        declared_vars.update(find_declared_variables(child))

    return declared_vars


def find_constants(node):
    constants = set()

    
    if isinstance(node, c_ast.Constant):
        constants.add(node.value)

    
    for _, child in node.children():
        constants.update(find_constants(child))

    return constants


def find_main_function(ast):
 
    for _, node in ast.children():
        if isinstance(node, c_ast.FuncDef) and node.decl.name == "main":
            return node
    return None


def find_defined_variables_at_while_entry(ast):
    while_defined_vars = {}
    current_scope = set()  
    scope_stack = []  
    all_constants = set()  

   
    main_func = find_main_function(ast)
    if not main_func:
        print("No main function found in the program.")
        return {}

   
    def traverse_node(node):
        nonlocal while_defined_vars, current_scope, scope_stack, all_constants

        current_scope.update(find_declared_variables(node))
        
        
        if isinstance(node, c_ast.Compound):
            
            scope_stack.append(current_scope.copy())
            for _, child in node.children():
                traverse_node(child)
            
            current_scope = scope_stack.pop()

        
        elif isinstance(node, c_ast.While):

            
            while_defined_vars[node] = {
                "line": node.coord.line,  
                "vars": current_scope.copy() 
            }

            for _, child in node.children():
                traverse_node(child)

        
        elif isinstance(node, c_ast.If):
            scope_stack.append(current_scope.copy())
            for _, child in node.children():
                traverse_node(child)
           
            current_scope = scope_stack.pop()

        
        else:
            for _, child in node.children():
                traverse_node(child)

        
        all_constants.update(find_constants(node))

    
    traverse_node(main_func.body)

    return while_defined_vars, all_constants


def generate_boolean_expressions(vars_list, constants):

    operators = ['==', '!=', '<', '<=', '>', '>=']


    boolean_expressions = []
    

    for var in vars_list:
        for constant in constants:
            for op in operators:
                expr = f"{var} {op} {constant}"
                boolean_expressions.append(expr)


    for var1, var2 in itertools.combinations(vars_list, 2):
        for op in operators:
            expr = f"{var1} {op} {var2}"
            boolean_expressions.append(expr)

    return boolean_expressions

def parse_c_program(c_code):

    parser = c_parser.CParser()


    try:
        ast = parser.parse(c_code)
    except Exception as e:
        print(f"Error parsing the C code: {e}")
        return None

    return ast

def main():

    c_benchmarks = './ibmc_code2inv_parsable_benchmarks/'

    c_benchmark_time_limit = 2000 

    c_benchmarks_successful = []

    c_benchmarks_unsuccessful = []

    total_duration_spent_on_benchmarks = 0

    total_duration_spent_on_each_benchmark = 0

    for name_of_the_c_benchmark_file in os.listdir(c_benchmarks):
        if name_of_the_c_benchmark_file.endswith('.c'):

            while True:
                

                try:
                    with open(os.path.join(c_benchmarks, name_of_the_c_benchmark_file), 'r') as benchmark_read:
                        c_code = benchmark_read.read()
                except FileNotFoundError:
                    print(f"File '{name_of_the_c_benchmark_file}' not found.")
                    return
                except Exception as e:
                    print(f"Error reading file: {e}")
                    return


                ast = parse_c_program(c_code)
                if not ast:
                    return

                while_defined_vars, constants = find_defined_variables_at_while_entry(ast)

                print(f"Defined constants:")
                print(f"Constants: {', '.join(constants)}")

                if not while_defined_vars:
                    print("No while loops found in the main function.")
                else:
                    for while_node, data in while_defined_vars.items():
                        line_number = data["line"]
                        defined_vars = data["vars"]
                        print(f"Benchmark Filename {name_of_the_c_benchmark_file}:")
                        print(f"Defined variables at the entry to the while loop at line {line_number}:")
                        print(f"Variables: {', '.join(defined_vars)}")
                        
                        if defined_vars:
                            boolean_expressions = generate_boolean_expressions(list(defined_vars), constants)
                            print("Generated boolean expressions:")
                            for expr in boolean_expressions:
                                print("__invariant(" + expr + ");")
                        else:
                            print("No defined variables at the entry to this while loop.")

                new_code = c_code.split('\n')
                for insertion_index, line in enumerate(new_code):
                    if 'while' in line:
                        new_code.insert(insertion_index, '\n'.join(f'__invariant({expr});' for expr in boolean_expressions))
                        break

                new_modified_code  = '\n'.join(new_code)

                print(new_modified_code)

                with open("new_modified_code.c", "w") as file:
                    file.write(new_modified_code)

                start_time = time.time()

                esbmc_executable_path = sys.argv[1]

                esbmc_command = [esbmc_executable_path, "new_modified_code.c"]

                run_str = "--vampire-for-loops --ir --output testVampEsbmc --vampire-path " + sys.argv[2] + " --no-bounds-check"
                
                vampire_executable_path_addition = run_str.split(" ")

                vampire_executable_command = [*esbmc_command, *vampire_executable_path_addition]

                run_esbmc_with_script = subprocess.run(vampire_executable_command, capture_output=True, text=True)

                end_time = time.time()

                total_time_per_benchmark = end_time - start_time

                os.remove('new_modified_code.c')

                print("C Benchmark Name: " + name_of_the_c_benchmark_file + "\n" + "Total Time Spent in Seconds: " + str(end_time - start_time))

                if run_esbmc_with_script.returncode !=0: 
                    print("ESMBC + Vampire execution has encountered an error")
                    print(run_esbmc_with_script.stderr)
                    print("Invariant Generation is occurring again")
                    print('\n'*5)
                    total_duration_spent_on_benchmarks+=total_time_per_benchmark
                    total_duration_spent_on_each_benchmark += total_time_per_benchmark
                    print('----------------------------------------------------------')
                    print('END OF BENCHMARK ATTEMPT ON: ', name_of_the_c_benchmark_file)
                    print('----------------------------------------------------------')
                    print('\n'*2)
                    c_benchmarks_unsuccessful.append((name_of_the_c_benchmark_file, str(total_duration_spent_on_benchmarks), str(total_duration_spent_on_each_benchmark)))
                    total_duration_spent_on_each_benchmark = 0
                    break
                else: 
                    total_duration_spent_on_benchmarks+=total_time_per_benchmark
                    total_duration_spent_on_each_benchmark+= total_time_per_benchmark
                    print("ESBMC + Vampire ran SUCCESSFULLY")
                    print("Generated Successful Invariant.")
                    print(run_esbmc_with_script.stdout)
                    print('----------------------------------------------------------')
                    print('END OF BENCHMARK ATTEMPT ON: ', name_of_the_c_benchmark_file)
                    print('----------------------------------------------------------')
                    print('\n'*2)
                    c_benchmarks_successful.append((name_of_the_c_benchmark_file, str(total_time_per_benchmark), str(total_duration_spent_on_benchmarks), str(total_duration_spent_on_each_benchmark)))
                    total_duration_spent_on_each_benchmark = 0
                    break              

    print("Number of the Code2Inv Benchmarks Solved: " + str(len(c_benchmarks_successful)))
    print("The names of the Benchmark Files that were Solved: ")
    print('\n'.join(map(str, c_benchmarks_successful)))
    print("Number of the Code2Inv Benchmarks that were not Solved: " + str(len(c_benchmarks_unsuccessful)))
    print("The names of the Benchmark Files that were not Solved: ")
    print('\n'.join(map(str, c_benchmarks_unsuccessful)))
    print("Total Time for all Benchmarks in Seconds: " + str(total_duration_spent_on_benchmarks) + " s")
    
if __name__ == "__main__":
    main()

