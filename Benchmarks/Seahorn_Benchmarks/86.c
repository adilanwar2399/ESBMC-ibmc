#include "seahorn/seahorn.h"
extern void abort(void);
void assume_abort_if_not(int cond) {
  if(!cond) {abort();}
}

int abs(int x){
  return x < 0 ? -x : x;
}
extern void __SEA_assume(bool);
extern int nd();
int main() {
  // variable declarations
  int x = nd();
  int y = nd();
  int z1 = nd();
  int z2 = nd();
  int z3 = nd();
  // pre-conditions
  (x = -50);
  // loop body
  while ((x < 0)) {
    {
    (x  = (x + y));
    (y  = (y + 1));
    }

  }
  // post-condition
sassert( (y > 0) );
}
