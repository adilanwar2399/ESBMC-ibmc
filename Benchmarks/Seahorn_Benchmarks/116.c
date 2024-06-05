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
  int sn = nd();
  int v1 = nd();
  int v2 = nd();
  int v3 = nd();
  int x = nd();
  // pre-conditions
  (sn = 0);
  (x = 0);
  // loop body
  while (nd()) {
    {
    (x  = (x + 1));
    (sn  = (sn + 1));
    }

  }
  // post-condition
if ( (sn != x) )
sassert( (sn == -1) );

}
