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
    int x = 1;
    int y = nd();

    while (x <= 100) {
        y = 100 - x;
        x = x +1;
    }

    sassert (y >= 0);
    //sassert (y < 100);
}
