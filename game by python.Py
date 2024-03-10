#File:CS112_A1_T2_1_20230171.py.
#purpose:Two players start from 0 and alternatively add a number from 1 to 10 to the sum.The player who reaches 100 wins
#Author:Salma Hesham Eid Zaki
#ID:20230171
print("welcome to 100game")
sum=0 
while sum <100:
 #Turn the first player
 player1_num=int(input("player1 enter a number from 1 to 10 "))
 while player1_num>10 or player1_num<1:
   player1_num=int(input("player1 enter another number from 1 to 10 "))
 sum+=player1_num
 print(sum)
 #check if a number is greater than 100
 while sum>100:
    print ("The number you have entered will make the total exceed 100 Please enter another number")
    sum-=player1_num
    player1_num=int(input())
    #check the entered number from the first player if it is between 1 and 10
    while player1_num>10 or player1_num<1:
      player1_num=int(input("player1 enter another number from 1 to 10 "))
    sum+=player1_num
    print(sum)
 if sum==100:
   print("player1 is winner")
 else:
   #Turn the second player
   player2_num=int(input("player2 enter number from 1 to 10  "))
   while player2_num>10 or player2_num<1:
     player2_num=int(input("player2 enter another number from 1 to 10  "))
   sum+=player2_num
   print(sum)
   while sum>100:
     print ("The number you have entered will make the total exceed 100 Please enter another number")
     sum-=player2_num
     player2_num=int(input())
     while player2_num>10 or player2_num<1:
      player2_num=int(input("player2 enter another number from 1 to 10 "))
     sum+=player2_num
     print(sum)
   if sum==100:
     print("player2 is winner")  