function [J, grad] = costFunction(theta, X, y, lambda)

%-----------------------------------------------------------------------------
%Introduction
%The cost function is used to computer the cost of the algorithm

%Input:
%1. theta: the logistic regression parameters, which has a dimension of
%n*1, n is the number of the features
%2. X: the input data, which has a dimension of m*n, n is the number of the
%features and m is the number of the training set
%3. y: the actual value of output, in this project, y can take two values,
%0 and 1. 0 means the person is a not a specialist in the specific disease
%and 1 means the person is the specialist in that disease. It has a
%dimension of m*1, m is the number of the training set
%4. lambda: the regularization parameter for preventing overfitting

%Output:
%1. J: the cost of the algorithm
%2. grad: the gradient of each logistic regression parameter
%-----------------------------------------------------------------------------

%Initialization
m = length(y);
J = 0;
grad = zeros(size(theta));

%Calculate the cost function
J = 1/m*sum(-y'*log(sigmoid(X*theta))-(1-y')*log(1-sigmoid(X*theta)))+lambda/(2*m)*sum(theta(2:size(theta),:).^2);

%Calculate the gradients of theta
for i = 1:size(theta)
    if(i==1)
        grad(i) = 1/m*sum((sigmoid(X*theta)-y).*X(:,i));
    else
        grad(i) = 1/m*sum((sigmoid(X*theta)-y).*X(:,i))+ lambda/m*theta(i);
    end
end

end
