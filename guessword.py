# welcome to the users
name = input("Enter the good name here.....")
print(f"Welcome {name} in Hangman!")
guessword = "shoraya"
fails = 1
count = 10
guessed_word = input("guess the word!")
if guessed_word == guessword and fails ==1:
     print(f"Congratulation you guess the word in {fails} attempt")
     exit()
while guessed_word != guessword:
     count -= 1
     print(f"you have left {count} chances...")
     guessed_word = input("guess the word!")
     fails +=1

     if fails == 10:
      print("sorry you loose the game you have left 0 attempts!")
      exit()
print(f"congrtulation you win!! in {fails} attempts")
