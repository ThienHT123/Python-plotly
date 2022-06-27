import plotly.express as Chart 

data_frame=Chart.data.iris()

Draw_Chart=Chart.line(data_frame,x='sepal_length',y='sepal_width')

print(Draw_Chart)

Draw_Chart.show()