import plotly.express as Chart
import plotly.graph_objects as Graph
import os as OperatorSystem
import operator 
import pyglet as GUI
import pyscreenshot

OperatorSystem.system("color a")

Data_frame=Chart.data.iris()

Draw_Chart=Chart.bar(Data_frame,x='sepal_width',y='sepal_length',color='species',barmode='group',title="My chart")

print(Draw_Chart)

Draw_Chart.show()