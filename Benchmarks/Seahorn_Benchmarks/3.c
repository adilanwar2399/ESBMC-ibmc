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
    int y = nd();
    int z = nd();

    while(x < 5) {
       x += 1;
       if( z <= y) {
          y = z;
       }
    }

    sassert (z >= y);
}
