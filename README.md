# LLM-Generated Invariants For Bounded Model Checking Without Loop Unrolling
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This repository contains tools, scripts and benchmarks relating to the paper titled _LLM-Generated Invariants For Bounded Model Checking Without Loop Unrolling_.

The folder structure is as follows:

```
root
├───Benchmarks
│   ├───ibmc_benchmarks
│   ├───ibmc_benchmarks_with_invariants
│   ├───paper_benchmarks
│   └───SeaHorn_Benchmarks
└───Code_Pipelines
```
  
We briefly mention what each folder contains:

## Benchmarks

A set of benchmarks that we refer to in our paper and test our tools on.

### ibmc_benchmarks

A set of 133 benchmarks originating from the [code2inv repository](https://github.com/PL-ML/code2inv/tree/master/benchmarks/C_instances/c). We have updated the benchmarks to use assertion syntax recognised by ESBMC and VeriAbs tools.

### ibmc_benchmarks_with_invariants

The same 133 benchmarks as above, but in this case all benchmarks that can successfully be verified by the ESBMC ibmc tool have their loops marked with the invariants that the tool generated and validated. The invariants are identified by a special function `__invariant(...)` that only our development branch of ESBMC (included in this release) can currently recognise.

### SeaHorn_benchmarks

Again, the same 133 benchmarks mentioned above, but in this instance the assertions are per the SeaHorn verifier's syntax. 

### paper_benchmarks

A number of benchmarks referred to in the paper that are not amongst the 133 benchmarks included in the other benchmark folders.

## Code_Pipelines

This folder contains a set of Python scripts for invoking our LLM pipelines. As mentioned in the paper, we developed 6 pipelines each of which invokes ChatGPT to annotate the benchmarks contained in the ibmc_benchmarks folder with invariants and then calls the ESBMC ibmc tool on the annotated benchmarks.

The names of the Python scripts directly link them with the pipelines discussed in the paper. The folder also contains a pair of Python scripts `Prompt_Examples.py` and `Prompt_Examples_2.py`. These are used by the pipeline scripts, but can be ignored by users of the repository. We discuss how to run the pipelines below.

# Running ESBMC with Vampire

The binaries of ESBMC and Vampire tools can be obtained by downloading one of the releases linked to this repo (if this has not already been done). The command to run ESBMC with Vampire to verify a benchmark:

`<path to ESBMC executable> <path to benchmark> --vampire-for-loops --ir --output <output file name> --vampire-path <path to Vampire executable> --no-bounds-check`

Note that for verification to succeed the benchmark must contain suitable invariants. It thus makes sense to invoke the tool on one of the benchmarks in the ibmc_benchmarks_with_invariants folder.

# Running the pipelines

Assuming that you are located in the root folder of this repo, the following commands can be used to execute any of the pipelines. Note that the pipelines invoke ChatGPT to obtain the candidate invariants and hence it is necessary to have a OpenAI API key to run the pipelines. To allow the scripts to make use of this key please set the environment variable `key_for_the_API` to hold your key. This can be done as follows:

`export key_for_the_API="<your key>"`

To run a pipeline do:

`cd Code_Pipelines`

`python3 <pipeline name> <path to ESBMC executable> <path to Vampire executable>`

This will start the pipeline running on all the benchmarks contained in the ibmc_benchmarks folder. 
