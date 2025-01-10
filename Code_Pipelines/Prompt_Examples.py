code_example_1 = """
                
                First Example:
                "
                extern void abort(void);
                extern void __assert_fail(const char *, const char *, unsigned int, const char *) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__noreturn__));
                void reach_error() { __assert_fail("0", "vnew2.c", 3, "reach_error"); }
                extern void abort(void);
                void assume_abort_if_not(int cond) {
                  if(!cond) {abort();}
                }
                void __VERIFIER_assert(int cond) {
                  if (!(cond)) {
                    ERROR: {reach_error();abort();}
                  }
                  return;
                }

                #define FORALL(Var, Type, Cond)       \
                  Type Var;                           \
                  __invariant(__forall(Var, Cond));   \

                #define EXISTS(Var, Type, Cond)       \
                  Type Var;                           \
                  __invariant(__exists(Var, Cond));   \

                int __VERIFIER_nondet_int();

                int main()
                {
                    int x = 0;
                    int y = __VERIFIER_nondet_int();
                    int z = __VERIFIER_nondet_int();

                    __invariant(x == 0 || z >= y);

                    while(x < 5) {
                       x += 1;
                       if( z <= y) {
                          y = z;
                       }
                    }

                    __VERIFIER_assert (z >= y);
                }

                "

                The invariant, __invariant(x==0 || z>=y);, holds in this while loop because of the following step by step explanation,
                "
                    The Initialization:
                        At the beginning of the loop:
                            x is initialized to 0.
                            y and z are assigned nondeterministic integer values.
                        Invariant holds:
                            x == 0 is true initially.
                            Since y and z are arbitrary, z >= y may or may not hold initially.

                    The Base Case (Inductive Base):
                        Assumption:
                            Assume the invariant x == 0 || z >= y holds at the start of an arbitrary iteration.

                    The Inductive Step comprises of the following:
                        Analysis within the Iteration:
                            x increments by 1.
                            If z <= y, y is updated to z.
                            Thus, x increases monotonically, and y either decreases or remains the same.
                        The End of Iteration:
                            The loop terminates when x reaches 5.
                            If x is now 5, it satisfies x == 0.
                            If x is not 5, the loop continues, and the invariant is still maintained.
                            If z >= y held initially, it's either maintained or strengthened due to the loop's logic. If z <= y, y is updated to z, implying z >= y.
                        The Conclusion:
                            The invariant holds at the end of the iteration if it holds at the beginning.

                    The Termination:
                        The loop terminates when x becomes 5.
                        At loop termination, either x == 0 or z >= y holds.
                        Therefore, the invariant x == 0 || z >= y holds upon loop termination.

                    The Overall Conclusion:
                        The loop invariant x == 0 || z >= y is maintained throughout the loop execution.
                        This ensures that the assertion __VERIFIER_assert(z >= y) is valid as it aligns with the loop invariant.

                In summary, the step-by-step explanation clarifies how the loop invariant holds true from initialization through each iteration until termination, ensuring the correctness of the assertion in relation to the loop's behavior
                “.
"""

