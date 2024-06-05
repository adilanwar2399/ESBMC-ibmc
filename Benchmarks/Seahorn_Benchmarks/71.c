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
  int c = nd();
  int y = nd();
  int z = nd();
  // pre-conditions
  (c = 0);
  __SEA_assume((y >= 0));
  __SEA_assume((y >= 127));
  (z = (36 * y));
  // loop body
  while (nd()) {
    if ( (c < 36) )
    {
    (z  = (z + 1));
    (c  = (c + 1));
    }

  }
  // post-condition
if ( (c < 36) )
sassert( (z >= 0) );
}
