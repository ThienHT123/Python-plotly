import plotly.express as Chart

data_frame=Chart.data.tips()

Draw_Chart=Chart.line(data_frame,x='day',y='total_bill',color='sex')

print(Draw_Chart)

Draw_Chart.show()