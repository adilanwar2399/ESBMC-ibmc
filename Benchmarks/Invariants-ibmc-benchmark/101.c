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
  int n = __VERIFIER_nondet_int();
  int x = __VERIFIER_nondet_int();
  // pre-conditions
  (x = 0);
  // loop body
  __invariant(n < 0 || x <= n);
  while ((x < n)) {
    {
    (x  = (x + 1));
    }

  }
  // post-condition
if ( (x != n) )
__VERIFIER_assert( (n < 0) );

}