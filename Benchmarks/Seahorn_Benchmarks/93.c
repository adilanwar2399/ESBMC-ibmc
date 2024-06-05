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
  int n = nd();
  int x = nd();
  int y = nd();
  // pre-conditions
  __SEA_assume((n >= 0));
  (i = 0);
  (x = 0);
  (y = 0);
  // loop body
  while ((i < n)) {
    {
    (i  = (i + 1));
      if ( nd() ) {
        {
        (x  = (x + 1));
        (y  = (y + 2));
        }
      } else {
        {
        (x  = (x + 2));
        (y  = (y + 1));
        }
      }

    }

  }
  // post-condition
sassert( ((3 * n) == (x + y)) );
}
