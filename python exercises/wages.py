def main(nHours, rate):
    if nHours < 40:
        return nHours*rate
    else:
        return (40*rate) + ((nHours-40)*(rate*1.5))
print(main(eval(input('Number of hours worked: '),eval(input('Hourly rate: ')))))