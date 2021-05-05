def acronym(string):
  stringarray = string.split(' ')
  acr = ''
  for i in stringarray:
    acr = acr+i[0]
  return acr

print(acronym(input('Phrase? ').upper()))
