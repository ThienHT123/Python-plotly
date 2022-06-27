import plotly.express as Chart
import plotly.graph_objects as Graph
import pyglet as GUI 
import os as OperatorSystem
import pyscreenshot as Capture
import operator

OperatorSystem.system("color a")

data_frame=Chart.data.iris()

draw_chart=Graph.Figure(data=[Graph.Histogram(x=data_frame['sepal_width'],cumulative_enabled=True)])

print(draw_chart)

draw_chart.show()