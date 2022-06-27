import plotly.express as Chart 
import plotly.graph_objects as Graph
import os as OperatorSystem
import operator
import pyglet as GUI
import pyscreenshot as Capture

OperatorSystem.system("color a")

data_frame=Chart.data.tips()

Draw_Chart=Chart.bar(data_frame,x='total_bill',y='day',barmode='group',color='sex',title='My chart')

print(Draw_Chart)

Draw_Chart.show()