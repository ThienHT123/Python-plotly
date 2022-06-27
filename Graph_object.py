import numpy as np
import plotly.graph_objects as Graph

x=[0,1,2,3,4,5,6,7,8,9]
y=[1,3,4,5,6]
Chart=Graph.Figure(data=Graph.Scatter(x=x,y=y))

print(Chart)

Chart.show()

