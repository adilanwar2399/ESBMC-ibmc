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
  int n = nd();
  int x = nd();
  int y = nd();
  // pre-conditions
  __SEA_assume((n >= 0));
  (x = n);
  (y = 0);
  // loop body
  while ((x > 0)) {
    {
    (y  = (y + 1));
    (x  = (x - 1));
    }

  }
  // post-condition
sassert( (y == n) );
}
