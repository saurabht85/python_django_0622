import math
import pdb

class Quad:

    def __init__(self, x, y, z):
        self.a = x
        self.b = y
        self.c = z

    def solve(self):
        d = (self.b ** 2) - (4 * self.a * self.c)
        if d > 0:
            disc = math.sqrt(d)
            root1 = (-self.b + disc)/(2*self.a)
            root2 = (-self.b - disc) /(2*self.a)
            return root1, root2
        elif d == 0:
            return -self.b / 2 * self.a
        else:
            return "This equation has no roots"

print(__name__)
if __name__ == '__main__':
    while True:
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        c = int(input("Enter the value of c: "))
        if a == -1:
            print("Exiting")
            break
        #pdb.set_trace()
        #breakpoint()
        solver = Quad(a, b, c)
        roots = solver.solve()
        print(roots)

