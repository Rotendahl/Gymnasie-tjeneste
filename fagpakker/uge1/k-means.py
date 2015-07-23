import numpy as np
import sqlite3 as lite
from datetime import datetime
import matplotlib.pyplot as plt


n


""" This function takes the attributes and a table
        both in the form  of a string, and returns an array
        containg tuples with the rows from the database
"""
def selectFrom(attributes, table):
        connection = lite.connect("DataminingAssignment2014.db")
        cursor = connection.cursor()
        with connection:
                cursor.execute("SELECT " + attributes + " FROM " + table)
                data = cursor.fetchall()
                return data

""" This sql statement returns all x values for galaxies """
filterGalaxy = "((SELECT id FROM Objects_Train_Y WHERE y=0) NATURAL JOIN Objects_Train_X)"

""" We transpose X such that we have x = (val1,val2,val3,val4,val5, ..., valN), where val
	is a colum vector.
"""
x = np.matrix(selectFrom(" x0, x1, x2, x3, x4, x5, x6, x7, x8, x9 ", filterGalaxy)).T

""" This method taxes a matrix consisting of colum vectors and returns the average colum """
def calMean(data):
 	sum = data[:,[0]]
 	size = len(data.T)
 	for i in range(1, size):
 		sum += data[:,[i]]
 	return sum/size


""" Takes an array an a mean and returns the covariance matrix
"""
def calCovariance(data, mean):
 	size = len(data.T)
	covarianceMatrix = (data[:,[0]] - mean) * (data[:,[0]] - mean).T
	for i in range(1, size):
		covarianceMatrix  += (data[:,[i]] - mean) * (data[:,[i]] - mean).T
	return covarianceMatrix /size



""" Takes a matrix and returns an array containg [eigenValues,matrix(eigenVectores)].
	Both are sorted after dercresing eigenvalue
"""
def EigenSort(covariance):
	eigen = np.linalg.eig(covariance)
	val   = eigen[0]
	vectores  = eigen[-1].A

	ordered = val.argsort()
	sortedVal = []
	sortedVec = []
	for i in range(0, len(ordered)):
		sortedVal.append(val[ordered[i]])
		sortedVec.append(vectores[ordered[i]])
	return [sortedVal[::-1], np.matrix(sortedVec[::-1])]

""" This method takes a matrix and the number of dimsions the output should have """
def reduceDim(matrix, m):
	vals = matrix.A
	newVals = []
	for i in range(0,len(vals)):
			newVals.append(vals[i][0:m])
	return np.matrix(newVals)

""" This method takes a matrix and reduces it to it's m princibal compontents """
def model(matrix, m):
	 mean = calMean(matrix)
	 covariance = calCovariance(matrix, mean)
	 eigen = EigenSort(covariance)
	 eigenValues = eigen[0]
	 eigenVectors = eigen[1]
	 u = reduceDim(eigenVectors, m)
	 newMatrix = []
	 size = len(matrix.T)
 	 for i in range(0, size):
 	 	val = (u.T * (x[:,[i]] - mean)).A1.tolist()
 	 	newMatrix.append(val)
 	 return np.matrix(newMatrix)


""" Plots the eigenspectrum """
def eigenSpectrum ():
	eigen = EigenSort(calCovariance(x, calMean(x)))
	eigenValues = eigen[0]
	eigenNr = range(0,len(eigenValues))
	plt.plot(eigenNr, eigenValues)
	plt.ylabel('Eigen values')
	plt.xlabel('Index eigen vector')
	plt.axis([-1, 10, -1, 25])
	plt.show()

""" Uncomment for plot """
#eigenSpectrum()


""" Calculates how many compontents are nesseary to show p '%' of the variance"""
def quotient(eigenValues, p):
	quotient = 0.0
	m = 1
	mSum = 0.0
	nSum = 0.0
	while quotient < p and m < len(eigenValues) :
		mSum = sum (eigenValues[0:m])
		nSum = sum (eigenValues)
		quotient = mSum/nSum * 100
		m += 1
	if(m >= len(eigenValues)):
		m = 0
	return m -1

