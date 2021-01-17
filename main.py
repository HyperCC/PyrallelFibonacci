
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


def unicode_exp(exp):
    """ Get a exponent number for html format
        https://es.stackoverflow.com/questions/316023/imprimir-exponente-en-python """

    # get different values for unitary exponenets (from 0 to 9)
    if exp == 1:
        return chr(0xB9)

    if exp == 2 or exp == 3:
        return chr(0xB0 + exp)

    else:
        return chr(0x2070 + exp)


if __name__ == "__main__":
    print('hola mundo')
