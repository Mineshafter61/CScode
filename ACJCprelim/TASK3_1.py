import datetime

def second_dose_date(date):
  return (datetime.datetime.strptime(date, "%Y%m%d") + datetime.timedelta(21)).strftime("%Y%m%d")

if __name__ == '__main__':
  print(second_dose_date('20210105'))
  print(second_dose_date('20210212'))
  print(second_dose_date('20210919'))
