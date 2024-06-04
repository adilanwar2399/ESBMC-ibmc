
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
int __VERIFIER_nondet_int();

int abs(int x){
  return x < 0 ? -x : x;
}

int main() {
    int a = __VERIFIER_nondet_int();
    int c = __VERIFIER_nondet_int();
    int m = __VERIFIER_nondet_int();
    int j = __VERIFIER_nondet_int();
    int k = __VERIFIER_nondet_int();

    __ESBMC_assume(a <= m);
    j = 0;
    k = 0;

    while ( k < c) {
        if(m < a) {
            m = a;
        }
        k = k + 1;
    }

    __VERIFIER_assert( a <=  m);
}
