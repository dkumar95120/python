# Advanced Python
# top-level function or top-level syntax
# x + y -> __add__
# init(x) -> __init__
# repr(x) -> __repr__
#  x()    -> __call__


class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        coeffs = list(self.coeffs) if len(self.coeffs) > len(
            other.coeffs) else list(other.coeffs)
        for i in range(min(len(self.coeffs), len(other.coeffs))):
            coeffs[-(i+1)] = self.coeffs[-(i+1)] + other.coeffs[-(i+1)]

        return Polynomial(*coeffs)

    def __len__(self):
        return len(self.coeffs)

    def __call__(self):
        pass

    def __str__(self):
        order = len(self.coeffs) - 1
        s = ''
        for i, c in enumerate(self.coeffs):
            str_c = str(c) if c > 1 else ''
            if order - i > 1:
                s += str_c + 'x' + str(order-i) + ' + '
            elif order - i == 1:
                s += str_c + 'x' + ' + '
            elif order - i == 0:
                s += str(c)
        return s


def main():
    p1 = Polynomial(1, 2, 3)  # x2 + 2x + 3
    p2 = Polynomial(3, 4, 1)  # 3x2 + 4x + 3
    print(p1)
    print(p2)


if __name__ == '__main__':
    main()
