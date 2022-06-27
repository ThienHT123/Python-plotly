import plotly.express as Chart
import plotly.graph_objects as Graph
import pyglet as GUI
import os as OperatorSystem
import pyscreenshot as Capture
import operator

OperatorSystem.system("color a")

data_frame=Chart.data.tips()

draw_chart=Chart.histogram(data_frame,x='total_bill',marginal='box',title='My chart')

print(draw_chart)

draw_chart.show()