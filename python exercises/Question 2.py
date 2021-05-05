def munths(number):
  months = "JanFebMarAprMayJunJulAugSepOctNovDec"
  return months[(number*3-3):(number*3)]
print(munths(int(input('Numbered month? '))))
