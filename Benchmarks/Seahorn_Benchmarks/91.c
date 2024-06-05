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
int main(){

    int x = 0;
    int y = 0;

    while(y >= 0){
        y = y + x;
    }

    sassert( y>= 0);
}