code_example_2= """

                Second Example:
                "
                extern void abort(void);
                extern void __assert_fail(const char *, const char *, unsigned int, const char *) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__noreturn__));
                void reach_error() { __assert_fail("0", "vnew2.c", 3, "reach_error"); }
                extern void abort(void);
                void assume_abort_if_not(int cond) {
                  if(!cond) {abort();}
                }
                void __VERIFIER_assert(int cond) {
                  if (!(cond)) {
                    ERROR: {reach_error();abort();}
                  }
                  return;
                }

                #define FORALL(Var, Type, Cond)       \
                  Type Var;                           \
                  __invariant(__forall(Var, Cond));   \

                #define EXISTS(Var, Type, Cond)       \
                  Type Var;                           \
                  __invariant(__exists(Var, Cond));   \

                int __VERIFIER_nondet_int();

                int abs(int x){
                  return x < 0 ? -x : x;
                }

                int main() {
                  // variable declarations
                  int x = __VERIFIER_nondet_int();
                  int y = __VERIFIER_nondet_int();
                  // pre-conditions
                  __ESBMC_assume((x >= 0));
                  __ESBMC_assume((x <= 10));
                  __ESBMC_assume((y <= 10));
                  __ESBMC_assume((y >= 0));
                  // loop body

                  __invariant(abs(x - y) <= 10);
                  while (__VERIFIER_nondet_int()) {
                    {
                    (x  = (x + 10));
                    (y  = (y + 10));
                    }

                  }
                  // post-condition
                  if ( y == 0 )
                    __VERIFIER_assert( (x != 20) );

                }

                "

                The invariant, __invariant(abs(x - y) <= 10);, holds in this while loop because of the following step by step explanation,
                "
                    Variable Declaration:


                    int x = __VERIFIER_nondet_int();
                    int y = __VERIFIER_nondet_int();

                    Two integer variables x and y are declared and initialized with non-deterministic values using __VERIFIER_nondet_int(). This means their values can be anything.

                    Pre-conditions:

                    __ESBMC_assume((x >= 0));
                    __ESBMC_assume((x <= 10));
                    __ESBMC_assume((y <= 10));
                    __ESBMC_assume((y >= 0));

                    These assumptions restrict the possible values of x and y. They ensure that both x and y are between 0 and 10 (inclusive).

                    Loop Body:

                    while (__VERIFIER_nondet_int()) {
                        x = (x + 10);
                        y = (y + 10);
                    }

                    Inside the loop, x and y are incremented by 10 in each iteration. The loop continues until __VERIFIER_nondet_int() returns a falsy value, which is non-deterministic.

                    Invariant:

                    __invariant(abs(x - y) <= 10);

                    This is the invariant that holds true throughout the execution of the loop. It asserts that the absolute difference between x and y is always less than or equal to 10.

                    Post-condition:


                    if (y == 0)
                        __VERIFIER_assert(x != 20);

                    This condition checks if y eventually becomes 0 after the loop. If y is indeed 0, it asserts that x should not be equal to 20.

                    Now, let's analyze why the invariant abs(x - y) <= 10 holds true:

                    Initially, x and y are both non-deterministically chosen between 0 and 10.
                    In each iteration of the loop, both x and y are incremented by 10.
                    Since x and y are both incremented by the same value in each iteration, the absolute difference between them remains constant at 0.
                    The loop continues until __VERIFIER_nondet_int() returns a falsy value, which means the loop can execute any number of times.
                    Throughout these iterations, the absolute difference between x and y remains within the range of 0 to 10.
                    Therefore, the invariant abs(x - y) <= 10 holds true for this benchmark.

                    In summary, the step-by-step explanation clarifies how the loop invariant holds true from the first stage to the end.
                “. 
"""

