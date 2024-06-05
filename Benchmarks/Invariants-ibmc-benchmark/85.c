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
  (x = -15000);
  // loop body
  __invariant(x < 0 || ((y > 0)));
  while ((x < 0)) {
    {
    (x  = (x + y));
    (y  = (y + 1));
    }

  }
  // post-condition
__VERIFIER_assert( (y > 0) );
}
