import plotly.express as Chart
import plotly.graph_objects as Graph
import os as OperatorSystem
import pyglet as GUI
import operator
import pyscreenshot as Capture

OperatorSystem.system("color a")

data_frame=Chart.data.iris()

Draw_Chart=Chart.bar(data_frame,x='sepal_width',y='sepal_length',color='species',hover_data=['petal_width'],barmode='stack',title='My chart')

print(Draw_Chart)

Draw_Chart.show()