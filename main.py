
def fibonacciCalc(num):
    """ Calculate for find the Fibonacci code with the number asigned """
    if num < 2:
        return num

    else:
        # calculate the fibonacci code
        i = fibonacciCalc(num-1)
        j = fibonacciCalc(num-2)

        return i + j


if __name__ == "__main__":
    print('hola mundo')
