#funkcja ktora doprowadza do postaci takiej na ktorej bedziemy dzialac
def to_tableau(c, A, b):
    xb = [eq + [x] for eq, x in zip(A, b)]
    z = c + [0]
    return xb + [z]

#szukanie w wspolczynnikach funkcji celu
def can_be_improved(tableau):
    z = tableau[-1] #ostatni  wiersz inaczej C
    print(z)
    return any(x > 0 for x in z[:-1]) #jesli x jest gdzies wiekszy od zera zwroc prawde

c = [1, 1, 0, 0, 0]
A = [
    [-1, 1, 1, 0, 0],
    [ 1, 0, 0, 1, 0],
    [ 0, 1, 0, 0, 1]
]
b = [2, 4, 4]

if __name__ == '__main__':
    t = to_tableau(c,A,b)
    print(t)
    x = can_be_improved(t)
    print(x)

