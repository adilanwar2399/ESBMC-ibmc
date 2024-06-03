########### CONSTRAINED PROMPT #################
########### EX 1: SINGLE INVARIANT #############
########### EX 2: ABSOLUTE INVARIANTS ##########
########### EX 3: MULTIPLE INVARIANTS ##########

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

                The invariant, __invariant(x==0 || z>=y);, holds in this while loop. 
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

                The invariant, __invariant(abs(x - y) <= 10);, holds in this while loop.

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

                        These invariants: 
                        __invariant(sn == i - 1); 
                        __invariant(sn == 0 || size >= 0);
                        __invariant(size < 0 || i <= size + 1);
                        hold in this while loop.
                       
"""

