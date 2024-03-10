import numpy as np

def midpoint_vector(f, a, b, n):
    h = (b-a)/n
    x = np.linspace(a+h/2.0, b-h/2.0, n)
    return h*f(x).sum()

def test_midpoint_vector():
    a = 9.81
    x_t = lambda t: 0.5 * a * t**2
    f = lambda t: a*t
    computed = midpoint_vector(f, 0, 100, 10000)
    expected = x_t(100)
    error = abs(expected - computed)
    tol = 1E-14
    success = error < tol
    msg = f'error={error} > tol={tol}' 
    assert success, msg

test_midpoint_vector()