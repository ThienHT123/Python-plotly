import plotly.express as Chart
import pyglet as GUI
import plotly.graph_objects as Graph
import os as OperatorSystem
import operator
import pyscreenshot as Capture

OperatorSystem.system("color a")

data_frame=Chart.data.tips()

Draw_Chart=Chart.histogram(data_frame,x='total_bill',color='smoker')

print(Draw_Chart)

Draw_Chart.show()