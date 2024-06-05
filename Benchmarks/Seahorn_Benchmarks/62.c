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
  int n = nd();
  int v1 = nd();
  int v2 = nd();
  int v3 = nd();
  // pre-conditions
  (c = 0);
  __SEA_assume((n > 0));
  // loop body
  while (nd()) {
    {
      if ( nd() ) {
        if ( (c != n) )
        {
        (c  = (c + 1));
        }
      } else {
        if ( (c == n) )
        {
        (c  = 1);
        }
      }

    }

  }
  // post-condition
if ( (n > -1) )
sassert( (c != n) );

}
