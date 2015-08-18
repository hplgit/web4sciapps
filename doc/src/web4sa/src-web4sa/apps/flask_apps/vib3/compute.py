from numpy import exp, cos, linspace
import bokeh.plotting as plt
import os, re

def damped_vibrations(t, A, b, w):
    return A*exp(-b*t)*cos(w*t)

def compute(A, b, w, T, resolution=500):
    """Return filename of plot of the damped_vibration function."""
    t = linspace(0, T, resolution+1)
    u = damped_vibrations(t, A, b, w)

    # create a new plot with a title and axis labels
    TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select,lasso_select"
    p = plt.figure(title="simple line example", tools=TOOLS,
                   x_axis_label='t', y_axis_label='y')

    # add a line renderer with legend and line thickness
    p.line(t, u, legend="u(t)", line_width=2)

    from bokeh.resources import CDN
    from bokeh.embed import components
    script, div = components(p)
    head = """
<link rel="stylesheet"
 href="http://cdn.pydata.org/bokeh/release/bokeh-0.9.0.min.css"
 type="text/css" />
<script type="text/javascript"
 src="http://cdn.pydata.org/bokeh/release/bokeh-0.9.0.min.js">
</script>
<script type="text/javascript">
Bokeh.set_log_level("info");
</script>
"""
    return head, script, div

if __name__ == '__main__':
    print compute(A=1, b=0.2, w=6.28, T=4, resolution=500)
