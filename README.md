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
