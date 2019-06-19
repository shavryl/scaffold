from array import array
import reprlib
import math


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._componenets = array(self.typecode, components)

    def __iter__(self):
        return iter(self._componenets)

    def __repr__(self):
        components = reprlib.repr(self._componenets)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._componenets))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._componenets)

    def __getitem__(self, index):
        return self._componenets[index]

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
