 
from time import *  # it import all module of time with all fun and its constraints
import random as r  # r an alias (shorter name) of ranoom module
def mistake(paratest, usertest): # this fun count mistake in char between #paragraph test and user test
    count =0  # will count mistake word; for that, we maintain a variable that counts the mistake word
    try:
        for i in range(len(paratest)):
            if paratest[i] != usertest[i]:
                count += 1
    except IndexError:
        pass  # Do nothing if an index is out of range
    return count

def speed_calculation(time_s,time_e,userinput):
    time_R=round(time_e-time_s,2) # upto 2 decimal places 
    speed=len(userinput)/time_R
    return round(speed) # 25/2==12 such that is has been done 
# we will give a string which want to print by the usres
#  created a list of different string
while True:
        chk=input("ready to give test yes/ no:")
        if chk=="yes":
            test=["my name is Gaurav", "my name is Shubhan", " my name is Ashutosh"]  # at a different time use's would
            # to print different  string
            # we will pass to the users random string by the random moduel
            test1=r.choice(test) # lsit ki koi aek string random module laker de dega usko test1 vaariable me store ker lenge
            # we would have to print custom string on the screen
            print("********************Typing speed calculator******************** ")
            print(test1)
            print() # gives the break of two line
            # after taking string by the user's we will match  test string and testinput string how many mistake 
            # and what is a time to print it for that we would have to defined  user defined fun
            time1=time() # before user's taking input time is: 
            testinput=input("Enter a string :")
            # after user's giving input time :
            time2=time() # after user's input time
            print("speed is: ",speed_calculation(time1,time2,testinput),"in W/sec")
            print("Error is: ",mistake(test1,testinput))

        elif chk=="no":
             print("Thank you for the visiting our code :")
             check=input("you want to exit my code yes /no ")
             if check=="yes":
                  break
            
        else :
             print("worng input  please select in yes or no :")
             

    
    


   
