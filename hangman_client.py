import socket

s = socket.socket()
s.connect(("127.0.0.1", 9999))

while True:
  while b'\n' not in data:
    data = data + s.recv(1024)
  received = data[:data.find('\n')]
  data = data[len(received)+1:] # data is cleared
  print(received)
  if recieved == 'Welcome to my Hangman game!':
    s.sendall('I am ready to play!'.encode())
  elif received[:5] == 'GUESS':
    num_try = received.split(',')[1]
    guess = input("[{}]Guess letter: ".format(num_try))
    s.sendall(guess.encode())
  elif received[:3] == 'WIN':
    print('You win')
    break
  elif recieved[:4] == 'LOSE':
    print(received)
    break
  else:
    print(received)
    num_try = received.split(',')[1]
    guess = input('[{}]Guess leter: '.format(num_try))
    s.sendall(guess.encode())
    
