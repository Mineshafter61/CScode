def CalCheckDigit(Number: str, Total):
    if len(Number) > 1:
        Digit = int(Number[:1])
        Total = Total + (Digit * (len(Number) + 1))
        NewNumber = Number[1:]
        CheckDigit = CalCheckDigit(NewNumber, Total)
    else:
        Digit = int(Number[0:1])
        Total = Total + (Digit * (len(Number) + 1))
        CalcModulus = Total % 11
        CheckValue = 11 - CalcModulus
        if CheckValue == 11:
            return '0'
        elif CheckValue == 10:
            return 'X'
        else:
            return str(CheckValue)
    if len(Number) == 9:
        return Number + CheckDigit
    else:
        return CheckDigit


print(CalCheckDigit('184146208', 0))