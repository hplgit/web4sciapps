
def formula2series2pyfunc(formula, N, x, x0=0):
    """
    Convert a sympy expression formula in some independent
    variable x to a series representation of degree N terms
    and create a Python function for evaluating this series
    representation. Return Python functions for the formula
    and the series expansion, plus a LaTeX formula for the
    series expansion.
    """
    import sympy as sp
    series = formula.series(x, x0, N+1).removeO()
    series_pyfunc = sp.lambdify([x], series, modules='numpy')
    formula_pyfunc = sp.lambdify([x], formula, modules='numpy')
    return formula_pyfunc, series_pyfunc, sp.latex(series)

def visualize_series(
    formula,                  # string: formula
    independent_variable,     # string: name of independent variable
    N,                        # int: degree of polynomial approximation
    xmin, xmax, ymin, ymax,   # strings: extent of axes
    x0='0',                   # string: point of expansion
    ):
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
    f, s, latex = formula2series2pyfunc(formula, N=N, x=x)
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

if __name__ == '__main__':
    visualize_series(
        'sin(t)', 't', N=12,
        xmin='0', xmax='2*pi', ymin='-2', ymax='2',
        x0='0')
