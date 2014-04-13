cimport libbundled

def foo():
    return libbundled.foo()

def bar():
    return libbundled.bar()

def bundled_version():
    cdef int major, minor, patch
    libbundled.bundled_version(&major, &minor, &patch)
    return major, minor, patch

def foo_bar():
    cdef int f, b
    libbundled.foo_bar(&f, &b)
    return f, b
