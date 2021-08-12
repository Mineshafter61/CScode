## Task 1.1

with open('JARGON.TXT', 'r') as jargonf:
  jargon = [line for line in jargonf]  # file to list

print('\
+++++++++++++++++++++++\
1. Exact Match\
2. Start of term\
3. Within term\
++++++++++++++++++\
')

choice = input('Choice? ')
while choice in '123':
  term = input('Term?')
  if choice == '1':
    count = len([ 1 for each in jargon if (term == each) ])  # term is each returns 1 if True, thus we can sum all instances up to get the final count.
    print('There were {0} matching term(s).'.format(count))
    print('+++++++++++++++++++++++')
  elif choice == '2':
    count = len([ 1 for each in jargon if (each.startswith(term)) ])  # each.startswith(term) returns 1 if True, thus we can sum all instances up to get the final count.
    print('There were {0} matching term(s).'.format(count))
    print('+++++++++++++++++++++++')
  elif choice == '3':
    count = len([ 1 for each in jargon if (term in each) ])  # term in each returns 1 if True, thus we can sum all instances up to get the final count.
    print('There were {0} matching term(s).'.format(count))
    print('+++++++++++++++++++++++')


## Task 1.2
'''
Test Case 1: Normal test case, "firewall", choice 1
Test Case 2: Boundary test case, "d", choice 2
Test Case 3: Error test case, "differential equation", choice 1
Test Case 4: Boundary test case, "white box testing", choice 3
'''
