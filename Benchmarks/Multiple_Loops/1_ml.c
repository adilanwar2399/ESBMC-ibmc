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
  
  while (x > 0) 
  {
    { 
      xin = xin;
      result = result + 1; 
      x = x - 1;
    }
  }
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
