import plotly.express as Chart

df=Chart.data.iris()

Draw_Chart=Chart.line(df,x="species",y="petal_width")
#* NOTE petal width là trục y, còn species là trục x

print(Draw_Chart)

Draw_Chart.show()