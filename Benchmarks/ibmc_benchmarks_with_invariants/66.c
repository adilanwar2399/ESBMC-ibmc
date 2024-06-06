
extern void abort(void);
extern void __assert_fail(const char *, const char *, unsigned int, const char *) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__noreturn__));
void reach_error() { __assert_fail("0", "vnew2.c", 3, "reach_error"); }
extern void abort(void);
void assume_abort_if_not(int cond) {
  if(!cond) {abort();}
}
void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: {reach_error();abort();}
  }
  return;
}
int __VERIFIER_nondet_int();

int abs(int x){
  return x < 0 ? -x : x;
}

int main() {
    int x = 1;
    int y = __VERIFIER_nondet_int();

    __invariant(x <= 100 || (y >= 0 && y < 100));
    while (x <= 100) {
        y = 100 - x;
        x = x +1;
    }

    //__VERIFIER_assert (y >= 0);
    __VERIFIER_assert (y < 100);
}
