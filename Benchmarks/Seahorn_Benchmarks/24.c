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
  // pre-conditions
  (i = 1);
  (j = 10);
  // loop body
  while ((j >= i)) {
    {
    (i  = (i + 2));
    (j  = (j - 1));
    }

  }
  // post-condition
sassert( (j == 6) );
}
