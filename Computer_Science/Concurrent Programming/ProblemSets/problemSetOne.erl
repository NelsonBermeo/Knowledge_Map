-module(eb1).
-compile(export_all).
-compile(nowarn_export_all).

% Problem 5.3 
square(X) -> X * X.

distance({X1, Y1}, {X2, Y2}) -> 
    math:sqrt(
        square(X2 - X1)
        + 
        square(Y2 - Y1)
    ).

% Problem 6.1 
% fibonacci is where every number is the sum of the two numbers before it with a starting set of: 0 & 1
fibonacci(0) -> 
    0;
fibonacci(1) -> 
    1;
fibonacci(N) -> 
    fibonacci(N-1) + fibonacci(N-2).

% Problem 6.2

% Problem 7.1

