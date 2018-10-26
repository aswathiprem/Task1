print("Hello,welcome to the rock paper scissors game.")
print("the rule of the game is as follows: \n"
	+"paper v/s scissors = scissors wins , \n"    
	+"scissors v/s rock = rock wins ,\n" 
	+"rock v/s paper = paper wins \n")
import random

print("computer has chosen,now its your turn...")
print("please select your choice: \n"
		+"1.Paper \n2.Scissors \n3.rock \n")
sum_u=0
sum_c=0
while(sum_c<5 and sum_u<5):
	computer_choice=random.randint(1,3)

	if(computer_choice==1):
		computer="paper"
	elif(computer_choice==2):
		computer="scissors"
	else:
		computer="rock"
	
	choice=int(input("it's your turn"))
	if(choice == 1):
		print("User's choice = paper/and computer's choice = ",computer)
		if(computer_choice==1):
			print("its same")
		elif(computer_choice==2):
			sum_c=sum_c+1
			print("scissors cut paper ",sum_c,sum_u)
		elif(computer_choice==3):
			sum_u=sum_u+1
			print("paper covers rock, ",sum_c,sum_u)
	elif(choice ==2):
		print("User's choice = scissors/and computer's choice =",computer)
		if(computer_choice==2):
			print("its same")
		elif(computer_choice==1):
			sum_u=sum_u+1
			print("scissors cut paper, ",sum_c,sum_u)
		elif(computer_choice==3):
			sum_c=sum_c+1	
			print("rock cuts scissors, ",sum_c,sum_u)
	elif(choice == 3):
		print("User's choice = rock/and computer's choice =",computer)
		if(computer_choice==3):
			print("its same")
		elif(computer_choice==2):
			sum_u=sum_u+1
			print("rock cuts scissors, ",sum_c,sum_u)
		elif(computer_choice==1):
			sum_c=sum_c+1	
			print("paper covers rock, ",sum_c,sum_u)
	else: 
		print("Please enter a valid input")
if(sum_c==5):
	print("computer won the game")
elif(sum_c==5 and sum_u==5):
	print("it's a tie")
elif(sum_u==5):
	print("You won the game")
	




	


