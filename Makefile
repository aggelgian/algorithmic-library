.PHONY: default all clean distclean test

PYTHON=python

test:
	@(cd $(PYTHON) && ./test.sh)
