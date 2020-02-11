import pandas as pd

datapdfile = pd.read_excel("/Users/Li/Documents/GitHub/ml-workshop-material/Iris.xls") # import file

import numpy as np

datanpfile = np.array(datapdfile)

irissetosa = datanpfile[0:50,0:4]

irisversicolor = datanpfile[50:100,0:4]

irisvirginica = datanpfile[100:150,0:4]

# Making petal or sepal plots

import matplotlib.pyplot as plt

# Plot sepal

sepal = False # Edit true or false to determine whether to plot petal or sepal

if sepal:
	xindex = 0
	yindex = 1
	mystr = 'sepal'
else:
	xindex = 2
	yindex = 3
	mystr = 'petal'

irissetosapetalx = list(irissetosa[:,xindex])

irisversicolorpetalx = list(irisversicolor[:,xindex])

irisvirginicapetalx = list(irisvirginica[:,xindex])

irissetosapetaly = list(irissetosa[:,yindex])

irisversicolorpetaly = list(irisversicolor[:,yindex])

irisvirginicapetaly = list(irisvirginica[:,yindex])

plt.plot(irissetosapetalx, irissetosapetaly, 'rx', irisversicolorpetalx, irisversicolorpetaly, 'bx', irisvirginicapetalx, irisvirginicapetaly, 'gx')

myxaxis = mystr + ' length'

myyaxis = mystr + ' width'

mytitle = 'A graph of ' + myxaxis + ' against ' + myyaxis + ' for the Iris dataset'

plt.xlabel(myxaxis)

plt.ylabel(myyaxis)

plt.title(mytitle)

plt.show()

