import plotly.express as Chart
import plotly.graph_objects as Graph

data_frame=Chart.data.iris()
draw_chart=Chart.scatter(data_frame,x='species',y='sepal_length',title='My chart')

print(draw_chart)

draw_chart.show()