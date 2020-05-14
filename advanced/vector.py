class Vector:

    'Base class for 2-D vectors'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Vector(' + str(self.x) + ',' + str(self.y) + ')'

    def __add__(self, v):
        'returns a new vector which is a sum of two vectors'
        return Vector(self.x + v.x, self.y + v.y)

    def __eq__(self, v):
        return (self.x == v.x) and (self.y == v.y)

    def __repr__(self):
        return 'Vector({},{})'.format(self.x, self.y)


v1 = Vector(5, -10)
v2 = Vector(2, 2)
v3 = v1 + v2
print(v3)
