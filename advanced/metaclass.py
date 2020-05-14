""" A metaclass example """
# to check if the derived class has defined a bar method


class BaseMeta(type):
    """ base metaclass """
    def __new__(cls, name, base, body):
        if not 'bar' in body:
            raise TypeError("bad user class")
        return super().__new__(cls, name, base, body)


# metaclass to enforce protocol based model of python
class Base(metaclass=BaseMeta):
    """ base class """

    def foo(self):
        return self.bar()

    def __init_subclass__(self, *a, **kw):
        print('init_subclass', a, kw)
        return super().__init_subclass__(*a, **kw)


# Check for all modules that you intend to use from Base class
assert hasattr(Base, 'foo'), "you broke it"


class Derived(Base):
    """ derived class from base """

    def bar(self):
        return 'bar'
