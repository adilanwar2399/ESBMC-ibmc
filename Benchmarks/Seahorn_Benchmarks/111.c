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
  int sn = nd();
  // pre-conditions
  (sn = 0);
  (i = 1);
  // loop body
  while ((i <= n)) {
    {
    (i  = (i + 1));
    (sn  = (sn + 1));
    }

  }
  // post-condition
if ( (sn != 0) )
sassert( (sn == n) );

}
