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
  int i = nd();
  int j = nd();
  int x = nd();
  int y = nd();
  int z1 = nd();
  int z2 = nd();
  int z3 = nd();
  // pre-conditions
  (i = x);
  (j = y);
  // loop body
  while ((x != 0)) {
    {
    (x  = (x - 1));
    (y  = (y - 1));
    }

  }
  // post-condition
if ( (y != 0) )
sassert( (i != j) );

}
