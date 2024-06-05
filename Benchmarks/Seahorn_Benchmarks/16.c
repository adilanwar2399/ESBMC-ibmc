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
    int x = 0;
    int m = 0;
    int n = nd();

    while (x < n) {
        if (nd()) {
            m = x;
        }
        x = x + 1;
    }

    if(n > 0) {
       //sassert (m < n);
       sassert (m >= 0);
    }
}
