# LLM-Generated-Invariants-For-Bounded-Model-Checking-Without-Loop-Unrolling
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Here is the tool invariant based bounded model checking (ibmc) tool that is based on the ESBMC-Vampire Integration with LLMs Project. 

This project contains the pipelines to test the prompt engineering with the ChatGPT LLM 3.5 Turbo-Instruct Model in order to generate invariants for various c programs from the code2inv benchmark set. 

The prompt engineering technique utilised here comprises of the following known as the chain of thought approach where you have this structure: 

Prompt Engineering: Chain of Thought Approach.

Give a Solved Example Benchmark to the LLM 

{
 C code with loop ...
} 

Correct Loop invariant is e.g. x>y

(Important Note: The following Step-by-step explanation is not used for Constrained Prompts (Prompt_Examples_2.py file); this is only for Unconstrained Prompts (Prompt_Examples.py file)

Explain in sequential steps as to why the invariant x>y is successful. 

(Note: Here you can ask the LLM to generate a sequential break down in order to understand and break down in steps why the invariant is correct - as that way it will break down and tell the user how and why this invariant is correct and will work in the same way by feeding it that same information in that same style - as a prompt.) 

Then utilise the benchmark (C program) that you need to generate the correct invariant(s) for:

{
   C code with loop ...
}

Then specify the conditions of the output and the form that the output will appear in plus any constraints or extra contextual information may help as well.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The tool has 6 pipelines exploring 3 different approaches in this integration. 

1. Using Full vs Constrained Prompts to generate invariants for the benchmarks. 
2. Using Full vs Constrained Prompts to generate invariants for the benchmarks - whilst using regular expressions (regex).
3. Using Both Prompts to generate invariants - with and without regex, respectively.

Stages of the Project Pipeline: 

1. Detect For loops iteratively.
2. Ask the LLM to generate an invariant for each loop. 
3. Requirements:


   a. GPT 3.5 Turbo-Instruct is being used (OpenAI).



   b. Good Prompting for LLMs (Chain of thought used; Tree of thought is also a popular choice).
   
5. Ask the respective LLM to generate only loop invariants that are going to be placed before each loop.
6. Check whether the generated loop invariant can be parsed (implementation is done via using regex); if the generated responses match the pattern defined through the regular expression then the rest of the pipeline will execute - otherwise it will regenerate and re-match until the match is successful) - this reduces the parsing errors and increases the number of useful iterations per benchmark.
   - Note: This step is skipped if regex is not used in the pipelines. 
7. Repeat for the next loop (multiple loops check is under development so current pipeline skips this step).
8. Once done, call ESBMC-Vampire.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Experimental Setup: 

The requirements are that you have either a macOS or a Linux OS (Ubuntu or Debian) as the tools that need installing require at least one of these operating systems preferably Linux as it is easier. 

Binary Files for both Operating Systems will be available here: 
- ESBMC
- Vampire

Seahorn: 
- This tool's build version can be installed via the github link here: https://github.com/seahorn/seahorn
- Alternatively, this could be ran via the docker - instructions to install and run this via the docker are also in the link above.
- And then you can run the files using the commands mentioned in the repo.

VeriAbs: 
- Here you will need the script of veriabs which can be obtained via downloading the latest version of VeriAbs and make sure that you also have the sv-benchmark properties in particular the unreach_call.prp to ensure that veriabs can run properly with the execution commands.

Pipeline: 

To run the pipelines the paths to ESBMC and Vampire need to be updated with the correct syntax and alongside this the path to the code2inv ibmc benchmarks need to be added to the pipeline.py file that you want to run. Also, you need to have an OpenAI API account in order to create an OPENAI API KEY allowing the LLM to generate invariants that can then be used as intended in the pipeline code.

Alternatively, the invariants of the solved benchmarks can be added and then the can be inserted into the c benchmarks and then tested by ESBMC and Vampire to see if Verification is Successful or not.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

References: 

1. https://platform.openai.com/docs/api-reference
2. https://platform.openai.com/docs/guides/text-generation
3. https://platform.openai.com/docs/guides/prompt-engineering/strategy-write-clear-instructions
4. https://github.com/FrontAnalyticsInc/data-winners/blob/main/generation-api-openai/openai-text-generation-examples-in-python.ipynb
5. https://stackoverflow.com/questions/31126596/saving-response-from-requests-to-file
6. http://www.java2s.com/Code/Python/File/AddingLineNumberstoaPythonScript.htm
7. https://chat.openai.com/
8. https://stackoverflow.com/questions/48797580/how-to-add-line-numbers-in-a-list
9. https://docs.python.org/3/c-api/index.html
10. https://www.geeksforgeeks.org/python-os-path-join-method/
11. https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory
12. https://mathai2023.github.io/papers/28.pdf
13. https://arxiv.org/pdf/2302.11382.pdf
14. https://arxiv.org/abs/2305.10601
15. https://stackoverflow.com/questions/19389490/how-do-pythons-any-and-all-functions-work
16. https://www.w3schools.com/python/ref_func_map.asp
17. https://stackoverflow.com/questions/65333658/how-to-join-values-of-map-in-python
18. https://docs.python.org/3/library/re.html
19. https://stackoverflow.com/questions/64173161/python-regular-expression-substitution-function-using-lambda-in-the-replacement
