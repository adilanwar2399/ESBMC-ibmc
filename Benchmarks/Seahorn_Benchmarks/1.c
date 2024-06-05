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
  // pre-conditions
  (x = 1);
  (y = 0);
  // loop body
  while ((y < 100000)) {
    {
    (x  = (x + y));
    (y  = (y + 1));
    }

  }
  // post-condition
sassert( (x >= y) );
}
