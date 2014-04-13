#include "foo.h"
#include "bar.h"

void bundled_version(int *major, int *minor, int *patch) {
    *major = 1;
    *minor = 2;
    *patch = 3;
};

void foo_bar(int *f, int *b) {
    *f = foo();
    *b = bar();
};