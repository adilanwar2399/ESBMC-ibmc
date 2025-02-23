extern void abort(void);
extern void __assert_fail(const char *, const char *, unsigned int, const char *); 
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
  
  int i = __VERIFIER_nondet_int();
  int x = __VERIFIER_nondet_int();
  int y = __VERIFIER_nondet_int();
  int z1 = __VERIFIER_nondet_int();
  int z2 = __VERIFIER_nondet_int();
  int z3 = __VERIFIER_nondet_int();
  
  (i = 0);
  __ESBMC_assume((x >= 0));
  __ESBMC_assume((y >= 0));
  __ESBMC_assume((x >= y));
  
  while (__VERIFIER_nondet_int()) {
    if ( (i < y) )
    {
    (i  = (i + 1));
    }

  }
  
if ( (i < y) )
__VERIFIER_assert( (0 <= i) );
}
