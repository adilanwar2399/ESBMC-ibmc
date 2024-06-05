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
    int d1 = 1;
    int d2 = 1;
    int d3 = 1;
    int x1 = 1;
    int x2 = nd();
    int x3 = nd();

    while( x1 > 0) {
        if(x2 > 0) {
            if(x3 > 0) {
                x1 = x1 - d1;
                x2 = x2 - d2;
                x3 = x3 - d3;
            }
        }
    }

    sassert (x2 >= 0);
    //sassert (x3 >= 0);
}
