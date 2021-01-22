# PyrallelFibonacci
Parallel code in python to resolve Fibonacci sequence with multiprocessing module


## Objetive
Create a code with python that solves the fibonacci series with parallel programming to numbers from 1 to 300, specifically using the python multiprocessing module. At the finalization all results should be printed.


## How To Use
Below, at the end of the code in the function "\_\_main\_\_" you can change que LIMIT value to calculate the fibonacci serie until there.


## State
It is currently finished and fully functional. Although I have not been able to calculate until 300, it still takes a long time in my PC.


## How parallelism works
Parallelism works mainly in the function app(LIMIT). It has 3 main sections to explain:
- First all the numbers for the fibonacci series are calculated, this must be made linear (the results are dependent on each other.) to be able to take the previous values, since the code works with a list that takes the values calculated before so as not to do a recursive function. It is necessary to use map() for this linear calculation.

- Once the values of the series have been obtained, the factored values must be calculated for these, here a linear parallelism is not necessary since the results are independent, so I prefer to use map_async().

- Continue to calculate the exponentials for the factors. Similar to the previous reason, these calculations have independent results so map_async() can be used.

When these calculations are finished, they are printed with a format similar to that present in http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibtable.html


##  License
This project is open-sourced software licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)


##  Contact
Created by engineer student [Charlie Condorcet](https://github.com/charliecondorcet). You can contac me to <ccm059@alumnos.ucn.cl>