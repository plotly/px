"""
A simple scatter plot
=====================

bla bla bla
"""
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import iplot, plot

# Create random data with numpy
import numpy as np

N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers'
)

data = [trace]

# Plot and embed in ipython notebook!
plot(data, filename='../auto_examples/simple_scatter.html')

####################################
# .. raw:: html
#     :file: simple_scatter.html
