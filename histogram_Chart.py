import plotly.express as Chart
import plotly.graph_objects as Graph
import os as OperatorSystem
import pyglet as GUI
import pyscreenshot as Capture

OperatorSystem.system("color a")

data_frame=Chart.data.iris()

Draw_Chart=Chart.histogram(data_frame,x='sepal_length',y='petal_width')

print(Draw_Chart)

Draw_Chart.show()