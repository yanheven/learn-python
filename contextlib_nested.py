__author__ = 'evan'
from contextlib import contextmanager
from contextlib import nested

@contextmanager
def tag(name):
    print "<%s>" % name
    yield
    print "</%s>" % name


@contextmanager
def param(name):
    print "{{"
    yield
    print "}}"


with nested(tag("h1"), tag("p")):
    print "t1"


