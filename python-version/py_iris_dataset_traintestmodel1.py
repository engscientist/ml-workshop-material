import pandas as pd

datapdfile = pd.read_excel("/Users/Li/Documents/GitHub/ml-workshop-material/Iris.xls") # import file

import numpy as np

datanpfile = np.array(datapdfile)

irissetosa = datanpfile[0:50,0:4]

irisversicolor = datanpfile[50:100,0:4]

irisvirginica = datanpfile[100:150,0:4]

'''
% Come up with random indexes to get testing data
% There are 50 data points for each flower
'''

import random

iris_setosa_testindex = random.randrange(0,50) # Python translation of iris_setosa_testindex = randi(50);
iris_versicolor_testindex = random.randrange(0,50) # Python translation of iris_versicolor_testindex = randi(50);
iris_virginica_testindex = random.randrange(0,50) # Python translation of iris_virginica_testindex = randi(50);

'''
Python translation of
iris_setosa_testindex = randi(50);
iris_versicolor_testindex = randi(50);
iris_virginica_testindex = randi(50);
'''

'''
% Obtain training and testing matrix
% Let the training matrix take all values
% We will deploy the simple model, which only takes into account petal
% length and petal width
'''

iris_setosa_train = irissetosa[:,2:4]
iris_versicolor_train = irisversicolor[:,2:4]
iris_virginica_train = irisvirginica[:,2:4]

'''
Python translation of
iris_setosa_train = iris_setosa(:,[3,4]);
iris_versicolor_train = iris_versicolor(:,[3,4]);
iris_virginica_train = iris_virginica(:,[3,4]);
'''

''' % Remove the rows of test index '''

iris_setosa_train = np.delete(iris_setosa_train, iris_setosa_testindex, 0)
iris_versicolor_train = np.delete(iris_versicolor_train, iris_versicolor_testindex, 0)
iris_virginica_train = np.delete(iris_virginica_train, iris_virginica_testindex, 0)

'''
Python translation of
iris_setosa_train(iris_setosa_testindex,:) = [];
iris_versicolor_train(iris_versicolor_testindex,:) = [];
iris_virginica_train(iris_virginica_testindex,:) = [];
'''

''' % Get test matrices '''

iris_setosa_test = irissetosa[iris_setosa_testindex, 2:4]
iris_versicolor_test = irisversicolor[iris_versicolor_testindex, 2:4]
iris_virginica_test = irisvirginica[iris_virginica_testindex, 2:4]

'''
Python translation of
iris_setosa_test = iris_setosa(iris_setosa_testindex,[3,4]);
iris_versicolor_test = iris_versicolor(iris_versicolor_testindex,[3,4]);
iris_virginica_test = iris_virginica(iris_virginica_testindex,[3,4]);
'''

'''
% Train model
% Here, we are using centroids
'''

iris_setosa_centroid = np.sum(iris_setosa_train, axis = 0) / 49;
iris_versicolor_centroid = np.sum(iris_versicolor_train, axis = 0) / 49;
iris_virginica_centroid = np.sum(iris_virginica_train, axis = 0) / 49;

'''
Python translation of
iris_setosa_centroid = sum(iris_setosa_train) / 49;
iris_versicolor_centroid = sum(iris_versicolor_train) / 49;
iris_virginica_centroid = sum(iris_virginica_train) / 49;
'''

'''
% To differentiate between setosas and non-setosas, we simply use the
% distance between the point with the setosa and versicolor centroids
% To differentiate between the versicolors and the virginicas, we have
% three categories (forbidden, versicolor, virginica). If the testing point
% is not classfied a setosa, and is not in the forbidden region, the point
% is either a versicolor or a virginica (depending on distance to centroid).
% The forbidden region is the region that fulfils two criteria
% First forbidden criteria: This makes it inconclusive of whether the point
% is rightfully a versicolor or is a virginica outlier. The distance
% between the point and the versicolor centroid is greater than that of the
% virginica point closest to the versicolor centroid.
'''

forbidden_d1 = np.min(np.sqrt(np.sum(np.power((iris_virginica_train - iris_versicolor_centroid), 2))))

'''
Python translation of
forbidden_d1 = min(sqrt(sum(((iris_virginica_train - iris_versicolor_centroid).^2),2)));
'''

'''
% (Distance between versicolor centroid and virginica data point closest to
% versicolor centroid)
% The second forbidden criteria is vice versa.
'''

forbidden_d2 = np.min(np.sqrt(np.sum(np.power((iris_versicolor_train - iris_virginica_centroid), 2))))

'''
Python translation of
forbidden_d2 = min(sqrt(sum(((iris_versicolor_train - iris_virginica_centroid).^2),2)));
'''

'''
% Test model
% Initialize matrix indicating test result
'''

test_result = np.zeros(3)

'''
Python translation of
test_result = zeros(1,3);
'''

''' % Test 1 '''

from numpy import linalg as LA

test_result[0] = int(LA.norm(iris_setosa_test - iris_setosa_centroid) < LA.norm(iris_setosa_test - iris_versicolor_centroid))

'''
Python translation of
test_result(1) = norm(iris_setosa_test - iris_setosa_centroid) < norm(iris_setosa_test - iris_versicolor_centroid);
'''

''' % Test 2 '''

if LA.norm(iris_versicolor_test - iris_setosa_centroid) < LA.norm(iris_versicolor_test - iris_versicolor_centroid):
	pass
else:
	if LA.norm(iris_versicolor_test - iris_versicolor_centroid) > forbidden_d1 and LA.norm(iris_versicolor_test - iris_virginica_centroid) > forbidden_d2:
		test_result[1] = -1
	elif LA.norm(iris_versicolor_test - iris_versicolor_centroid) < LA.norm(iris_versicolor_test - iris_virginica_centroid):
		test_result[1] = 1

'''
Python translation of
if norm(iris_versicolor_test - iris_setosa_centroid) < norm(iris_versicolor_test - iris_versicolor_centroid)
else
    if norm(iris_versicolor_test - iris_versicolor_centroid) > forbidden_d1 && norm(iris_versicolor_test - iris_virginica_centroid) > forbidden_d2
        test_result(2) = -1;
    elseif norm(iris_versicolor_test - iris_versicolor_centroid) < norm(iris_versicolor_test - iris_virginica_centroid)
        test_result(2) = 1;
    end
end
'''

''' % Test 3'''

if LA.norm(iris_virginica_test - iris_setosa_centroid) < LA.norm(iris_virginica_test - iris_versicolor_centroid):
	pass
else:
	if LA.norm(iris_virginica_test - iris_versicolor_centroid) > forbidden_d1 and LA.norm(iris_virginica_test - iris_virginica_centroid) > forbidden_d2:
		test_result[2] = -1
	elif LA.norm(iris_virginica_test - iris_virginica_centroid) < LA.norm(iris_virginica_test - iris_versicolor_centroid):
		test_result[2] = 1

'''
Python translation of
if norm(iris_virginica_test - iris_setosa_centroid) < norm(iris_virginica_test - iris_versicolor_centroid)
else
    if norm(iris_virginica_test - iris_versicolor_centroid) > forbidden_d1 && norm(iris_virginica_test - iris_virginica_centroid) > forbidden_d2
        test_result(3) = -1;
    elseif norm(iris_virginica_test - iris_virginica_centroid) < norm(iris_virginica_test - iris_versicolor_centroid)
        test_result(3) = 1;
    end
end

disp(test_result)
'''

print(test_result)

