extern void abort(void);
//extern void __assert_fail(const char *, const char *, unsigned int, const char *) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__noreturn__));
//void reach_error() { __assert_fail("0", "vnew2.c", 3, "reach_error"); }
extern void abort(void);
void assume_abort_if_not(int cond) {
  if(!cond) {abort();}
}
// void sassert(int cond) {
//   if (!(cond)) {
//     ERROR: {reach_error();abort();}
//   }
//   return;
// }
//int nd();

int abs(int x){
  return x < 0 ? -x : x;
}

#include "seahorn/seahorn.h"
extern void __SEA_assume(bool);
extern int nd();
int main() {
  // variable declarations
  int i = nd();
  int x = nd();
  int y = nd();
  int z1 = nd();
  int z2 = nd();
  int z3 = nd();
  // pre-conditions
  (i = 0);
  __SEA_assume((x >= 0));
  __SEA_assume((y >= 0));
  __SEA_assume((x >= y));
  // loop body
  while (nd()) {
    if ( (i < y) )
    {
    (i  = (i + 1));
    }

  }
  // post-condition
if ( (i < y) )
sassert( (i < x) );
}
