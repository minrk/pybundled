#include <stdio.h>
#include <stdarg.h>
#include "bundled.h"

int main (int argc, char const *argv[])
{
    int major, minor, version;
    int f, b, i;
    bundled_version(&major, &minor, &version);
    printf("libbundled version: %d.%d.%d\n", major, minor, version);
    for(i = 0; i < 5; ++i) {
        printf("foo: %d\n", foo());
    }
    for(i = 0; i < 5; ++i) {
        printf("bar: %d\n", bar());
    }
    for(i = 0; i < 5; ++i) {
        foo_bar(&f, &b);
        printf("foo bar: %d,%d\n", f, b);
    }
    return 0;
}