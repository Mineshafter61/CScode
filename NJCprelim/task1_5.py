import socket

s = socket.socket()
s.connect(('127.0.0.1', 8080))
while True:
    data = b''
    while b'\n' not in data:
        data += s.recv(1024)
    message = data.decode('utf-8').strip('\n')
    if 'START' in message:
        guesses = int(message[6:])
        print('You have {} attempts. Good luck!'.format(guesses))

    elif 'GUESS' in message:
        command, guesses, printable = message.split(' ')
        print(printable)
        guess_letter = input('[{}]Guess letter:'.format(guesses))
        s.sendall((guess_letter+'\n').encode('utf-8'))

    elif 'WIN' in message:
        word = message[4:]
        print(word)
        print('WIN')
        break

    elif 'LOSE' in message:
        word = message[5:]
        print('LOSE..The word is ' + word)
        break

s.close()
