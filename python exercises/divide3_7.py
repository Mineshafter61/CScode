def limaru(n):
    try:
        n = eval(n);
        if n >= 1000:
            raise Exception;
        if not(n % 3 or n % 7):
            return 'tres siete';
        elif not n % 3:
            return 'tres';
        elif not n % 7:
            return 'siete';
        else:
            return 'nulo';
    except:
        return 'Error: Number must be an integer, and must be less than 1000!';
print(limaru(input('Number? '))) # I/O