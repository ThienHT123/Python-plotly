import plotly.express as Chart
import plotly.graph_objects as Graph
import os as OperatorSystem
import pyglet as GUI
import operator
import pyscreenshot

OperatorSystem.system("color a")

data_frame=Chart.data.tips()

Draw_Chart=Chart.histogram(data_frame,x='total_bill',histnorm='percent',nbins=21)

print(Draw_Chart)

Draw_Chart.show()