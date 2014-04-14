# pybundle

An example Python package for bundling a C library dependency as a Python Extension
if it is not found. This is a Cython project, but the basics apply to pure C extensions just the same.


- `libbundled` is a simple C library that doesn't do much.
- `pybundled` is a simple Cython wrapper exposing `libbundled` to Python.


You can install libbundled with:

```bash
cd libbundled
make && make install
```

`make uninstall` will undo the install.

If libbundled is installed, pybundle will link against it.
If, however, libbundled cannot be found,
then pybundle will compile libbundled as a Python extension.

This code is based on lessons learned in [pyzmq](https://github.com/zeromq/pyzmq),
but is much simpler than the shenanigans I get up to over there.

## Unhandled cases

### bundle is the only extension

One possibly common case this does not cover is a project that doesn't already have any extensions,
but still wants to ship a dependency as an Extension if it isn't found.
In this case, a dummy Extension may want to be added,
lest distutils decide to skip the `build_ext` process entirely.

### specifying the location of libbundled

Often you will want to configure the install prefix of the dependency.
This doesn't handle that particular case without specifying several options to build_ext.

## License

pybundle is in the Public Domain. Do whatever you want with it,
but some credit would be nice.
