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
  int v1 = nd();
  int v2 = nd();
  int v3 = nd();
  int x = nd();
  // pre-conditions
  (x = n);
  // loop body
  while ((x > 0)) {
    {
    (x  = (x - 1));
    }

  }
  // post-condition
if ( (x != 0) )
sassert( (n < 0) );

}
