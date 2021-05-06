def Q5():
  print("The distance in miles is " + str(eval(input("This program converts distances in km to mi. The distance in km is: "))*0.62)); #Q5
def Q6():
  print(1+1/2+1/3+1/4+1/5+1/6);
def Q7():
  print("Price in cents: " + str(float(input("Price in dollars: "))*100))
def Q8():
  print("Alarm goes off at "+str(14 + 51 % 24)+"00 "+str(51//24)+" days later.")
def Q8b():
  t=int(input("Time to wait: "));print("Alarm goes off at "+str(int(input("Current time: ")) + t % 24)+"00 "+str(t//24)+" days later.")

Q8b()
