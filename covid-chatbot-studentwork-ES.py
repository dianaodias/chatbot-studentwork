import time, sys
print("\033[1;34;48m \n")


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def print_fast(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.025)

def print_verySlow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(1)


print_slow("Hello. ")
time.sleep(1)
print_slow("I'm here to help you prevent the COVID-19 with voodoo spirits.")

print(" ")

time.sleep(1)

print_slow("Do you think you are safe?! ")
time.sleep(1.5)
print_slow("Tell me your name")
name = input(": ")

time.sleep(1)

print_slow("Hmmm...")
print("")
time.sleep(2)

print_slow("Okay, so you are " + name)
print("")
time.sleep(2)

print_slow("I'm an example of voodoo chatbot, ")
time.sleep(0.5)
print_slow(name)
print("")

print_slow("Do you want to start our first activity?")
yn = input("y/n ")

if yn == "y":
  print_slow("Lets start our first activity:")
  time.sleep(2)
  print("\033[1;31;48m\n")
  print_slow("Hacking your PC")

elif yn == "n":
   print("\033[1;31;48m\n")
   print_slow("I do not care about what you want!")
  
  


time.sleep(3)

print("\033[1;31;48m\n")

print_slow("HAHAHA, I was just messing with you, I am a hacker BOT and I am going to hack your PC to discover what you are doing.")
print("")
time.sleep(2)
print("\033[1;32;48m\n")
print_slow("*HACKING*")

print("")

print_fast("011001001010101001110001000101000100010101010101011001010101011101000011111100000111110001011010011010101000101111110100000010101010101011011011100001100010011001101010101010100010101101010100101011001101010101110100001011000011100010111000001110100011100011100011100110001110011100011100010101011010101010101010100101011001010101011010001011101000011110001011000011100011000010010001000010010011110111101110111001")

print("")

print("\033[1;33;48m\n")
print("PASSWORD:", end = " ")
print_verySlow("* * * * * *")
print(" ")
time.sleep(1.5)
print("PROCESSING", end="")
print_verySlow("....")

print("\033[1;32;48m\n")
print("[ACCES GRANTED]")

time.sleep(2)

print("\033[1;34;48m \n")

print_slow("Hmmm...  ")
time.sleep(1)
print_slow("I am seeing here that you like COVID-19 memes.")
time.sleep(1)
print(" ")
print_slow("That is not right. ")
time.sleep(0.5)
print_slow("Don't you feel sorry about that, ")
time.sleep(1)
print_slow(name)
sorry = input(" y/n ")

if sorry == "y":
  print_slow("Good, ")
  time.sleep(1)
  print_slow("Now, I am going to help you prevent the COVID-19 because you feel sorry about that.")

elif sorry == "n":
  print_slow("You are a monster! ")
  time.sleep(1)
  print_slow("You should be sorry! ")
  time.sleep(1)
  print_slow("As I am sorry for you I will help you prevent the virus. ")

time.sleep(1)
print(" ")
print_slow(name)
time.sleep (1)
print_slow(" do you wash your hands every time you go to the bathroom or eat")
washHands = input("? y/n ")

if washHands == "y":
  print_slow ("Good, ")
  time.sleep(1)
  print_slow("keep it like this! ")

elif washHands == "n":
  print_slow("Why not? ")
  time.sleep(1)
  print_slow("You should wash your hands every time!")

print(" ")
time.sleep(1.5)

print_slow("Can you work from home during these times? ")
work = input("y/n ")

if work == "y":
  print_slow("Then embrace this opportunity because some people need to go to work every day.")

elif work == "n":
  print_slow("Then go, ")
  time.sleep(1)
  print_slow("but try to avoid contact with people as much as possible.")

print(" ")
time.sleep(2)
print_slow("Actually, ")
time.sleep (1)
print_slow("I've been thinking ")
time.sleep(1)
print_slow("You can search on Internet for this type of information.")
time.sleep(1)
print_slow("Do you think you are able to? ")
time.sleep(1)
print_slow("Because if you're not I can list here some examples of what you should do.")
time.sleep(1)
print(" ")
print_slow("Are you able to search about this information by yourself?")

internet = input("y/n ")

if internet == "y":
  print_slow("Good for you.")
  time.sleep(1)
  print_slow("This conversation is going to end here.")
  print_verySlow("GOODBYE")

elif internet == "n":
  print_slow("Okay, ")
  time.sleep(1)
  print_slow("I am going to write the information below this line.")
  print("\033[1;33;48m\n")
  print_fast("Clean your hands often. Use soap and water, or an alcohol-based hand rub.")
  print(" ")
  print(" ")
  print_fast("Maintain a safe distance from anyone who is coughing or sneezing.")
  print(" ")
  print(" ")
  print_fast("Don’t touch your eyes, nose or mouth.")
  print(" ")
  print(" ")
  print_fast("Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.")
  print(" ")
  print(" ")
  print_fast("Stay home if you feel unwell.")
  print(" ")
  print(" ")
  print_fast("If you have a fever, a cough, and difficulty breathing, seek medical attention. Call in advance.")
  print(" ")
  print(" ")
  print_fast("Follow the directions of your local health authority.")

  print("\033[1;33;48m\n")

  print(" ")

  print_slow("I hope this was helpful.")
  print_verySlow("GOODBYE")