from unittest import TestCase
from Module5.debugging import Quad
# -0.10102051443364424, -9.898979485566356

class TestQuad(TestCase):
    def setUp(self):
        self.solver = Quad(1, 10, 1)

    def test_solve(self):
        root1, root2 = self.solver.solve()
        self.assertEqual(root1, -0.10102051443364424)
        self.assertEqual(root2, -9.898979485566356)

