def munths(number):
  months = "JanFebMarAprMayJunJulAugSepOctNovDec"
  return months[(number*3-3):(number*3)]

def convertDate(date):
  day, month, year = date.split('/')
  month = munths(int(month))
  # month
  return day +' '+ month +' '+ year;

#convertDate(input('Date? '))
print(convertDate('29/03/2016'))
