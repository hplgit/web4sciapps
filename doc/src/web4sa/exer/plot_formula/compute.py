def plot_formula(formula, domain, erase):
    """
    formula: string containing function expression of x to be plotted.
    domain: 2-list of min and mix x value in the plot.
    Return PNG plot as a string.
    """
    # Evaluate domain is list and extract xmin and xmax.
    # Evaluate in numpy namespace so that '[0, pi/2]' is a
    # possible domain specification.
    import numpy as np
    input_error = False
    try:
        domain_list = eval(domain, np.__dict__)
    except Exception as e:
        input_error = True
    if not isinstance(domain, list) and len(domain) == 2:
        input_error = True
    if input_error:
        raise ValueError('Specified domain "%s" is not a 2-list' % domain)
    xmin, xmax = domain_list

    # Define x coordinates
    x = np.linspace(xmin, xmax, 10001)
    # Turn formula into numpy expression.
    # Need np.__dict__ namespace and the x defined here
    namespace = np.__dict__.copy()
    namespace.update({'x': x})
    try:
        y = eval(formula, namespace)
    except Exception as e:
        raise ValueError(
            'expression "%s" could not be evaluated:\n%s' %
            formula, str(e))

    # Make plot
    import matplotlib.pyplot as plt
    if erase == 'yes':
        plt.figure()
    plt.plot(x, y)
    plt.xlabel('x')
    from StringIO import StringIO
    figfile = StringIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)  # rewind to beginning of file
    import base64
    figdata_png = base64.b64encode(figfile.buf)
    return figdata_png
