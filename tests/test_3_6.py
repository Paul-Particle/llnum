
import sympy
import numpy as np

def midpoint(f, a, b, n):
    h = (b-a)/n
    x = np.linspace(a+h/2.0, b-h/2.0, n)
    return h*f(x).sum()

def midpoint_double(f, a, b, c, d, n_x, n_y):
    def g(x):
        return midpoint(lambda y: f(x,y), c, d, n_y)
    return midpoint(g, a, b, n_x)

def test_midpoint_double():
    """Test that a linear function is integrated exactly."""
    def f(x, y):
        return 2*x + y

    a=0; b=2; c=2; d=3
    x, y = sympy.symbols('x y')
    I_expected = sympy.integrate(f(x, y), (x, a, b), (y, c, d)) 
    # Test three cases: nx < ny, nx = ny, nx > ny
    for nx, ny in (3, 5), (4, 4), (5, 3):
        I_computed = midpoint_double(f, a, b, c, d, nx, ny)
        tol = 1E-14
        print(I_expected, I_computed)
        assert abs(I_computed - I_expected) < tol