# test_all.py

# Running py.test -s -v will run all tests in all test*.py files in all subdirectories
# just test.py isnt picked up by py.test

def add(a, b):
    return a + b

def test_add():
    expected = 1 + 1
    computed = add(1, 1)
    assert computed == expected, f'1+1={computed: .15g}' 

def trapezoidal(f, a, b, n):
    h = float(b-a)/n
    result = 0.5*f(a) + 0.5*f(b)
    for i in range(1, n):
        result += f(a + i*h)
    result *= h
    return result

def test_trapezoidal_one_exact_result():
    """Compare one hand-computed result."""
    from math import exp
    v = lambda t: 3*(t**2)*exp(t**3)
    n=2
    computed = trapezoidal(v, 0, 1, n) 
    expected = 2.463642041244344
    error = abs(expected - computed)
    tol = 1E-14
    success = error < tol
    msg = f'error={error} > tol={tol}' 
    assert success, msg

def test_trapezoidal_linear():
    """Check that linear functions are integrated exactly."""
    f = lambda x: 6*x - 4
    F = lambda x: 3*x**2 - 4*x  # Anti-derivative
    a = 1.2
    b = 4.4
    expected = F(b) - F(a)
    tol = 1E-14
    for n in 2, 20, 21:
        computed = trapezoidal(f, a, b, n)
        error = abs(expected - computed)
        success = error < tol
        msg = f'n={n}, err={error}'
        assert success, msg

test_add()
test_trapezoidal_one_exact_result()
test_trapezoidal_linear()
