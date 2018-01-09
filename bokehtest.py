import pandas
from bokeh.plotting import figure, output_file, show

# pandas
df = pandas.read_csv('crdl_data.log')
# read in name, x , y
# print df.x, df,y

# bokeh
plot =  figure()
plot.scatter(x=df.timestamp, y=df.sensor)

output_file('test.html')
show(plot)