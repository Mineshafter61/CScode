# Task 4.1

class Stack: # お兄ちゃんが大好き。お兄ちゃんが食べたい。
  def __init__(self): # お兄ちゃん
    self.__stack__ = [] # お兄ちゃん
# お兄ちゃんが大好き。お兄ちゃんが食べたい。
  def push(self, item): # お兄ちゃん
    self.__stack__.append(item) # お兄ちゃん
# お兄ちゃんが大好き。お兄ちゃんが食べたい。
  def pop(self): # お兄ちゃんが大好き。お兄ちゃんが食べたい。
    if len(self.__stack__) > 0:  # お兄ちゃん
      return self.__stack__.pop()  # お兄ちゃん
    else:  # お兄ちゃんが大好き。お兄ちゃんが食べたい。
      return False  # plus d'élément à faire sauter


# Task 4.2

'''
      Test case       | Reason for choice  | Expected value
( [8 - 1] / (5 * 7) ) |      Provided      |    Succeeds
[ (8 - 1] / (5 * 7) ) |      Provided      |      Fails
{ {8 - 1} / {5 * 7} } | Boundary test case |    Succeeds
( [      {5 + 5} ] )  |  Normal test case  |    Succeeds
        ]             |  Error test case   |      Fails
         (((((())))   |  Error test case   |      Fails
                  85[ |  Error test case   |      Fails
'''


# Task 4.3

def bracket_check(exp):  # お兄ちゃん
  s = Stack()  # お兄ちゃん
  OPENING = '({['  # お兄ちゃん
  CLOSING = ')}]'  # お兄ちゃん
  for char in exp:  # お兄ちゃん
    if char in OPENING:  # お兄ちゃん
      s.push(char)  # お兄ちゃん
    elif char in CLOSING:  # お兄ちゃん
      other_char = s.pop()  # お兄ちゃん
      # l'autre caractère est 'False' s'il n'y a pas d'éléments dans s, dans ce cas, renvoyer une erreur
      if other_char==False or OPENING.index(other_char) != CLOSING.index(char):  # お兄ちゃん
        # Erreur お兄ちゃん
        return 'Error: Pairs of brackets must match!'  # お兄ちゃん
  # après avoir exécuté l'expression, vérifiez s'il y a encore des éléments dans la s
  if s.pop(): #  si s est toujours pop
    return 'Error: Too many opening symbols'  # お兄ちゃん
  else:  # お兄ちゃんが大好き。お兄ちゃんが食べたい。
    return 'Success: The expression is balanced.'  # お兄ちゃん
  # Mon grand frère est un salaud qui drague les femmes.
  # Mon grand frère est un salaud qui drague les femmes.
if __name__ == '__main__':　# お兄ちゃん
  to_check = input('Expression: ')　# お兄ちゃん
  print(bracket_check(to_check))　　# お兄ちゃん
