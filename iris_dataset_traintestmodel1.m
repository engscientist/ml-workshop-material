% Preparing the files well
clear
load iris_dataset.mat

% Come up with random indexes to get testing data
% There are 50 data points for each flower
iris_setosa_testindex = randi(50);
iris_versicolor_testindex = randi(50);
iris_virginica_testindex = randi(50);

% Obtain training and testing matrix
% Let the training matrix take all values
% We will deploy the simple model, which only takes into account petal
% length and petal width
iris_setosa_train = iris_setosa(:,[3,4]);
iris_versicolor_train = iris_versicolor(:,[3,4]);
iris_virginica_train = iris_virginica(:,[3,4]);
% Remove the rows of test index
iris_setosa_train(iris_setosa_testindex,:) = [];
iris_versicolor_train(iris_versicolor_testindex,:) = [];
iris_virginica_train(iris_virginica_testindex,:) = [];
% Get test matrices
iris_setosa_test = iris_setosa(iris_setosa_testindex,[3,4]);
iris_versicolor_test = iris_versicolor(iris_versicolor_testindex,[3,4]);
iris_virginica_test = iris_virginica(iris_virginica_testindex,[3,4]);

% Train model
% Here, we are using centroids
iris_setosa_centroid = sum(iris_setosa_train) / 49;
iris_versicolor_centroid = sum(iris_versicolor_train) / 49;
iris_virginica_centroid = sum(iris_virginica_train) / 49;
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
forbidden_d1 = min(sqrt(sum(((iris_virginica_train - iris_versicolor_centroid).^2),2)));
% (Distance between versicolor centroid and virginica data point closest to
% versicolor centroid)
% The second forbidden criteria is vice versa.
forbidden_d2 = min(sqrt(sum(((iris_versicolor_train - iris_virginica_centroid).^2),2)));

% Test model
% Initialize matrix indicating test result
% Test results: a test result of 1 indicates that the data point has been
% correctly identified, a test result of 0 indicates that the data point
% has been wrongly identified and a test result of -1 indicates that the
% data point is said to belong to the forbidden region
test_result = zeros(1,3);
% Test 1
test_result(1) = norm(iris_setosa_test - iris_setosa_centroid) < norm(iris_setosa_test - iris_versicolor_centroid);
% Test 2
if norm(iris_versicolor_test - iris_setosa_centroid) < norm(iris_versicolor_test - iris_versicolor_centroid)
else
    if norm(iris_versicolor_test - iris_versicolor_centroid) > forbidden_d1 && norm(iris_versicolor_test - iris_virginica_centroid) > forbidden_d2
        test_result(2) = -1;
    elseif norm(iris_versicolor_test - iris_versicolor_centroid) < norm(iris_versicolor_test - iris_virginica_centroid)
        test_result(2) = 1;
    end
end
% Test 3
if norm(iris_virginica_test - iris_setosa_centroid) < norm(iris_virginica_test - iris_versicolor_centroid)
else
    if norm(iris_virginica_test - iris_versicolor_centroid) > forbidden_d1 && norm(iris_virginica_test - iris_virginica_centroid) > forbidden_d2
        test_result(3) = -1;
    elseif norm(iris_virginica_test - iris_virginica_centroid) < norm(iris_virginica_test - iris_versicolor_centroid)
        test_result(3) = 1;
    end
end

disp(test_result)