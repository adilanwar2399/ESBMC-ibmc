import openai
import os
import subprocess 
import time
import Prompt_Examples
import Prompt_Examples_2


key_for_the_API = 'OPENAI API KEY'
openai.api_key = key_for_the_API


c_benchmarks = 'PATH TO CODE2INV BENCHMARKS'


c_benchmark_time_limit = 600 


c_benchmarks_successful = []


c_benchmarks_unsuccessful = []


total_duration_spent_on_benchmarks = 0


total_duration_spent_on_each_benchmark = 0  


total_iterations_for_benchmarks = 0


for name_of_the_c_benchmark_file in os.listdir(c_benchmarks):
    if name_of_the_c_benchmark_file.endswith('.c'):

  
        invariant_generation_iteration = 0


        parse_error_iterations = 0 


        invariant_generated_correct_format = False


        c_benchmark_start_time = time.time()
        
        while True:


            if time.time() - c_benchmark_start_time >= c_benchmark_time_limit:
                print("Max Duration Limit Reached for the Benchmark.") 
                print("Time to move on to the next Benchmark")
                break


            with open(os.path.join(c_benchmarks, name_of_the_c_benchmark_file), 'r') as benchmark_read:
                c_benchmark = benchmark_read.read()


            line_numbered_code = c_benchmark.split('\n') 


            for position_index, line in enumerate(line_numbered_code):
                if line.strip().startswith(('while', 'for')): 
                    line_numbered_code.insert(position_index, "// Line A")
                    break

            unmodified_code = '\n'.join(line_numbered_code)
            print (unmodified_code)

            if invariant_generation_iteration <6:


                code_modifying_prompt = """
                
                "
                \n"""+Prompt_Examples.code_example_1+"""\n

                "
                "
                \n"""+Prompt_Examples.code_example_2+"""\n

                "
                "
                \n"""+Prompt_Examples.code_example_3+"""\n

                "

                Based on these examples provided above can you generate an C invariant for the following code,
                “
                \n"""+c_benchmark+"""\n

                "
                Print a valid C invariant for this loop that holds in the form '__invariant(...);' . 
                They should help prove the assertions. You can utilise '&&' or '||' if required. 
                No explanation. Your answer should be in the form '__invariant(…);' 
                Ensuring that it matches with this regular expression ^__invariant\((\w|\s|\|\||&&|!|=|<|>|\(|\))*\);$

                """

            elif invariant_generation_iteration == 6 and invariant_generation_iteration<11: 

                code_modifying_prompt = """
                "
                \n"""+Prompt_Examples_2.code_example_1+"""\n

                "
                "
                \n"""+Prompt_Examples_2.code_example_2+"""\n

                "
                "
                \n"""+Prompt_Examples_2.code_example_3+"""\n

                "

                Based on these examples provided above can you generate an C invariant for the following code,
                “
                \n"""+c_benchmark+"""\n

                "

                Print two valid invariants for this loop that all hold in the form '__invariant(...);' . 
                They should help prove the assertions. You can utilise '&&' or '||' if required. 
                No explanation. Your answer should be in the form '__invariant(…);'
                Ensuring that it matches with this regular expression ^__invariant\((\w|\s|\|\||&&|!|=|<|>|\(|\))*\);$

                """

            elif invariant_generation_iteration == 11 and invariant_generation_iteration<16:

                code_modifying_prompt = """
                "
                \n"""+Prompt_Examples.code_example_1+"""\n

                "
                "
                \n"""+Prompt_Examples.code_example_2+"""\n

                "
                "
                \n"""+Prompt_Examples.code_example_3+"""\n

                "
                Based on these examples provided above can you generate an C invariant for the following code,
                “
                \n"""+c_benchmark+"""\n

                "

                Print three valid invariants for this loop that all hold in the form '__invariant(...);' . 
                They should help prove the assertions. You can utilise '&&' or '||' if required. 
                No explanation. Your answer should be in the form '__invariant(…);'
                Ensuring that it matches with this regular expression ^__invariant\((\w|\s|\|\||&&|!|=|<|>|\(|\))*\);$

                """

            elif invariant_generation_iteration ==16 and invariant_generation_iteration<21:

                code_modifying_prompt = """
                
                "
                \n"""+Prompt_Examples_2.code_example_1+"""\n

                "
                "
                \n"""+Prompt_Examples_2.code_example_2+"""\n

                "
                "
                \n"""+Prompt_Examples_2.code_example_3+"""\n

                "

                Based on these examples provided above can you generate an C invariant for the following code,
                “
                \n"""+c_benchmark+"""\n

                "
                Print a valid invariant for this loop that holds in the form '__invariant(...);' . 
                They should help prove the assertions. You can utilise '&&' or '||' if required. 
                No explanation. Your answer should be in the form '__invariant(…);'
                Ensuring that it matches with this regular expression ^__invariant\((\w|\s|\|\||&&|!|=|<|>|\(|\))*\);$

                """

            elif invariant_generation_iteration == 21 and invariant_generation_iteration<26:         

                code_modifying_prompt = """
                "
                \n"""+Prompt_Examples.code_example_1+"""\n

                "
                "
                \n"""+Prompt_Examples.code_example_2+"""\n

                "
                "
                \n"""+Prompt_Examples.code_example_3+"""\n

                "

                Based on these examples provided above can you generate an C invariant for the following code,
                “
                \n"""+c_benchmark+"""\n

                "

                Print two valid invariants for this loop that all hold in the form '__invariant(...);' . 
                They should help prove the assertions. You can utilise '&&' or '||' if required. 
                No explanation. Your answer should be in the form '__invariant(…);'
                Ensuring that it matches with this regular expression ^__invariant\((\w|\s|\|\||&&|!|=|<|>|\(|\))*\);$

                """

            elif invariant_generation_iteration == 26 and invariant_generation_iteration < 31:


                code_modifying_prompt = """
                "
                \n"""+Prompt_Examples_2.code_example_1+"""\n

                "
                "
                \n"""+Prompt_Examples_2.code_example_2+"""\n

                "
                "
                \n"""+Prompt_Examples_2.code_example_3+"""\n

                "
                Based on these examples provided above can you generate an C invariant for the following code,
                “
                \n"""+c_benchmark+"""\n

                "

                Print three valid invariants for this loop that all hold in the form '__invariant(...);' . 
                They should help prove the assertions. You can utilise '&&' or '||' if required. 
                No explanation. Your answer should be in the form '__invariant(…);'
                Ensuring that it matches with this regular expression ^__invariant\((\w|\s|\|\||&&|!|=|<|>|\(|\))*\);$

                """
            elif invariant_generation_iteration == 31 and invariant_generation_iteration < 36:


                code_modifying_prompt = """
                "
                \n"""+Prompt_Examples.code_example_1+"""\n

                "
                "
                \n"""+Prompt_Examples.code_example_2+"""\n

                "
                "
                \n"""+Prompt_Examples.code_example_3+"""\n

                "
                Based on these examples provided above can you generate an C invariant for the following code,
                “
                \n"""+c_benchmark+"""\n

                "

                Print a valid invariant for this loop that holds in the form '__invariant(...);' . 
                They should help prove the assertions. You can utilise '&&' or '||' if required. 
                No explanation. Your answer should be in the form '__invariant(…);'
                Ensuring that it matches with this regular expression ^__invariant\((\w|\s|\|\||&&|!|=|<|>|\(|\))*\);$

                """
            elif invariant_generation_iteration == 36 and invariant_generation_iteration < 41:


                code_modifying_prompt = """
                "
                \n"""+Prompt_Examples_2.code_example_1+"""\n

                "
                "
                \n"""+Prompt_Examples_2.code_example_2+"""\n

                "
                "
                \n"""+Prompt_Examples_2.code_example_3+"""\n

                "
                Based on these examples provided above can you generate an C invariant for the following code,
                “
                \n"""+c_benchmark+"""\n

                "

                Print two valid invariants for this loop that all hold in the form '__invariant(...);' . 
                They should help prove the assertions. You can utilise '&&' or '||' if required. 
                No explanation. Your answer should be in the form '__invariant(…);'
                Ensuring that it matches with this regular expression ^__invariant\((\w|\s|\|\||&&|!|=|<|>|\(|\))*\);$

                """
            elif invariant_generation_iteration == 41 and invariant_generation_iteration < 46:

                code_modifying_prompt = """
                "
                \n"""+Prompt_Examples.code_example_1+"""\n

                "
                "
                \n"""+Prompt_Examples.code_example_2+"""\n

                "
                "
                \n"""+Prompt_Examples.code_example_3+"""\n

                "
                Based on these examples provided above can you generate an C invariant for the following code,
                “
                \n"""+c_benchmark+"""\n

                "

                Print three valid invariants for this loop that all hold in the form '__invariant(...);' . 
                They should help prove the assertions. You can utilise '&&' or '||' if required. 
                No explanation. Your answer should be in the form '__invariant(…);'
                Ensuring that it matches with this regular expression ^__invariant\((\w|\s|\|\||&&|!|=|<|>|\(|\))*\);$

                """
            elif invariant_generation_iteration == 46 and invariant_generation_iteration < 51:

                code_modifying_prompt = """
                "
                \n"""+Prompt_Examples_2.code_example_1+"""\n

                "
                "
                \n"""+Prompt_Examples_2.code_example_2+"""\n

                "
                "
                \n"""+Prompt_Examples_2.code_example_3+"""\n

                "
                Based on these examples provided above can you generate an C invariant for the following code,
                “
                \n"""+c_benchmark+"""\n

                "

                Print a valid invariant for this loop that holds in the form '__invariant(...);' . 
                They should help prove the assertions. You can utilise '&&' or '||' if required. 
                No explanation. Your answer should be in the form '__invariant(…);'
                Ensuring that it matches with this regular expression ^__invariant\((\w|\s|\|\||&&|!|=|<|>|\(|\))*\);$

                """
            elif invariant_generation_iteration == 51 and invariant_generation_iteration < 56:


                code_modifying_prompt = """
                "
                \n"""+Prompt_Examples.code_example_1+"""\n

                "
                "
                \n"""+Prompt_Examples.code_example_2+"""\n

                "
                "
                \n"""+Prompt_Examples.code_example_3+"""\n

                "
                Based on these examples provided above can you generate an C invariant for the following code,
                “
                \n"""+c_benchmark+"""\n

                "

                Print two valid invariants for this loop that all hold in the form '__invariant(...);' . 
                They should help prove the assertions. You can utilise '&&' or '||' if required. 
                No explanation. Your answer should be in the form '__invariant(…);'
                Ensuring that it matches with this regular expression ^__invariant\((\w|\s|\|\||&&|!|=|<|>|\(|\))*\);$

                """
            elif invariant_generation_iteration == 56 and invariant_generation_iteration< 61:

                code_modifying_prompt = """
                "
                \n"""+Prompt_Examples_2.code_example_1+"""\n

                "
                "
                \n"""+Prompt_Examples_2.code_example_2+"""\n

                "
                "
                \n"""+Prompt_Examples_2.code_example_3+"""\n

                "
                Based on these examples provided above can you generate an C invariant for the following code,
                “
                \n"""+c_benchmark+"""\n

                "

                Print three valid invariants for this loop that all hold in the form '__invariant(...);' . 
                They should help prove the assertions. You can utilise '&&' or '||' if required. 
                No explanation. Your answer should be in the form '__invariant(…);'
                Ensuring that it matches with this regular expression ^__invariant\((\w|\s|\|\||&&|!|=|<|>|\(|\))*\);$

                """    
 
            elif invariant_generation_iteration == 61:

                break;

            response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",
                prompt=code_modifying_prompt,
                max_tokens=35,
                timeout = 600, 
            )

            generated_modified_code = response['choices'][0]['text'].strip()
            print (generated_modified_code)
            
            invariant_insertion = unmodified_code.split('\n')

            for insertion_index, line in enumerate(invariant_insertion):
                if '// Line' in line:
                    invariant_insertion.insert(insertion_index+1, generated_modified_code)
                    break

            new_modified_code  = '\n'.join(invariant_insertion)

            print(new_modified_code)

            with open("new_modified_code.c", "w") as file:
                file.write(new_modified_code)

            start_time = time.time()
  
            esbmc_executable_path = "PATH TO ESBMC" 


            esbmc_command = [esbmc_executable_path, "new_modified_code.c"]


            vampire_executable_path_addition = "PATH TO VAMPIRE".split(" ")


            vampire_executable_command = [*esbmc_command, *vampire_executable_path_addition]


            run_esbmc_with_script = subprocess.run(vampire_executable_command, capture_output=True, text=True)

            end_time = time.time()

            total_time_per_benchmark = end_time - start_time

            os.remove('new_modified_code.c')

            print("C Benchmark Name: " + name_of_the_c_benchmark_file + "\n" + "Total Time Spent in Seconds: " + str(end_time - start_time))

            if run_esbmc_with_script.returncode !=0: 
                invariant_generation_iteration+=1
                total_iterations_for_benchmarks+=1
                print("ESMBC + Vampire execution has encountered an error")
                print(run_esbmc_with_script.stderr)
                print("Code Generation is occurring again")
                print("Generated Invariant Number: ", invariant_generation_iteration)
                print("Total Iterations for all benchmarks: ", total_iterations_for_benchmarks)
                total_duration_spent_on_benchmarks+=total_time_per_benchmark
                total_duration_spent_on_each_benchmark += total_time_per_benchmark
                if "ERROR: PARSING ERROR" in run_esbmc_with_script.stderr:
                    parse_error_iterations+=1
                    print("Parse Error Iteration Count: ",parse_error_iterations)
                time.sleep(1)
                if total_time_per_benchmark >= 600 or invariant_generation_iteration == 61:
                    print("The Duration Limit / Invariant Generation Iteration for the Particular Benchmark, " + name_of_the_c_benchmark_file + " has exceeded.")
                    print("Or Too much time spent on ESBMC and Vampire. ") 
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



