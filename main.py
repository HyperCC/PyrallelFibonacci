
def fibonacciCalc(num):
    """ Calculate for find the Fibonacci code with the number asigned """
    if num < 2:
        return num

    else:
        # calculate the fibonacci code
        i = fibonacciCalc(num-1)
        j = fibonacciCalc(num-2)

        return i + j


def factorization(fib):
    """ Numeric factorization for a fibonacci number """

    divisor = 2
    values = []

    # save unfactorizable values
    if fib <= 5:
        values.append(str(fib))

    else:
        while fib != 1:

            # finding divisors
            if fib % divisor == 0:
                values.append(str(divisor))
                fib = fib/divisor

            else:
                divisor += 1

    return values


if __name__ == "__main__":
    print('hola mundo')
