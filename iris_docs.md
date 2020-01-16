# Iris dataset

The Iris dataset is a common dataset used when people are first introduced to machine learning.

Here, we are given four features: sepal length, sepal width, petal length and petal width. These features are used to help us distinguish between three types of irises: iris-setosa, iris-versicolor and iris-virginica.

The task here is to investigate whether there is any relationship between the iris-setosa, iris-versicolor and iris-virginica. If a relationship exists, we would be able to use these relationships to predict the type of irises using the features of a particular iris.

Credits for iris dataset: Saed Sayad

The iris dataset has been converted to MATLAB matrices `A`, `B` and `C`. Each matrix has 50 rows (representing the 50 data points) and 4 columns (representing the 4 features).

Matrix | Data
------------ | -------------
`A` | iris-setosa
`B` | iris-versicolor
`C` | iris-virginica

## Approach

Here, the iris features can be split into two groups: sepal data and petal data. In each feature group, there are two pieces of data we are interested in, and that is the length and the width of the sepal / petal.

### Plot of the length and width of the sepals of the irises

![Plot of the length and width of the iris sepals](https://raw.githubusercontent.com/engscientist/ml-workshop-material/master/iris_sepal_plot.jpg)

### Plot of the length and width of the petals of the irises

![Plot of the length and width of the iris petals](https://raw.githubusercontent.com/engscientist/ml-workshop-material/master/iris_petal_plot.jpg)

### Insights

From the plots above, it seems that clearly the petals of the iris-setosa is smaller than that of the iris-versicolor and the iris-virginica. This can be used to determine whether a given petal is from the iris-setosa or not.


