import openai
import os
import subprocess 
import time
import re
import Prompt_Examples
import sys
from collections import defaultdict

openai.api_key = os.getenv("key_for_the_API")

c_benchmarks = '../Benchmarks/Multiple_Loops/'

c_benchmark_time_limit = 600 

c_benchmarks_successful = []

c_benchmarks_unsuccessful = []

total_duration_spent_on_benchmarks = 0

total_duration_spent_on_each_benchmark = 0  

total_iterations_for_benchmarks = 0

index = 0

for name_of_the_c_benchmark_file in os.listdir(c_benchmarks):
    if name_of_the_c_benchmark_file.endswith('.c'):

        invariant_generation_iteration = 0

        parse_error_iterations = 0 

        invariant_generated_correct_format = False

        c_benchmark_start_time = time.time()
        
        loop_counter = 0

        index = 0

        while True:

            if time.time() - c_benchmark_start_time >= c_benchmark_time_limit:
                print("Max Duration Limit Reached for the Benchmark.") 
                print("Time to move on to the next Benchmark")
                break

            with open(os.path.join(c_benchmarks, name_of_the_c_benchmark_file), 'r') as benchmark_read:
                c_benchmark = benchmark_read.read()

            line_numbered_code = c_benchmark.split('\n') 

            line_array = ["A", "B", "C", "D", "E"]

            loop_label_counter_index = 0

            label_for_the_loops = []

            for line in line_numbered_code:
                if line.strip().startswith(('while', 'for')):
                    loop_label = f'// Line {line_array[loop_label_counter_index]}'
                    label_for_the_loops.append(loop_label)
                    loop_label_counter_index=loop_label_counter_index+1
                label_for_the_loops.append(line)


            unmodified_code = '\n'.join(label_for_the_loops)
            print('----------------------------------------------------------')
            print('STARTING VERIFICATION ATTEMPT ON: ', name_of_the_c_benchmark_file)
            print('----------------------------------------------------------')
            print (unmodified_code)

            if invariant_generation_iteration <6:

                code_modifying_prompt = """
                
                "
                \n"""+Prompt_Examples.code_example_4+"""\n

                "

                Based on these examples provided above can you generate an C invariant for the following code,
                “
                \n"""+c_benchmark+"""\n

                "
                Print two sets of single valid C invariants for each loop in the C program.
                They should help prove the assertions. You can utilise '&&' or '||' if required. 
                No explanation. Your answer should be in the form i.e. for the first loop '__invariant(…); // Line A'. 
                Do this for every loop appropriately in the program i.e for the second loop '__invariant(…); // Line B'. 
                The end comment of all generated invariant(s) for every loop shall be labelled '// Line A' or '// Line B' or '// Line C' and so on depending on the number of loops in the program.
                No explanation.
                """
            elif invariant_generation_iteration == 6 and invariant_generation_iteration<11: 

                code_modifying_prompt = """

                "
                \n"""+Prompt_Examples.code_example_4+"""\n

                "
                Based on these examples provided above can you generate an C invariant for the following code,
                “
                \n"""+c_benchmark+"""\n

                "

                Print two sets of double valid invariants for each loop in the C program. 
                They should help prove the assertions. You can utilise '&&' or '||' if required. 
                No explanation. Your answer should be in the form i.e. for the first loop '__invariant(…); // Line A'. 
                Do this for every loop appropriately in the program i.e for the second loop '__invariant(…); // Line B'. 
                The end comment of all generated invariant(s) for every loop shall be labelled '// Line A' or '// Line B' or '// Line C' and so on depending on the number of loops in the program.
                No explanation.
                """

            elif invariant_generation_iteration == 11 and invariant_generation_iteration<16:

                code_modifying_prompt = """

                "
                \n"""+Prompt_Examples.code_example_4+"""\n

                "
                Based on these examples provided above can you generate an C invariant for the following code,
                “
                \n"""+c_benchmark+"""\n

                "

                Print two sets of triple valid invariants for each loop in the C program.
                They should help prove the assertions. You can utilise '&&' or '||' if required. 
                No explanation. Your answer should be in the form i.e. for the first loop '__invariant(…); // Line A'. 
                Do this for every loop appropriately in the program i.e for the second loop '__invariant(…); // Line B'. 
                The end comment of all generated invariant(s) for every loop shall be labelled '// Line A' or '// Line B' or '// Line C' and so on depending on the number of loops in the program.
                No explanation.
                """
            elif invariant_generation_iteration ==16 and invariant_generation_iteration<21:

                code_modifying_prompt = """

                "
                \n"""+Prompt_Examples.code_example_4+"""\n

                "
                Based on these examples provided above can you generate an C invariant for the following code,
                “
                \n"""+c_benchmark+"""\n

                "
                Print two sets of single valid invariants for each loop in the C program. 
                They should help prove the assertions. You can utilise '&&' or '||' if required. 
                No explanation. Your answer should be in the form i.e. for the first loop '__invariant(…); // Line A'. 
                Do this for every loop appropriately in the program i.e for the second loop '__invariant(…); // Line B'. 
                The end comment of all generated invariant(s) for every loop shall be labelled '// Line A' or '// Line B' or '// Line C' and so on depending on the number of loops in the program.
                No explanation.                
                """

            elif invariant_generation_iteration == 21 and invariant_generation_iteration<26: 

                code_modifying_prompt = """

                "
                \n"""+Prompt_Examples.code_example_4+"""\n

                "
                Based on these examples provided above can you generate an C invariant for the following code,
                “
                \n"""+c_benchmark+"""\n

                "

                Print two sets of double valid invariants for each loop in the C program.
                They should help prove the assertions. You can utilise '&&' or '||' if required. 
                No explanation. Your answer should be in the form i.e. for the first loop '__invariant(…); // Line A'. 
                Do this for every loop appropriately in the program i.e for the second loop '__invariant(…); // Line B'. 
                The end comment of all generated invariant(s) for every loop shall be labelled '// Line A' or '// Line B' or '// Line C' and so on depending on the number of loops in the program.
                No explanation.

                """

            elif invariant_generation_iteration == 26 and invariant_generation_iteration< 31:

                code_modifying_prompt = """

                "
                \n"""+Prompt_Examples.code_example_4+"""\n

                "
                Based on these examples provided above can you generate an C invariant for the following code,
                “
                \n"""+c_benchmark+"""\n

                "

                Print three sets of triple valid invariants for each loop in the C program.
                They should help prove the assertions. You can utilise '&&' or '||' if required. 
                No explanation. Your answer should be in the form i.e. for the first loop '__invariant(…); // Line A'. 
                Do this for every loop appropriately in the program i.e for the second loop '__invariant(…); // Line B'. 
                The end comment of all generated invariant(s) for every loop shall be labelled '// Line A' or '// Line B' or '// Line C' and so on depending on the number of loops in the program.
                No explanation.
                """
            if invariant_generation_iteration == 31:

                break;

            response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",
                prompt=code_modifying_prompt,
                max_tokens=2000,
                timeout = 600,
                temperature=0.3,
            )

            generated_modified_code = response['choices'][0]['text'].strip()

            generated_modified_code_format = re.compile(r".*(?P<invariant>__invariant\((\w|\s|\|\||&&|!|=|<|>|\+|-|\*|\?|:|\(|\))*\);)\s*//\s*(?P<line>Line\s*\w*)\s*")
            
            print(generated_modified_code)

            invariant_insertion = unmodified_code.split('\n')

            invariants_for_loops = generated_modified_code.splitlines()

            generated_invariants = [(m.group("line"), m.group("invariant")) for m in map(lambda x: generated_modified_code_format.match(x), invariants_for_loops) if m is not None] 

            grouped_invariants = defaultdict(list)
            for line, invariant in generated_invariants:
                if 'VERIFIER_nondet_int' not in invariant: 
                    grouped_invariants[line].append(invariant)

            print("The generated invariants are:" ,grouped_invariants)

            for insertion_index, line in enumerate(invariant_insertion):
                print("CHECK AND GROUPING STARTED FOR THE GENERATED INVARIANTS!")
                if '// Line A' in line and 'Line A' in grouped_invariants:
                    invariant_insertion.insert(insertion_index+1, '\n'.join(grouped_invariants['Line A']))
                    print("FIRST LINE: LINE A GROUPED INVARIANTS DONE!")
                elif '// Line B' in line and 'Line B' in grouped_invariants:
                    invariant_insertion.insert(insertion_index+1, '\n'.join(grouped_invariants['Line B']))
                    print("FIRST LINE: LINE B GROUPED INVARIANTS DONE!")
                    break

            new_modified_code  = '\n'.join(invariant_insertion)

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
                invariant_generation_iteration+=1
                total_iterations_for_benchmarks+=1
                index = 0
                print("ESMBC + Vampire execution has encountered an error")
                print("Code Generation is occurring again")
                print("Generated Invariant Number: ", invariant_generation_iteration)
                print("Total Iterations for all benchmarks: ", total_iterations_for_benchmarks)
                print('\n'*5)
                total_duration_spent_on_benchmarks+=total_time_per_benchmark
                total_duration_spent_on_each_benchmark += total_time_per_benchmark
                if "ERROR: PARSING ERROR" in run_esbmc_with_script.stderr:
                    parse_error_iterations+=1
                    print('----------------------------------------------------------')
                    print("Parse Error Iteration Count: ",parse_error_iterations)
                    print('----------------------------------------------------------')
                    print('\n'*5)
                time.sleep(1)
                if total_time_per_benchmark >= 600 or invariant_generation_iteration == 31:
                    print("The Duration Limit / Invariant Generation Iteration for the Particular Benchmark, " + name_of_the_c_benchmark_file + " has exceeded.")
                    print("Or Too much time spent on ESBMC and Vampire. ") 
                    print('----------------------------------------------------------')
                    print('END OF BENCHMARK ATTEMPT ON: ', name_of_the_c_benchmark_file)
                    print('----------------------------------------------------------')
                    print('\n'*2)
                    c_benchmarks_unsuccessful.append((name_of_the_c_benchmark_file, str(total_duration_spent_on_benchmarks), str(total_duration_spent_on_each_benchmark), invariant_generation_iteration, parse_error_iterations))
                    total_duration_spent_on_each_benchmark = 0
                    break
            else: 
                invariant_generation_iteration+=1
                total_iterations_for_benchmarks+=1
                total_duration_spent_on_benchmarks+=total_time_per_benchmark
                total_duration_spent_on_each_benchmark+= total_time_per_benchmark
                print("ESBMC + Vampire ran SUCCESSFULLY")
                print("Generated Successful Invariant on Iteration Number: ", invariant_generation_iteration)
                print("Total Benchmark Iterations: ", total_iterations_for_benchmarks)
                print(run_esbmc_with_script.stdout)
                print('----------------------------------------------------------')
                print('END OF BENCHMARK ATTEMPT ON: ', name_of_the_c_benchmark_file)
                print('----------------------------------------------------------')
                print('\n'*2)
                c_benchmarks_successful.append((name_of_the_c_benchmark_file, str(total_time_per_benchmark), str(total_duration_spent_on_benchmarks), str(total_duration_spent_on_each_benchmark), invariant_generation_iteration, parse_error_iterations))
                total_duration_spent_on_each_benchmark = 0
                break              

c_benchmark_iteration_average_number = total_iterations_for_benchmarks/(len(c_benchmarks_successful) + len(c_benchmarks_unsuccessful))  

c_benchmark_iteration_average_duration = (total_duration_spent_on_benchmarks/total_iterations_for_benchmarks) if total_iterations_for_benchmarks > 0 else 0 

print("Number of the Code2Inv Benchmarks Solved: " + str(len(c_benchmarks_successful)))
print("The names of the Benchmark Files that were Solved: ")
print('\n'.join(map(str, c_benchmarks_successful)))
print("Number of the Code2Inv Benchmarks that were not Solved: " + str(len(c_benchmarks_unsuccessful)))
print("The names of the Benchmark Files that were not Solved: ")
print('\n'.join(map(str, c_benchmarks_unsuccessful)))
print("Average time per iteration in Seconds: " + str(c_benchmark_iteration_average_duration) + " s") 
print("Total Time for all Benchmarks in Seconds: " + str(total_duration_spent_on_benchmarks) + " s")
print("Average number of iterations for Solved Benchmark Files: " + str(c_benchmark_iteration_average_number) + " iterations.") 
print("Iterations for all benchmarks total: " + str(total_iterations_for_benchmarks))

            

