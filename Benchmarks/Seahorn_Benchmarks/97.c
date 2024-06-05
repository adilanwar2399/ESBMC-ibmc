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
  int x = nd();
  int y = nd();
  // pre-conditions
  (j = 0);
  (i = 0);
  (y = 2);
  // loop body
  while ((i <= x)) {
    {
    (i  = (i + 1));
    (j  = (j + y));
    }

  }
  // post-condition
if ( (y == 1) )
sassert( (i == j) );

}
