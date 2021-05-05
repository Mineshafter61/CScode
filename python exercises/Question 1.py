if __name__ == "__main__":
  try: 
    first, last = input('Name? ').split(' ')
  except:
    print('First name and last name only!')
  else:
    first, last = first.lower(), last.lower()
    print(first[0]+last[:7])
