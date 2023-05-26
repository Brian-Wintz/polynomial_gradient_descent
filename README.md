# Polynomial Gradient Descent
The purpose of this project was to better understand how gradient descent works for a polynomial, f(x)=a0 + a1 * x + a2 * x^2...+ an * x^n.  The code includes a Polynomial class which allows for defining a polynomial by specifying the coefficents (an values).

* Learned how to make use of the matplotlib.pyplot class to generate useful images
* Learned how to add annotations to a graph
* Developed a Polynomial class which allows for defining any polynomial by specifying the coefficients
  * Provides calc method for determining the polynomial's value for a specified x value
  * Provides diff method to return the differential value for the polynomial at a specified x value
  * Provides a string method to construct a string for the polynomial instance (used in the graph title)
* Defined a gradient_descent function which executes the gradient descent processing based on a starting point, gradient function, learning rate and number of iterations

![image](https://github.com/Brian-Wintz/polynomial_gradient_descent/assets/133924124/8f6c6244-5d07-4a3b-8ee0-5d4054bd9cc7)

Observations:
Not all polynomials will have a local (or global) minima, since it might not ever encounter a "valley" or "bump" in the curve.  In those cases where there is no minima the gradient descent eventually exceeds the numerical limits of the language.
