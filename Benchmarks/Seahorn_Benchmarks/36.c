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
  // pre-conditions
  (c = 0);
  // loop body
  while (nd()) {
    {
      if ( nd() ) {
        if ( (c != 40) )
        {
        (c  = (c + 1));
        }
      } else {
        if ( (c == 40) )
        {
        (c  = 1);
        }
      }

    }

  }
  // post-condition
if ( (c != 40) )
sassert( (c <= 40) );
}
