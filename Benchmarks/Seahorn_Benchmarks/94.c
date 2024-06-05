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
  int k = nd();
  int n = nd();
  // pre-conditions
  __SEA_assume((k >= 0));
  __SEA_assume((n >= 0));
  (i = 0);
  (j = 0);
  // loop body
  while ((i <= n)) {
    {
    (i  = (i + 1));
    (j  = (j + i));
    }

  }
  // post-condition
sassert( ((i + (j + k)) > (2 * n)) );
}
