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
  __SEA_assume((x >= 0));
  __SEA_assume((x <= 2));
  __SEA_assume((y <= 2));
  __SEA_assume((y >= 0));
  // loop body
  while (nd()) {
    {
    (x  = (x + 2));
    (y  = (y + 2));
    }

  }
  // post-condition
if ( (y == 0) )
sassert( (x != 4) );

}
