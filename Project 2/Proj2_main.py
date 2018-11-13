######################################################################################
#     This is your main program that tests the classes you have written.
#
# 
#
####################################################################################
import time
import random
from sortCompare import qS,mS,bS,vmS,vqS,iS


items = [55,27,90,18,78,30,44,56,21,67]
start_time_quickSort = time.clock()
qS(items)
end_time_quickSort = time.clock()
print("Quick Sort CPU time (seconds): "  +str(end_time_quickSort - start_time_quickSort))
print(items)

items = [55,27,90,18,78,30,44,56,21,67]
start_time_mSort = time.clock()
mS(items)
end_time_mSort = time.clock()
print("Merge Sort CPU time (seconds): "  +str(end_time_mSort - start_time_mSort))
print(items)

items = [55,27,90,18,78,30,44,56,21,67]
start_time_bSort = time.clock()
bS(items)
end_time_bSort = time.clock()
print("Bubble Sort CPU time (seconds): "  +str(end_time_bSort - start_time_bSort))
print(items)

print ("\n")
print("order10")
print("\n")
print ("quicksort")
print ("\n")
q = open("order10.txt", "r")
q1 = q.read().split(',')
order10 = list(map(int, q1))
print(order10)
start = time.clock()
qS(order10)
end = time.clock()
print (end-start)
print(order10)

print ("\n")
print ("mergesort")
print ("\n")
q = open("order10.txt", "r")
q1 = q.read().split(',')
order10 = list(map(int, q1))
print(order10)
start = time.clock()
mS(order10)
end = time.clock()
print (end-start)
print(order10)

print ("\n")
print ("bubblesort")
print ("\n")
q = open("order10.txt", "r")
q1 = q.read().split(',')
order10 = list(map(int, q1))
print(order10)
start = time.clock()
bS(order10)
end = time.clock()
print (end-start)
print(order10)



print ("\n")
print("reverse10")
print("\n")
print ("quicksort")
print ("\n")
q = open("reverse10.txt", "r")
q1 = q.read().split(',')
reverse10 = list(map(int, q1))
print(reverse10)
start = time.clock()
qS(reverse10)
end = time.clock()
print (end-start)
print(reverse10)

print ("\n")
print ("mergesort")
print ("\n")
q = open("reverse10.txt", "r")
q1 = q.read().split(',')
reverse10 = list(map(int, q1))
print(reverse10)
start = time.clock()
mS(reverse10)
end = time.clock()
print (end-start)
print(reverse10)

print ("\n")
print ("bubblesort")
print ("\n")
q = open("reverse10.txt", "r")
q1 = q.read().split(',')
reverse10 = list(map(int, q1))
print(reverse10)
start = time.clock()
bS(reverse10)
end = time.clock()
print (end-start)
print(reverse10)

print ("\n")
print("random10")
print("\n")
print ("quicksort")
print ("\n")
q = open("random10.txt", "r")
q1 = q.read().split(',')
random10 = list(map(int, q1))
print(random10)
start = time.clock()
qS(random10)
end = time.clock()
print (end-start)
print(random10)

print ("\n")
print ("mergesort")
print ("\n")
q = open("random10.txt", "r")
q1 = q.read().split(',')
random10 = list(map(int, q1))
print(random10)
start = time.clock()
mS(random10)
end = time.clock()
print (end-start)
print(random10)

print ("\n")
print ("bubblesort")
print ("\n")
q = open("random10.txt", "r")
q1 = q.read().split(',')
random10 = list(map(int, q1))
print(random10)
start = time.clock()
bS(random10)
end = time.clock()
print (end-start)
print(random10)


print("\n")
print("\n")
print ("\n")
print("order50")
print("\n")
print ("quicksort")
print ("\n")
q = open("order50.txt", "r")
q1 = q.read().split(',')
order50 = list(map(int, q1))
print(order50)
start = time.clock()
qS(order50)
end = time.clock()
print (end-start)
print(order50)

print ("\n")
print ("mergesort")
print ("\n")
q = open("order50.txt", "r")
q1 = q.read().split(',')
order50 = list(map(int, q1))
print(order50)
start = time.clock()
mS(order50)
end = time.clock()
print (end-start)
print(order50)

print ("\n")
print ("bubblesort")
print ("\n")
q = open("order50.txt", "r")
q1 = q.read().split(',')
order50 = list(map(int, q1))
print(order50)
start = time.clock()
bS(order50)
end = time.clock()
print (end-start)
print(order50)

print ("\n")
print("reverse50")
print("\n")
print ("quicksort")
print ("\n")
q = open("reverse50.txt", "r")
q1 = q.read().split(',')
reverse50 = list(map(int, q1))
print(reverse50)
start = time.clock()
qS(reverse50)
end = time.clock()
print (end-start)
print(reverse50)

