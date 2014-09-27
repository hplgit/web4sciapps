
def formula2series2pyfunc(formula, N, x, x0=0):
    """
    Convert a sympy expression in some independent_variable to
    a series representation with N terms and create a Python
    function for evaluating this series representation.
    """
    import sympy as sp
    series = formula.series(x, x0, N).removeO()
    print formula
    print series
    series_pyfunc = sp.lambdify([x], series, modules='numpy')
    formula_pyfunc = sp.lambdify([x], formula, modules='numpy')
    return formula_pyfunc, series_pyfunc

# Enable eval on strings to turn them into sympy expressions
#from sympy import *

def visualize(formula, independent_variable, N, xmin, xmax, ymin, ymax):
    # Turn independent variable into sympy symbol, stored in x
    import sympy as sp
    exec('x = %s = sp.symbols("%s")' %
         (independent_variable, independent_variable))
    # Turn string formula into sympy expression. Need to
    # evaluate formula in the sympy namespace plus the
    # independent variable.
    namespace = sp.__dict__.copy()
    local = {}
    local[independent_variable] = x
    namespace.update(local)
    formula = eval(formula, namespace)
    # Turn x0 into sympy expression
    x0 = eval(x0, sp.__dict__)
    f, s = formula2series2pyfunc(formula, N=N, x=x)
    # Make plot
    import numpy as np
    # Assume xmin, xmax, ymin, ymax are all strings and
    # allow symbols like pi
    xmin = eval(xmin, np.__dict__)
    xmax = eval(xmax, np.__dict__)
    ymin = eval(ymin, np.__dict__)
    ymax = eval(ymax, np.__dict__)
    x = np.linspace(xmin, xmax, 1001)
    import matplotlib.pyplot as plt
    plt.plot(x, f(x), x, s(x))
    plt.xlabel(independent_variable)
    plt.axis([xmin, xmax, ymin, ymax])
    plt.legend(['$%s$' % sp.latex(formula), 'series, N=%d' % N])
    plt.show()

visualize('sin(t)', 't', N=12,
          xmin='0', xmax='2*pi', ymin='-2', ymax='2',
          x0='0')
