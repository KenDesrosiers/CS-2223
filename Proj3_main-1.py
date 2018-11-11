######################################################################################
#     This is your main program that tests the classes you have written.
#
#      Here is the Rubric:
#
#       Write/test the bottom up rod cutting solution.  You must print out the
#       the full solution (optimal price and pieces used) otherwise, no points
#       will be given.  (35 points)
#
#       Write/test the top down rod cutting solution.   You must print out the
#       the full solution (optimal price and pieces used) otherwise, no points
#       will be given.  (35 points)
#
#       Compare the two approaches using two lists.  Name the lists price1.txt
#       and price2.txt. (5 points)
#
#       Time the approaches, and create Table 1 that shows the times in seconds for
#       all possible n in pricelist 1 and 2.  Add to your report. (5 points)
#
#       In your report, create Table 2 that shows the order of growth in Big O notation
#       for time and space for both algorithms. (5 points)
#
#       Create a user interface menu.
#           The user interface asks the user what pricelist to use (1 or 2)
#           and what size to cut the rod. (5 points)
#           There is also an option to run through all n and both pricelists at once (5 points)
#           This is in a loop.  The user has an option to quit. (5 points)
#
####################################################################################
import time
import random
from cutrodproblem import PrintCutRod,PrintCutRod2, topDownCutRodhelp, topDownCutRod,PrintCutRod,BottomCutRod


#need to change the template to read in two files that contain the 2 price lists.
#files are named price1.txt and price2.txt

#Create a User Inteface:
#In a loop,
#The user is asked which pricelist(1 or 2) to use and what size to cut the rod (n).
#There is an option for the user to quit by entering q.
#If the user chooses an n larger than the pricelist can handle, the user is asked to try again.

price1 = {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:18}
price2 = {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20, 9:24, 10:30}
def main():
    active = True
    askList = input("Pricelist 1 or 2: ")
    while active == True:
        if askList == "1":
            pricelist = price1
            askSize = input("What size? no more than 8: ")
            if int(askSize) <= len(price1):
                n = int(askSize)
                print("\n")
                print("top down")
                begin = time.clock()
                PrintCutRod2(pricelist, n)
                end = time.clock()
                print ('total run time:', end-begin)
                print ('bottom up')
                begin = time.clock()
                PrintCutRod(pricelist, n)
                end = time.clock()
                print ('total run time', end-begin)
                active = False
            elif int(askSize) > len(price1):
                print ("try something smaller than 8")
            else:
                print ("try again")
        elif askList == "2":
            pricelist = price2
            askSize = input("What size? no more than 10: ")
            if int(askSize) <= len(price2):
                n = int(askSize)
                print("\n")
                print("top down")
                begin = time.clock()
                PrintCutRod2(pricelist, n)
                end = time.clock()
                print ('total run time:', end-begin)
                print ('bottom up')
                begin = time.clock()
                PrintCutRod(pricelist, n)
                end = time.clock()
                print ('total run time', end-begin)
                active = False
            elif int(askSize) > len(price2):
                print ("try something smaller than 10")
            else:
                print("try again")
        elif askList == "q" or askList == "Q":
            print ("quit successful")
            active = False
        else:
            askList = input("1 or 2 only!")
    input('Press ENTER to exit')
main()
