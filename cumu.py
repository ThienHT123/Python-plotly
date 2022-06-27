import plotly.express as Chart
import plotly.graph_objects as Graph
import os as OperatorSystem
import pyglet as GUI
import operator
import pyscreenshot as Capture

OperatorSystem.system("color a")

data_frame=Chart.data.iris()

draw_chart=Graph.Figure(data=Graph.Histogram(y=data_frame['sepal_width'],cumulative_enabled=True))

print(draw_chart)

draw_chart.show()