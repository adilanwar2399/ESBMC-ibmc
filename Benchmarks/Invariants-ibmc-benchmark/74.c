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
  // variable declarations
  int c = __VERIFIER_nondet_int();
  int x1 = __VERIFIER_nondet_int();
  int x2 = __VERIFIER_nondet_int();
  int x3 = __VERIFIER_nondet_int();
  int y = __VERIFIER_nondet_int();
  int z = __VERIFIER_nondet_int();
  // pre-conditions
  (c = 0);
  __ESBMC_assume((y >= 0));
  __ESBMC_assume((y >= 127));
  (z = (36 * y));
  // loop body
  __invariant(z >= y && c <= 36 && (c >= 0 || c < 36));
  while (__VERIFIER_nondet_int()) {
    if ( (c < 36) )
    {
    (z  = (z + 1));
    (c  = (c + 1));
    }

  }
  // post-condition
if ( (c < 36) )
__VERIFIER_assert( (z >= 0) );
}
