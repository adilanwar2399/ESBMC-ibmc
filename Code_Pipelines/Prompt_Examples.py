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

