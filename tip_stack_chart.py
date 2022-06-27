import plotly.express as Chart
import plotly.graph_objects as Graph
import os as OperatorSystem
import operator
import pyscreenshot as Capture

OperatorSystem.system("color a")

data_frame=Chart.data.tips()

Draw_chart=Chart.bar(data_frame,x='total_bill',y='day',color='sex',barmode='stack',title='My chart')

print(Draw_chart)

Draw_chart.show()