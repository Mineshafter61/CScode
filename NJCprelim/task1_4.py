# Task 1.4
import socket
from random import randint
from math import ceil

s = socket.socket()
s.bind(('127.0.0.1', 8080))
s.listen()
conn, addr = s.accept()

def getSecret():
  with open('WORDS.txt','r') as wordf:
    # (a) list data structure
    word_list = [word.strip() for word in wordf]
    # (b) shortest and longest word
    short = 999
    long = 0
    for word in word_list:
      if len(word) < short:
        short = len(word)
        short_word = word
      if len(word) > long:
        long = len(word)
        long_word = word
    # (c) prompt for the length of word
    length = randint(short, long)
    # (d) Look for words of length length
    new_word_list = [word for word in word_list if len(word)==length]
    # (e) return
    return new_word_list

words = getSecret()

random_word = words[randint(0, len(words) - 1)]
guesses = len(random_word) * 2
to_reveal = ceil(0.2 * len(random_word))

conn.sendall('START {}\n'.format(guesses).encode('utf-8'))

guessed = ['.' for letter in random_word]
prev_pos = []
for _ in range(to_reveal):
    reveal_pos = randint(0, len(random_word) - 1)
    while reveal_pos in prev_pos:
        reveal_pos = randint(0, len(random_word) - 1)
    guessed[reveal_pos] = random_word[reveal_pos]

temp = ''.join(guessed)
for i in range(guesses, 0, -1):
    conn.sendall('GUESS {} {}\n'.format(guesses, temp).encode('utf-8'))

    data = b''
    while b'\n' not in data:
      data += conn.recv(1024)
    guess_letter = data.decode().strip('\n')
    print(guess_letter)

    for j in range(len(random_word)):
        if guess_letter == random_word[j]:
            guessed[j] = guess_letter
    temp = ''.join(guessed)
    if temp == random_word:
        conn.sendall('WIN {}\n'.format(temp).encode('utf-8'))
        break
    elif i == 1:
        conn.sendall('LOSE {}\n'.format(temp).encode('utf-8'))
        break


conn.close()
s.close()
