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
int main()
{
    int z1 = nd();
    int z2 = nd();
    int z3 = nd();
    int x = 1;
    int m = 1;
    int n = nd();

    while (x < n) {
        if (nd()) {
            m = x;
        }
        x = x + 1;
    }

    if(n > 1) {
       sassert (m < n);
       //sassert (m >= 1);
    }
}
