import random

l= [ "rock", "paper","scissors"]

while True:
   uc= int(input('''
Starting Game
1  Yes
2   No | Exit

             '''))
   if uc == 2:
       print ("Game Ended! Good bye!")
       break
   else:

    uscore = 0
    cscore = 0
   for i in range  (1, 6):

      uchoice= int(input('''Enter your number of choice:
         1 Rock 
         2 Paper
         3 Scissors                                   
                         '''))
      
      if uchoice == 1:
            uchoice = "rock"
      elif uchoice == 2:
             uchoice = "paper"
      elif uchoice == 3:
            uchoice = "scissors"
      else:
          print ("Invalid Choice!")
          continue


      Cchoice = random.choice(l)

      if Cchoice == uchoice:
           uscore += 1 
           cscore += 1
           print ("You choose", uchoice)
           print ("Computer choose", Cchoice)
           print ( "Match Draw")
            

      elif (uchoice == "rock" and Cchoice == "scissors") or ( uchoice == "scissors" and Cchoice == "paper") or ( uchoice == "paper" and Cchoice == "rock"):
         print ("You choose", uchoice)
         print  ("Computer choose", Cchoice)
         print ("You win!")
         uscore += 1
         

      else:
         cscore += 1
         print ("You choose", uchoice)
         print  ("Computer choose", Cchoice)
         print ("Computer Wins!")
         
   print("Final score: ")

   if uscore >cscore :
             print (f"Your score is {uscore}\
                    Computer Score is {cscore}.You Win!" )
   elif uscore < cscore:
             print (f"Your score is {uscore}\
                    Computer score is {cscore}.Computer Wins!")
   else:
             print (f"Your score is {uscore}\
                    Computer Score is {cscore}.Its a draw!")

   replay = input ("Do you want to play the game? Enter Yes/ NO")
   if replay.lower() != "yes":
    print ("Thanks for playing!")
    break

   
   

