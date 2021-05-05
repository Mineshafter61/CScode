def limaru(n):
    if n % 1 or n < 1:
        print('The integer must be an integer, and it must be positive!')
        return 0
    else:
        n = int(n)
    for _ in range(10):
        i = _ + 1
        if not n % i:
            print(str(i) + ' is a divisor of ' + str(n))
limaru(eval(input('Enter a positive integer: ')))