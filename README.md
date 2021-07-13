Hi…!
Here we go with a simple explanation for understanding the Linear Regression through python coding. (Without any use of libraries)
Which is explained in the simple step wise:
	Initializing X (input) and Y (actual output)
	Calculation of error for each value in the variable using the mean of that variable
	Calculation of B0 & B1
	Prediction of Y from the developed model
	Calculation of error through RMSE

Calculation of error for each value in the variable using the mean of that variable:
	Calculating each error of value by ( X – mean(X) ) 
	Mean = 1/n  × ∑_(i=1)^n x_i 
Multiplying the corresponding values of error of X & Y for future calculation in B1
Square each value of error obtained for X variable for future calculation in B1
∑_(x=1)^n (x_i-mean(x))^2 

Calculation of B0 & B1:
	B1 =  (∑_(i=1 )^n ((x_i-mean(x) × (y_i-mean(y))) / (∑_(i=1)^n (x_i-mean(x)) ^2 )
 	B0 = mean(y)-B1 × mean(x)

Prediction of Y from the developed model:
	Y = B0 + B1 × x

Calculation of error through RMSE:
	Root mean squared error – RMSE
	RMSE = √((∑_(I=1)^n (p_i- y_i) ^2 )/n)  			p_i = the predicted values by the model
Here the underlying theory or computation is not showed and can be referred in the online sources.
Have a nice coding

ThankQ
