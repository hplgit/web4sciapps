from numpy import exp, cos, linspace
import bokeh.plotting as plt
import os, re

def damped_vibrations(t, A, b, w):
    return A*exp(-b*t)*cos(w*t)

def compute(A, b, w, T, resolution=500):
    """Return filename of plot of the damped_vibration function."""
    t = linspace(0, T, resolution+1)
    u = damped_vibrations(t, A, b, w)

    # output to static HTML file
    outname = 'tmp.html'
    plt.output_file(outname, title="Damped vibrations")

    # create a new plot with a title and axis labels
    TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select,lasso_select"
    p = plt.figure(title="simple line example", tools=TOOLS,
                   x_axis_label='t', y_axis_label='y')

    # add a line renderer with legend and line thickness
    p.line(t, u, legend="u(t)", line_width=2)

    # show the results
    #plt.show(p)
    plt.save(p)
    with  open(outname, 'r') as f:
        text = f.read()
    # Grab head and body
    m = re.search('<head>(.+)</head>.+<body>(.+)</body>', text,
                  flags=re.DOTALL)
    if m:
        head = m.group(1)
        body = m.group(2)
    else:
        raise ValueError('Could not parse the bokeh output in tmp.html')
    #os.remove(outname)
    return head, body

if __name__ == '__main__':
    print compute(A=1, b=0.2, w=6.28, T=4, resolution=500)