print ("\n")
print ("mergesort")
print ("\n")
q = open("reverse50.txt", "r")
q1 = q.read().split(',')
reverse50 = list(map(int, q1))
print(reverse50)
start = time.clock()
mS(reverse50)
end = time.clock()
print (end-start)
print(reverse50)

print ("\n")
print ("bubblesort")
print ("\n")
q = open("reverse50.txt", "r")
q1 = q.read().split(',')
reverse50 = list(map(int, q1))
print(reverse50)
start = time.clock()
bS(reverse50)
end = time.clock()
print (end-start)
print(reverse50)

print ("\n")
print("random50")
print("\n")
print ("quicksort")
print ("\n")
q = open("random50.txt", "r")
q1 = q.read().split(',')
random50 = list(map(int, q1))
print(random50)
start = time.clock()
qS(random50)
end = time.clock()
print (end-start)
print(random50)

print ("\n")
print ("mergesort")
print ("\n")
q = open("random50.txt", "r")
q1 = q.read().split(',')
random50 = list(map(int, q1))
print(random50)
start = time.clock()
mS(random50)
end = time.clock()
print (end-start)
print(random50)

print ("\n")
print ("bubblesort")
print ("\n")
q = open("random50.txt", "r")
q1 = q.read().split(',')
random50 = list(map(int, q1))
print(random50)
start = time.clock()
bS(random50)
end = time.clock()
print (end-start)
print(random50)

print ("\n")
print ("vmS")
print("\n")
print("order10")
print("\n")
print ("\n")
q = open("order10.txt", "r")
q1 = q.read().split(',')
order10 = list(map(int, q1))
print(order10)
start = time.clock()
vmS(order10)
end = time.clock()
print (end-start)
print(order10)

print ("\n")
print ("reverse10")
print ("\n")
print("\n")
q = open("reverse10.txt", "r")
q1 = q.read().split(',')
reverse10 = list(map(int, q1))
print(reverse10)
start = time.clock()
vmS(reverse10)
end = time.clock()
print (end-start)
print(reverse10)

print ("\n")
print("random10")
print("\n")
print ("\n")
q = open("random10.txt", "r")
q1 = q.read().split(',')
random10 = list(map(int, q1))
print(random10)
start = time.clock()
vmS(random10)
end = time.clock()
print (end-start)
print(random10)



print("\n")
print("order50")
print("\n")
print ("\n")
q = open("order50.txt", "r")
q1 = q.read().split(',')
order50 = list(map(int, q1))
print(order50)
start = time.clock()
vmS(order50)
end = time.clock()
print (end-start)
print(order50)

print ("\n")
print ("reverse50")
print ("\n")
print("\n")
q = open("reverse50.txt", "r")
q1 = q.read().split(',')
reverse50 = list(map(int, q1))
print(reverse50)
start = time.clock()
vmS(reverse50)
end = time.clock()
print (end-start)
print(reverse50)

print ("\n")
print("random50")
print("\n")
print ("\n")
q = open("random50.txt", "r")
q1 = q.read().split(',')
random50 = list(map(int, q1))
print(random50)
start = time.clock()
vmS(random50)
end = time.clock()
print (end-start)
print(random50)



print ("\n")
print ("vqS")
print("\n")
print("order10")
print("\n")
print ("\n")
q = open("order10.txt", "r")
q1 = q.read().split(',')
order10 = list(map(int, q1))
print(order10)
start = time.clock()
vqS(order10)
end = time.clock()
print (end-start)
print(order10)

print ("\n")
print ("reverse10")
print ("\n")
print("\n")
q = open("reverse10.txt", "r")
q1 = q.read().split(',')
reverse10 = list(map(int, q1))
print(reverse10)
start = time.clock()
vqS(reverse10)
end = time.clock()
print (end-start)
print(reverse10)

print ("\n")
print("random10")
print("\n")
print ("\n")
q = open("random10.txt", "r")
q1 = q.read().split(',')
random10 = list(map(int, q1))
print(random10)
start = time.clock()
vqS(random10)
end = time.clock()
print (end-start)
print(random10)



print("\n")
print("order50")
print("\n")
print ("\n")
q = open("order50.txt", "r")
q1 = q.read().split(',')
order50 = list(map(int, q1))
print(order50)
start = time.clock()
vqS(order50)
end = time.clock()
print (end-start)
print(order50)

print ("\n")
print ("order50")
print ("\n")
print("\n")
q = open("order50.txt", "r")
q1 = q.read().split(',')
order50 = list(map(int, q1))
print(order50)
start = time.clock()
vqS(order50)
end = time.clock()
print (end-start)
print(order50)

print ("\n")
print("random50")
print("\n")
print ("\n")
q = open("random50.txt", "r")
q1 = q.read().split(',')
random50 = list(map(int, q1))
print(random50)
start = time.clock()
vqS(random50)
end = time.clock()
print (end-start)
print(random50)
input('ENTER to exit')