code_example_3 = """

                Third Example:

                "
                        extern void abort(void);
                        extern void __assert_fail(const char *, const char *, unsigned int, const char *) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__noreturn__));
                        void reach_error() { __assert_fail("0", "vnew2.c", 3, "reach_error"); }
                        extern void abort(void);
                        void assume_abort_if_not(int cond) {
                          if(!cond) {abort();}
                        }
                        void __VERIFIER_assert(int cond) {
                          if (!(cond)) {
                            ERROR: {reach_error();abort();}
                          }
                          return;
                        }

                        #define FORALL(Var, Type, Cond)       \
                          Type Var;                           \
                          __invariant(__forall(Var, Cond));   \

                        #define EXISTS(Var, Type, Cond)       \
                          Type Var;                           \
                          __invariant(__exists(Var, Cond));   \

                        int __VERIFIER_nondet_int();

                        int main() {
                          // variable declarations
                          int i;
                          int size = __VERIFIER_nondet_int();
                          int sn;
                          // pre-conditions
                          (sn = 0);
                          (i = 1);
                          // loop body
                          __invariant(sn == i - 1);
                          __invariant(sn == 0  || size >= 0);
                          __invariant(size < 0 || i <= size + 1);
                          while ((i <= size)) {
                            {
                            (i  = (i + 1));
                            (sn  = (sn + 1));
                            }

                          }
                          // post-condition
                        if ( (sn != 0) )
                        __VERIFIER_assert( (sn == size) );

                        }
                        "
                        Below is a step by step explanation of why these invariants holds in the loop provided:

                        1. __invariant(sn == i - 1);

                           This invariant asserts that the variable `sn` is always equal to the variable `i - 1`. In other words, it ensures that the value of `sn` is always one less than the value of `i`. 

                           Step-by-step explanation:
                           - Initially, before entering the loop, `sn` is initialized to 0 and `i` is initialized to 1. So, `sn` is indeed one less than `i`.
                           - Inside the loop, both `i` and `sn` are incremented by 1 in each iteration. Since `sn` is always assigned the value of `i - 1`, this relationship is maintained throughout the loop.
                           - Therefore, this invariant holds true throughout the execution of the loop.

                        2. __invariant(sn == 0 || size >= 0);

                           This invariant asserts that either `sn` is equal to 0 or `size` is greater than or equal to 0. In other words, it ensures that either `sn` is 0 or `size` is non-negative.

                           Step-by-step explanation:
                           - Initially, before entering the loop, `sn` is initialized to 0. Since `sn` is 0, this part of the invariant holds true.
                           - Regarding the second part, `size` is assigned a non-deterministic value using `__VERIFIER_nondet_int()`, which means it could be any integer value including negative, zero, or positive.
                           - Since `size` is assigned a non-negative value, `size >= 0` holds true.
                           - Therefore, this invariant holds true throughout the execution of the loop.

                        3. __invariant(size < 0 || i <= size + 1);

                           This invariant asserts that either `size` is negative or `i` is less than or equal to `size + 1`. In other words, it ensures that either `size` is negative or `i` doesn't exceed `size + 1`.

                           Step-by-step explanation:
                           - Initially, before entering the loop, `i` is initialized to 1, and `size` is assigned a non-deterministic value. Since we have no information about the value of `size`, this invariant holds trivially before the loop.
                           - Inside the loop, `i` is incremented by 1 in each iteration, and `size` remains constant. Therefore, if `size` is negative, `size < 0` holds true, which satisfies the invariant. If `size` is non-negative, `i` is guaranteed to be less than or equal to `size + 1` because the loop condition ensures that `i` doesn't exceed `size`. Hence, this part of the invariant also holds true.
                           - Therefore, this invariant holds true throughout the execution of the loop.

                            In summary, the step-by-step explanation clarifies how each loop invariant holds true from initialization through each iteration until termination, ensuring the correctness of the assertion in relation to the loop's behaviour.
                            “. 
"""
code_example_4 = """
            "
                extern void abort(void);
                extern void __assert_fail(const char *, const char *, unsigned int, const char *) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__noreturn__));
                void reach_error() { __assert_fail("0", "vnew2.c", 3, "reach_error"); }
                extern void abort(void);
                void assume_abort_if_not(int cond) {
                 if(!cond) {abort();}
                }
                void __VERIFIER_assert(int cond) {
                 if (!(cond)) {
                   ERROR: {reach_error();abort();}
                 }
                 return;
                }

                #define FORALL(Var, Type, Cond)       \
                 Type Var;                           \
                 __invariant(__forall(Var, Cond));   \

                #define EXISTS(Var, Type, Cond)       \
                 Type Var;                           \
                 __invariant(__exists(Var, Cond));   \

                int __VERIFIER_nondet_int();

                int main()  
                {
                  int xin = __VERIFIER_nondet_int(); 
                  int yin = __VERIFIER_nondet_int();
                  int z = __VERIFIER_nondet_int();
                  __VERIFIER_assume(xin >=0);
                  __VERIFIER_assume(yin >= 0);
                  int x = xin;
                  int y = yin;
                  int result = 0;
                  
                  __invariant(result + x == xin);
                  __invariant(x>=0);
                  while (x > 0) 
                  {
                    { 
                      xin = xin;
                      result = result + 1; 
                      x = x - 1;
                    }
                  }
                  __invariant(result + y == xin + yin);
                  __invariant(y>=0);
                  while (y > 0) 
                  {
                      yin = yin;
                      xin = xin;
                    { 
                      result = result + 1; 
                      y = y - 1;
                    }  
                  }
                  __VERIFIER_assert(result == xin + yin);
                }


                To understand how the invariants in the code were synthesized and why they ensure the assertion `result == xin + yin` holds, let’s break it down step-by-step. We analyze the loops and their semantics to derive the invariants.

                ---

                ### **1. Analysis of the First Loop**
                The first loop reduces `x` until it reaches zero while incrementing `result`.

                #### **Key Variables at Start**
                - `xin`: The initial value of `x`, which remains constant throughout.
                - `x`: Decreases by 1 in each iteration.
                - `result`: Starts at 0 and increments by 1 in each iteration.

                #### **Loop Dynamics**
                - Each iteration updates:
                  - `x = x - 1`
                  - `result = result + 1`
                - The relationship between `x`, `result`, and `xin` needs to be maintained across iterations.

                #### **Synthesizing the Invariant**
                1. Initially, the sum of `result` and `x` equals `xin`:
                   
                   result + x = xin
                   
                   This equality is true initially because `result` starts at 0 and `x` starts at `xin`.

                2. During each iteration:
                   - `result` increases by 1 and `x` decreases by 1. These updates keep the sum result + x constant at xin.

                3. The invariant:
                   
                   result + x = xin
                   
                   is preserved in every iteration.

                4. Non-negativity of `x`:
                   - Since `x` starts at `xin >= 0` and decreases by 1 each time, it’s clear that x >= 0 during the loop.

                #### **Final Invariant for First Loop**
                - result + x = xin
                - x >= 0

                ---

                ### **2. Analysis of the Second Loop**
                The second loop reduces `y` until it reaches zero while further incrementing `result`.

                #### **Key Variables at Start**
                - `yin`: The initial value of `y`, which remains constant.
                - `y`: Decreases by 1 in each iteration.
                - `result`: Starts with the value obtained after the first loop.

                #### **Loop Dynamics**
                - Each iteration updates:
                  - `y = y - 1`
                  - `result = result + 1`
                - The relationship between `result`, `y`, `xin`, and `yin` needs to be maintained across iterations.

                #### **Synthesizing the Invariant**
                1. Before this loop begins:
                   - The result of the first loop ensures:
                     
                     result = xin
                     
                   - At this point, the new invariant to track is the sum result + y = xin + yin, where yin is the original value of y

                2. During each iteration:
                   - `result` increases by 1 and `y` decreases by 1. These updates keep the sum result + y constant at xin + yin.

                3. The invariant:
                   
                   result + y = xin + yin
                   
                   is preserved in every iteration.

                4. Non-negativity of `y`:
                   - Since `y` starts at yin >= 0  and decreases by 1 each time, it’s clear that y >= 0 during the loop.

                #### **Final Invariant for Second Loop**
                -> result + y = xin + yin}
                -> y>=0

                ---

                ### 3. Why Do These Invariants Ensure the Assertion Holds?

                At the end of both loops:
                1. After the first loop:
                   -> x = 0, so:
                     
                     result = xin
                     

                2. After the second loop:
                   -> y = 0, so:
                    
                     result = xin + yin
                     

                The assertion result = xin + yin follows directly from these invariants. By ensuring the invariants hold in both loops, the program guarantees the final assertion is valid.
            "
"""
