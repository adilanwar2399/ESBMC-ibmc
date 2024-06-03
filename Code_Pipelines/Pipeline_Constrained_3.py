########### REGEX CONSTRAINED PROMPT PIPELINE ##########

import openai
import os
import subprocess 
import time
import Prompt_Examples
import Prompt_Examples_2
import re

# Set your OpenAI GPT-3.5 Turbo API key (Unique to the user account)
key_for_the_API = 'OPENAI API KEY'
openai.api_key = key_for_the_API


# Path to the Code2Inv or other Benchmarks.
c_benchmarks = 'PATH TO CODE2INV BENCHMARKS'

# In the respective directory each Benchmark is set a limit of 10 mins aka 600s.
c_benchmark_time_limit = 600 

# List of all the Solved Benchmarks aka Successful Ones.
c_benchmarks_successful = []

# List of the Unsolved Benchmarks aka Unsuccessful Ones.
c_benchmarks_unsuccessful = []

# Total Duration Spent on the Benchmarks.
total_duration_spent_on_benchmarks = 0

# Total Duration Spent on each Benchmark.
total_duration_spent_on_each_benchmark = 0  

# Total number of the Iterations for each Benchmark.
total_iterations_for_benchmarks = 0

# Check the Name of each individual file in the directory and check if it is a C file.
# If it is a C file then execute the process on it respectively.
for name_of_the_c_benchmark_file in os.listdir(c_benchmarks):
    if name_of_the_c_benchmark_file.endswith('.c'):

        # LLM GPT-3.5 Turbo-Instruct Code Generated Invariant Iteration Counter.
        invariant_generation_iteration = 0

        # LLM GPT-3.5 Turbo-Instruct Code Generated Invariant which lead to Parsing Errors Counter.
        parse_error_iterations = 0 

        # Variable to check if the generated invariant is in the correct format or not.
        invariant_generated_correct_format = False

        # Time check added. 
        c_benchmark_start_time = time.time()
        
        while True:

            # Checks if the total time of the benchmark has exceeded the limit of 600s or not.
            # If it has then stop and change the benchmark.
            if time.time() - c_benchmark_start_time >= c_benchmark_time_limit:
                print("Max Duration Limit Reached for the Benchmark.") 
                print("Time to move on to the next Benchmark")
                break

            # Read the contents of the selected benchmark.
            with open(os.path.join(c_benchmarks, name_of_the_c_benchmark_file), 'r') as benchmark_read:
                c_benchmark = benchmark_read.read()

            # Here the respective C benchmark gets split into a line array 
            # via splitting the respective string on the new line operator.
            line_numbered_code = c_benchmark.split('\n') 

            # Here for each line checks if line.stripwhitespace.startswith(while or for) 
            # and store the line number (index into line array).
            for position_index, line in enumerate(line_numbered_code):
                if line.strip().startswith(('while', 'for')): 
                    # Insert a new index into the array at the line number and 
                    # populate it with the string "// Line A"
                    line_numbered_code.insert(position_index, "// Line A")
                    break

            # Here the line array respectively turns back into a string to use in the prompt.
            unmodified_code = '\n'.join(line_numbered_code)
            print (unmodified_code)

            # Here the number of iterations will be selected for each prompt type.
            # Chain of Thought Approach is used for Prompt Engineering here. 
            # The contents of the Prompts are stored in the Prompt Examples File.
            if invariant_generation_iteration <6:
            
                # In this prompt approach I have added 3 different examples solved in a step by step manner.
                # The Benchmark types that are solved and are being use comprise of:
                # Single Invariant Benchmarks
                # Absolute Invariant Benchmarks.
                # Multiple Invariant Benchmarks.


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
                Print a valid C invariant for this loop that holds in the form '__invariant(...);' . 
                They should help prove the assertions. You can utilise '&&' or '||' if required. 
                No explanation. Your answer should be in the form '__invariant(…);' 
                Ensuring that it matches with this regular expression ^__invariant\((\w|\s|\|\||&&|!|=|<|>|\(|\))*\);$

                """

            elif invariant_generation_iteration == 6 and invariant_generation_iteration<11: 
            
                # In this prompt approach I have added 3 different examples solved in a step by step manner.
                # The Benchmark types that are solved and are being use comprise of:
                # Single Invariant Benchmarks
                # Absolute Invariant Benchmarks.
                # Multiple Invariant Benchmarks.


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

                # In this prompt approach I have added 3 different examples solved in a step by step manner.
                # The Benchmark types that are solved and are being use comprise of:
                # Single Invariant Benchmarks
                # Absolute Invariant Benchmarks.
                # Multiple Invariant Benchmarks.


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
            # Here the number of iterations will be selected for each prompt type.
            # Chain of Thought Approach is used for Prompt Engineering here. 
            # The contents of the Prompts are stored in the Prompt Examples File.
            elif invariant_generation_iteration ==16 and invariant_generation_iteration<21:
            
                # In this prompt approach I have added 3 different examples solved in a step by step manner.
                # The Benchmark types that are solved and are being use comprise of:
                # Single Invariant Benchmarks
                # Absolute Invariant Benchmarks.
                # Multiple Invariant Benchmarks.


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
            
                # In this prompt approach I have added 3 different examples solved in a step by step manner.
                # The Benchmark types that are solved and are being use comprise of:
                # Single Invariant Benchmarks
                # Absolute Invariant Benchmarks.
                # Multiple Invariant Benchmarks.


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

            elif invariant_generation_iteration == 26 and invariant_generation_iteration< 31:

                # In this prompt approach I have added 3 different examples solved in a step by step manner.
                # The Benchmark types that are solved and are being use comprise of:
                # Single Invariant Benchmarks
                # Absolute Invariant Benchmarks.
                # Multiple Invariant Benchmarks.


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
            # Here the number of iterations will be selected for each prompt type.
            # Chain of Thought Approach is used for Prompt Engineering here. 
            # The contents of the Prompts are stored in the Prompt Examples File.
            elif invariant_generation_iteration == 31:

                break;

            # Here is the use of the OpenAI GPT-3.5 Turbo API to generate code unspecified completion and randomness.
            response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",
                prompt=code_modifying_prompt,
                max_tokens=35,
                timeout = 600, # 600s Time limit
            )

            # Here the generated modified code will be obtained.
            generated_modified_code = response['choices'][0]['text'].strip()
            print (generated_modified_code)

            generated_modified_code_format= generated_modified_code_format = re.compile(r"__invariant\((\w|\s|\|\||&&|!|=|<|>|\?|:|\(|\))*\);")
            print (generated_modified_code_format)

            generated_modified_code_format_lines = generated_modified_code.split('\n')
            print (generated_modified_code_format_lines)

            generated_invariants = [m.group(0) for m in map(lambda x: generated_modified_code_format.match(x), generated_modified_code_format_lines) if m is not None] 
            print (generated_invariants)

            generated_invariants_str = '\n'.join(generated_invariants) 
            print (generated_invariants_str)  


            # Here the insertion of the LLM Gpt-3.5 Turbo generated invariant(s) will take place.
            invariant_insertion = unmodified_code.split('\n')

            # LLM produced the invariants and they get inserted 
            # in the appropriate line number of the the respective line array.
            for insertion_index, line in enumerate(invariant_insertion):
                if '// Line' in line:
                    invariant_insertion.insert(insertion_index+1, generated_invariants_str)
                    break

            # New modified program is ready to be used by ESBMC and Vampire after C file conversion.
            new_modified_code  = '\n'.join(invariant_insertion)

            print(new_modified_code)

            # Here the respective generated C code will be saved as a new file.
            # Note: w is for the respective write mode.
            with open("new_modified_code.c", "w") as file:
                file.write(new_modified_code)

            start_time = time.time()
            # Here the specific pathway to the respective ESBMC executable is used.
            esbmc_executable_path = "PATH TO ESBMC" 

            # Here is the respective command to ensure that  the esbmc executable,
            # and the respective newly generated modified code are linked and so that they 
            # can be processed together when ran with ESBMC + Automated Theorem Prover Vampire too.
            esbmc_command = [esbmc_executable_path, "new_modified_code.c"]

            # Below is the vampire executable path addition of the output file too - this is stored as an array.
            vampire_executable_path_addition = "PATH TO VAMPIRE".split(" ")

            # Below is the vampire executable command to allow esbmc and vampire to run together with each other on the c file.
            vampire_executable_command = [*esbmc_command, *vampire_executable_path_addition]

            # Now, here is the subprocess allows the subprocess to call esbmc on the modified C code file.
            run_esbmc_with_script = subprocess.run(vampire_executable_command, capture_output=True, text=True)

            end_time = time.time()

            total_time_per_benchmark = end_time - start_time

            os.remove('new_modified_code.c')

            print("C Benchmark Name: " + name_of_the_c_benchmark_file + "\n" + "Total Time Spent in Seconds: " + str(end_time - start_time))
            # These will respectively output either verification successful or unsuccessful, 
            # depending on whether or not ESBMC successfully runs.
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
                time.sleep(2)
                if total_time_per_benchmark >= 600 or invariant_generation_iteration == 31:
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

# Here the calculation of how to obtain the average number of iterations it takes to solve the benchmarks are done.
c_benchmark_iteration_average_number = total_iterations_for_benchmarks/(len(c_benchmarks_successful) + len(c_benchmarks_unsuccessful))  

# Here the calculation of how to obtain the average duration it takes to solve the benchmarks are done.
c_benchmark_iteration_average_duration = (total_duration_spent_on_benchmarks/total_iterations_for_benchmarks) if total_iterations_for_benchmarks > 0 else 0 

# Below are the respective metrics that will be outputted one the whole set of the Benchmarks are completed.
# Note these ones are tailored for Code2Inv Benchmarks.
print("Number of the Code2Inv Benchmarks Solved: " + str(len(c_benchmarks_successful)))
print("The names of the Benchmark Files that were Solved: ")
print('\n'.join(map(str, c_benchmarks_successful)))
print("Number of the Code2Inv Benchmarks that were not Solved: " + str(len(c_benchmarks_unsuccessful)))
print("The names of the Benchmark Files that were not Solved: ")
print('\n'.join(map(str, c_benchmarks_unsuccessful)))
print("Average time per iteration in Seconds: " + str(c_benchmark_iteration_average_duration) + " s") 
print("Total Time for all Benchmarks in Seconds: " + str(total_duration_spent_on_benchmarks) + " s")
print("Average number of iterations for Benchmark Files: " + str(c_benchmark_iteration_average_number) + " iterations.") 
print("Iterations for all benchmarks total: " + str(total_iterations_for_benchmarks))



