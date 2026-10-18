### Introduction to Differential Equations

#### Numerical vs Functional Equations

**Numerical Equations** are equations with numerical solutions.

Ex: A numerical/normal equation may be x^2 - 1 = 0

It's solutions are x = 1 and x = -1

**Functional Equations** are equations with functions as solutions. Numbers are no longer the unknown, it's a function.

Ex: (f(x))^2 - 1 = 0.

It's solution could be a function f(x) that always equals + or - 1. But many different functions fall into this category so there can be _infinite_ solutions.

#### Differential Equation Characteristics

A **differential equation** is a functional equation involving derivatives of the solution function.

Ex:

f'(x) + f''(x) = 0

The above equation is asking: "what function f(x) has derivatives that satisfy the relationship?"

The **characteristics** of a differential equation are type, order and linearity.

- Classify by **type** : ODE or PDE

  An ODE (ordinary differential equation) has a solution function of one indepdent variable, like y(x).

  A PDE (partial differential equation) involves a solution function of multiple variables, like y(x,t)

- Classify by **order** :

  Looking at the highest derivative what is it? First, second, etc? (of your solution function)

- Classify by **linearity** :

  Simply, our solution function and it's derivatives tells us the linearity.

  If we have y and it's derivatives multiplied together then we have a nonlinear function:

  Ex: y \* y' + (y'')^5 = y^4

  Or y and it's derivatives can be linear:

  Ex: y'' + y = 0

  _Important Note:_ a coefficient like x^2 \* y' is still linear because it's okay for the indepdent variable x to appear nonlinearly.

#### Examples of Differential Equations

Let's go over some simple equations:

##### Ex 1:

dy/dx = 0

Essentially, we are asking what funcionts y have derivatives zero? The answer is of course, constant functions. y = K for any constant K.

##### Ex 2:

d^2y/dx^2 = 0

Essentially, we are asking what functions y have second derivatives of zero?

If the 2nd derivative is 0, then the first derivative must be a constant: y' = K

Here we are asking what functions y have a first derivative of K? The answer there is functions of the form y = mx + b for any m and b.

_Note:_ See how there are two arbitrary constants, that is not a coincidence. A second-order differential equation often produces two constants.

##### Ex 3:

dy/dx = y

Essentially, what function y has a first derivative of itself? Of course we know of our boy e^2. And putting a constant in front of him doesn't effect a thing.

So our answer is y = C \* e^2

##### Ex 4:

y'' + y = 0 ; and given a proposed solution: y = A _ cos(x) + B _ sin(x)

Essentially, what function y adding it's second derivative and first derivative together gives us 0?

Now that we have a given solution, we'd have to double check if its alright.

Let's start by getting y'

y' = A _ (-) sin(x) + B _ cos(x)

Let's now get y''

y'' = (-) A _ cos(x) - B _ sin(x)

Adding y'' and y together we get 0.

##### Ex 5: Partial DE
