ifndef CC
  CC=gcc
endif

ifndef PREFIX
  PREFIX = /usr/local
endif

ifeq ($(shell uname), Darwin)
  LIBEXT = dylib
  SHARED = -dynamiclib
else
  LIBEXT = so
  SHARED = -shared
endif

LINK = $(CC) $(SHARED)

LIBRARY = libbundled.$(LIBEXT)

OBJECTS = foo.o bar.o bundled.o

$(LIBRARY): $(OBJECTS)
	$(CC) $(SHARED) -o $(LIBRARY) $(OBJECTS)

.c.o:
	$(CC) -c $*.c -o $*.o

test: test.c $(LIBRARY)
	$(CC) -o test test.c -L. -lbundled

check : test
	@echo $(PREFIX)
	./test

all: $(LIBRARY)

clean:
	@rm -f *.o *~ $(LIBRARY)

install: $(LIBRARY)
	cp $(LIBRARY) $(PREFIX)/lib/$(LIBRARY)
	cp bundled.h $(PREFIX)/include/bundled.h

uninstall:
	@rm -f $(PREFIX)/lib/$(LIBRARY)
	@rm -f $(PREFIX)/include/bundled.h
