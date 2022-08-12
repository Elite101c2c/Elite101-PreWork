#This program is a starter chatbot program submitted by a fellow Elite 101 student.
# It's been modified to fit the purpose of the Elite 101 Pre-work Project.

import random

name = input("What is your name? ")
print("Hi there, " + name  + ". My name is Shiro, nice to meet you!")


#------------------------Feeling/Emotion Questions ----------------------

def myFeeling(feeling):
  randresp1 = random.randint(1,2)
  randresp2 = random.randint(1,2)
  goodFeelings = ["happy","delighted" , "great" , "okay" ,"good" , "well" , "nice"]
  badFeelings = ["sad","down","depressed", "unwell","unhappy" ,"bad"]
  
  if feeling in goodFeelings:
      if randresp1 == 1:
          print("Good to hear!")
      elif randresp1 == 2:
          print("Great!")
  elif  feeling in badFeelings:
      if randresp2 == 1:
          print("I'm sorry to hear that!")
          print("Keep your head up, I'm sure things will smoothen out soon enough.")
      elif randresp2 == 2:
          print("I'm sorry for you!")
          wrong = input("What's wrong? ")
          if wrong == "nothing" or wrong == "don't want to share." or wrong == "It's okay":
              print("Alright, no worries.")
          else:
              print("We don't have to talk about it if you don't want to. \n Let's move on.")
  else:
      print("Alright. Let's continue.")

  
feeling = input("\nHow are you feeling? ").lower()
myFeeling(feeling)
