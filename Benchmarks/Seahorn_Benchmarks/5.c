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
    int size = nd();
    int y = nd();
    int z = nd();

    while(x < size) {
       x += 1;
       if( z <= y) {
          y = z;
       }
    }

    if(size > 0) {
       sassert (z >= y);
    }
}
