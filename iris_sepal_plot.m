load('iris_dataset.mat')
close all
myxlabel = 'petal length';
myylabel = 'petal width';
mytitle = ['A graph of ', myxlabel, ' against ', myylabel, ' for the Iris dataset'];
xindex = 3;
yindex = 4;
plot(iris_setosa(:,xindex),iris_setosa(:,yindex),'rx')
hold
plot(iris_versicolor(:,xindex),iris_versicolor(:,yindex),'bx')
plot(iris_virginica(:,xindex),iris_virginica(:,yindex),'mx')
xlabel(myxlabel)
ylabel(myylabel)
legend('iris-setosa','iris-versicolor','iris-virginica')
title(mytitle)