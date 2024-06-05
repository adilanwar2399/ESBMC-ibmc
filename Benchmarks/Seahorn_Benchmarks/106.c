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
    int a = nd();
    int m = nd();
    int j = nd();
    int k = nd();

    __SEA_assume(a <= m);
    __SEA_assume(j < 1);
    k = 0;

    while ( k < 1) {
        if(m < a) {
            m = a;
        }
        k = k + 1;
    }

    sassert( a >= m);
}
