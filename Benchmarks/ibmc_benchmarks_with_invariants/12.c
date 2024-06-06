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
  int x = __VERIFIER_nondet_int();
  int y = __VERIFIER_nondet_int();
  int z1 = __VERIFIER_nondet_int();
  int z2 = __VERIFIER_nondet_int();
  int z3 = __VERIFIER_nondet_int();
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
if ( (y == 0) )
__VERIFIER_assert( (x != 20) );

}
