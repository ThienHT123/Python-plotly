import plotly.express as Chart
import plotly.graph_objects as Graph
import pyglet as GUI
import os as OperatorSystem
import operator 
import pyscreenshot as Capture

OperatorSystem.system("color a")

data_frame=Chart.data.tips()

Draw_Chart=Chart.histogram(data_frame,x='total_bill',marginal='rug',color='sex',title='My chart')

print(Draw_Chart)

Draw_Chart.show()