eigen = EigenSort(calCovariance(x, calMean(x)))
eigenValues = eigen[0]
print ("To explain 90%  of the variance we need the first", quotient(eigenValues, 90),
 "princibal compontents")


""" Plots the a scatter plot of the first two princibal compontents """
def scatterPlot ():
	data = model(x,2).tolist()
	x1 = []
	x2 = []
	for i in range(0, len(data)):
		x1.append(data[i][0])
		x2.append(data[i][1])
	plt.plot(x1, x2, "bo")
	plt.ylabel('x2')
	plt.xlabel('x1')
	plt.axis([-17, 10, -8, 8])
	plt.show()

""" Uncomment for plot """
#scatterPlot()




""" This function take a column of x data, and returns
	the sqauard Euclidean distanse as a float
"""

def distance (xi,xj):
	dist = 0.0
	xi = xi.A1.tolist()
	xj = xj.A1.tolist()
	for i in range(0, len(xi)):
		dist += (xi[i] - xj[i]) ** 2
	return dist



""" Takes two centers places x values and returns two better centers
"""
def clusterMean(center1, center2):
	cluster1 = []
	cluster2 = []

	for i in range (0, len(x)):
		distC1 = distance(x[:,[i]], center1)
		distC2 = distance(x[:,[i]], center2)
		if(distC2 < distC1):
			cluster2.append((x[:,[i]]).A1.tolist())
		else:
			cluster1.append((x[:,[i]]).A1.tolist())
	return [calMean(np.matrix(cluster1).T), calMean(np.matrix(cluster2).T)]



""" Continues to move the centers of the clusteres until convergance"""
def relocate():
	oldCenter1 = x[:,[100]]
	oldCenter2 = x[:,[300]]
	newCenter1 = x[:,[200]]
	newCenter2 = x[:,[1000]]
	convergance = False
	while(not convergance):
		new = clusterMean(oldCenter1,oldCenter2)
		newCenter1 = new[0]
		newCenter2 = new[1]
		if(distance(oldCenter1, newCenter1) < 0.2 and distance(oldCenter2, newCenter2) < 0.2 ):
			convergance = True
		else :
			oldCenter1 = newCenter1
			oldCenter2 = newCenter2
	return [oldCenter1,oldCenter2]


""" Given to centers returns the points clustered in them """
def clusters(center1, center2):
	cluster1 = []
	cluster2 = []

	for i in range (0, len(x)):
		distC1 = distance(x[:,[i]], center1)
		distC2 = distance(x[:,[i]], center2)
		if(distC2 < distC1):
			cluster2.append((x[:,[i]]).A1.tolist())
		else:
			cluster1.append((x[:,[i]]).A1.tolist())
	return [cluster1,cluster2]


""" Plots the a scatter plot of the first two princibal compontents """
def scatterPlotWithCenter ():
	center = relocate()
	center1 = center[0]
	center2 = center[1]
	model1 = model(center1,2).A1.tolist()
	c1x = model1[0]
	c1y = model1[1]
	model2 = model(center2,2).A1.tolist()
	c2x = model2[0]
	c2y = model2[1]
	data = model(x,2).tolist()
	x1 = []
	x2 = []
	print "The center for cluster one is ", c1x, c1y,
	print "The center for cluster two is ", c2x, c2y,
	for i in range(0, len(data)):
		x1.append(data[i][0])
		x2.append(data[i][1])
	plt.plot(x1, x2, "bo", c1x, c1y, "ro", c2x, c2y, "ro")
	plt.ylabel('x2')
	plt.xlabel('x1')
	plt.axis([-17, 10, -8, 8])
	plt.show()

""" Uncomment for plot """
#scatterPlotWithCenter()
