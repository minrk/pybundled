cdef extern from "bundled.h":
    int foo()
    int bar()
    void foo_bar(int *f, int *b)
    void bundled_version(int *major, int *minor, int *patch)

