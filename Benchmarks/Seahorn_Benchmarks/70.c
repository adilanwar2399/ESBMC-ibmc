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
    int n = nd();
    int v1 = nd();
    int v2 = nd();
    int v3 = nd();
    int x = 1;
    int y = nd();

    while (x <= n) {
        y = n - x;
        x = x +1;
    }

    if (n > 0) {
      //sassert (y >= 0);
      sassert (y < n);
    }
}
