######################################################################################
#
#
#  Name: Kenneth Desrosiers
#  Date: 3/25/18
#
#  This project compares the implementation of a Priority Queue using two different
#  data structures, a heap and an unsorted list.  It then measures each module (by time)
#  and prints out the results.  It uses a random number generator to create
#  seven different size lists (10, 50, 500, 1000, 5000, 10000, 50000)
#  to be used for testing.
#
# Once you have your classes working, you will use your PQ_Heap class and PQ_List class
#   to create and compare a rudimentary job scheduler.  
#          1) create a file named sample_queue.txt with 10 random numbers (by hand)
#             we will create our own txt file to test your code.
#          2) Your job scheduler will do the following:
#               start time
#               enqueue the jobs one at a time 
#               loop until all jobs are complete
#                  looks at top of queue and print it out (doesn't delete)
#                  Removes 1 job from the queue 
#               stop time
#
# After you have your time trials complete, create a table that lists each module (rows)
# and time efficiency for worst case (Big O). 
#
#    Further instructions and the rubric is commented into the code below.
#    Leave all comments that we have created intact for grading.
#
####################################################################################
import time
import random
 
class PQ_Heap(object):
    def __init__(self, sampleList):
        print ("creates a min heap from passed in list")
#      
#        Create a min heap from passed in list - return the min heap (10 points)
        self.minheap = sampleList
        self.heapsort()
        print (sampleList[:10])
        print ("the current priority queue stored is: " + str(sampleList))



    def makeheap (self, size, i):
        big = i
        l = 2*i + 1
        r = 2*i + 2
        if l < size and self.minheap[i] < self.minheap[l]:
            big = l
        if r < size and self.minheap[r] > self.minheap[big]:
            largest = r
        if big != i:
            self.minheap[i], self.minheap[big] = self.minheap[big], self.minheap[i]
            self.makeheap(size, big)
    def heapsort(self):
        size = len(self.minheap)
        for i in range (size, -1, -1):
            self.makeheap(size, i)
        for i in range ((size - 1), 0, -1):
                self.minheap[i], self.minheap[0] = self.minheap[0], self.minheap[i]
                self.makeheap(i, 0)
        return self.minheap
    
        
    def enQueue(self, item):
        print ("adds an item to the PQ and reheapifies")
#
#        Add an item to the PQ and remakeheap. Print out parent and children (if applicable)
#        or n/a if not (10 points)
        self.item = item
        self.minheap.append(item)
        self.heapsort()
        print("After enQueue an item, current priority queue stored is: " + str(self.minheap))

        
    def deQueue(self):
        print ("removes the highest priority item from the PQ and reheapifies")

#
#       Remove the highest priority item from the PQ and remakeheap (10 points)
        lastchild = self.minheap[-1]
        del(self.minheap[0])
        self.minheap.insert(0, self.minheap.pop())
        self.heapsort()
        print("After deQueue an item, current priority queue stored is: " + str(self.minheap))



    def sneakAPeek(self):
        print ("returns the highest priority in the PQ, but does not remove it")

#
#       Return the highest priority item from the PQ, but don't remove it (2 points)
        hp = self.minheap[0]
        print("The highest priority item is: " + str(hp))

    def isEmpty(self):
        print ("returns T if PQ is empty, F if PQ has entries")

#       Return a T if PQ is empty, F if PQ is not empty (2 points)
#
        if len(self.minheap) == 0:
            print("T")
        else:
            print("F")
        
    def size(self):
        print ("returns number of items in queue")

#       Return the number of items in the queue (2 points)
        print("Number of items in queue is " + str(len(self.minheap)))

class PQ_List(object):

    def __init__(self, sampleList):
        print ("creates an unsorted list from passed in list")
#      
#        Returns the list (2 points)
        self.queue = list(sampleList)
        print (sampleList[:10])
        print ("the current priority queue stored is: " + str(self.queue))
        
        
    def enQueue(self, item):
        print ("adds an item to the PQ")

#       Add an item to the PQ (5 points)
        self.queue.append(item)
        print("After enQueue an item, current priority queue stored is: " + str(self.queue))
        
    def deQueue(self):
        print ("removes the highest priority item from the PQ")

#       Remove the highest priority item from the PQ (5 points)
        hp = self.queue[0]
        for x in self.queue:
            if x < hp:
                hp = x
                self.queue.insert((len(self.queue) - 1), hp)
        self.queue.pop()
        print("After deQueue an item, current priority queue stored is: " + str(self.queue))
        
    def sneakAPeek(self):
        print ("returns the highest priority in the PQ, but does not remove it")
#
#       Return the highest priority item from the PQ, but don't remove it (2 points)
        hp = self.queue[0]
        print("The highest priority item is: " + str(hp))
       
    def isEmpty(self):
        print ("returns T if PQ is empty, F if PQ has entries")
        
#       Return a T if PQ is empty, F if PQ is not empty (2 points)
        if len(self.queue) == 0:
            print("T")
        else:
            print("F")
#       
    def size(self):
        print ("returns number of items in queue")
#       Return the number of items in the queue (2 points)
        print("Number of items in queue is " + str(len(self.queue)))
        


#Use a pseudo random number generator to generate 7 different size lists (10 points)    
print ("Create 7 lists of different sizes (10, 50, 500, 1000, 5000, 10000, 50000) to use for testing.")
print ("Use a pseudo random number generator to generate lists (1-50000)")
List_10 = random.sample(range(50000), 10)
List_50 = random.sample(range(50000), 50)
List_500 = random.sample(range(50000), 500)
List_1000 = random.sample(range(50000), 1000)
List_5000 = random.sample(range(50000), 5000)
List_10000 = random.sample(range(50000), 10000)
List_50000 = random.sample(range(50000), 50000)

print ("Then time each module as it uses each list (using time.time) and print")
print ("out results in a table")

#change this code to create lists as described above and time each function
#sampleList = open("sample_queue.txt", "r")

#For each module, start the time, call module, stop time
#LIST 1

start = time.clock()
my_heapPQ = PQ_Heap(List_10) #print first 10 numbers, use size to prove the rest is there
end = time.clock()
l1m1h = end-start
print (l1m1h)

start = time.clock()
my_heapPQ.enQueue(1500)
end = time.clock()
l1m2h = end-start
print (l1m2h)

start = time.clock()
my_heapPQ.deQueue()
end = time.clock()
l1m3h = end-start
print (l1m3h)

start = time.clock()
my_heapPQ.sneakAPeek()
end = time.clock()
l1m4h = end - start
print (l1m4h)

start = time.clock()
my_heapPQ.isEmpty()
end = time.clock()
l1m5h = end-start
print (l1m5h)

start = time.clock()
my_heapPQ.size()
end = time.clock()
l1m6h = end-start
print (l1m6h)



start = time.clock()
my_listPQ = PQ_List(List_10) #print first 10 numbers, use size to prove the rest is there
end = time.clock()
l1m1l = end-start
print (l1m1l)

start = time.clock()
my_listPQ.enQueue(1500)
end = time.clock()
l1m2l = end-start
print (l1m2l)

start = time.clock()
my_listPQ.deQueue()
end = time.clock()
l1m3l = end-start
print (l1m3l)

start = time.clock()
my_listPQ.sneakAPeek()
end = time.clock()
l1m4l = end-start
print (l1m4l)

start = time.clock()
my_listPQ.isEmpty()
end = time.clock()
l1m5l = end-start
print (l1m5l)

start = time.clock()
my_listPQ.size()
end = time.clock()
l1m6l = end-start
print (l1m6l)
print ("end of list 1")


#LIST 2

start = time.clock()
my_heapPQ = PQ_Heap(List_50) #print first 10 numbers, use size to prove the rest is there
end = time.clock()
l2m1h = end-start
print (l2m1h)

start = time.clock()
my_heapPQ.enQueue(1500)
end = time.clock()
l2m2h = end-start
print (l2m2h)

start = time.clock()
my_heapPQ.deQueue()
end = time.clock()
l2m3h = end - start
print (l2m3h)

start = time.clock()
my_heapPQ.sneakAPeek()
end = time.clock()
l2m4h = end-start
print (l2m4h)

start = time.clock()
my_heapPQ.isEmpty()
end = time.clock()
l2m5h = end-start
print (l2m5h)

start = time.clock()
my_heapPQ.size()
end = time.clock()
l2m6h = end-start
print (l2m6h)



start = time.clock()
my_listPQ = PQ_List(List_50) #print first 10 numbers, use size to prove the rest is there
end = time.clock()
l2m1l = end-start
print (l2m1l)

start = time.clock()
my_listPQ.enQueue(1500)
end = time.clock()
l2m2l = end-start
print (l2m2l)

start = time.clock()
my_listPQ.deQueue()
end = time.clock()
l2m3l = end-start
print (l2m3l)

start = time.clock()
my_listPQ.sneakAPeek()
end = time.clock()
l2m4l = end-start
print (l2m4l)

start = time.clock()
my_listPQ.isEmpty()
end = time.clock()
l2m5l = end-start
print (l2m5l)

start = time.clock()
my_listPQ.size()
end = time.clock()
l2m6l = end-start
print (l2m6l)
print ("end of list 2")



#LIST 3

start = time.clock()
my_heapPQ = PQ_Heap(List_500) #print first 10 numbers, use size to prove the rest is there
end = time.clock()
l3m1h = end-start
print (l3m1h)

start = time.clock()
my_heapPQ.enQueue(1500)
end = time.clock()
l3m2h = end-start
print (l3m2h)

start = time.clock()
my_heapPQ.deQueue()
end = time.clock()
l3m3h = end-start
print (l3m3h)

start = time.clock()
my_heapPQ.sneakAPeek()
end = time.clock()
l3m4h = end-start
print (l3m4h)

start = time.clock()
my_heapPQ.isEmpty()
end = time.clock()
l3m5h = end-start
print (l3m5h)

start = time.clock()
my_heapPQ.size()
end = time.clock()
l3m6h = end-start
print (l3m6h)



start = time.clock()
my_listPQ = PQ_List(List_500) #print first 10 numbers, use size to prove the rest is there
end = time.clock()
l3m1l = end-start
print (l3m1l)

start = time.clock()
my_listPQ.enQueue(1500)
end = time.clock()
l3m2l = end-start
print (l3m2l)

start = time.clock()
my_listPQ.deQueue()
end = time.clock()
l3m3l = end-start
print (l3m3l)

start = time.clock()
my_listPQ.sneakAPeek()
end = time.clock()
l3m4l = end-start
print (l3m4l)

start = time.clock()
my_listPQ.isEmpty()
end = time.clock()
l3m5l = end-start
print (l3m5l)

start = time.clock()
my_listPQ.size()
end = time.clock()
l3m6l = end-start
print (l3m6l)
print ("end of list 3")


#LIST 4

start = time.clock()
my_heapPQ = PQ_Heap(List_1000) #print first 10 numbers, use size to prove the rest is there
end = time.clock()
l4m1h = end- start 
print (l4m1h)

start = time.clock()
my_heapPQ.enQueue(1500)
end = time.clock()
l4m2h = end-start
print (l4m2h)

start = time.clock()
my_heapPQ.deQueue()
end = time.clock()
l4m3h = end-start
print (l4m3h)

start = time.clock()
my_heapPQ.sneakAPeek()
end = time.clock()
l4m4h = end-start
print (l4m4h)

start = time.clock()
my_heapPQ.isEmpty()
end = time.clock()
l4m5h = end-start
print (l4m5h)

start = time.clock()
my_heapPQ.size()
end = time.clock()
l4m6h = end-start
print (l4m6h)



start = time.clock()
my_listPQ = PQ_List(List_1000) #print first 10 numbers, use size to prove the rest is there
end = time.clock()
l4m1l = end-start
print (l4m1l)

start = time.clock()
my_listPQ.enQueue(1500)
end = time.clock()
l4m2l = end-start
print (l4m2l)

start = time.clock()
my_listPQ.deQueue()
end = time.clock()
l4m3l = end-start
print (l4m3l)

start = time.clock()
my_listPQ.sneakAPeek()
end = time.clock()
l4m4l = end-start
print (l4m4l)

start = time.clock()
my_listPQ.isEmpty()
end = time.clock()
l4m5l = end-start
print (l4m5l)

start = time.clock()
my_listPQ.size()
end = time.clock()
l4m6l = end-start
print (l4m6l)
print ("end of list 4")


#LIST 5

start = time.clock()
my_heapPQ = PQ_Heap(List_5000) #print first 10 numbers, use size to prove the rest is there
end = time.clock()
l5m1h = end-start
print (l5m1h)

start = time.clock()
my_heapPQ.enQueue(1500)
end = time.clock()
l5m2h = end-start
print (l5m2h)

start = time.clock()
my_heapPQ.deQueue()
end = time.clock()
l5m3h = end-start
print (l5m3h)

start = time.clock()
my_heapPQ.sneakAPeek()
end = time.clock()
l5m4h = end-start
print (l5m4h)

start = time.clock()
my_heapPQ.isEmpty()
end = time.clock()
l5m5h = end-start
print (l5m5h)

start = time.clock()
my_heapPQ.size()
end = time.clock()
l5m6h = end-start
print (l5m6h)



start = time.clock()
my_listPQ = PQ_List(List_5000) #print first 10 numbers, use size to prove the rest is there
end = time.clock()
l5m1l = end-start
print (l5m1l)

start = time.clock()
my_listPQ.enQueue(1500)
end = time.clock()
l5m2l = end-start
print (l5m2l)

start = time.clock()
my_listPQ.deQueue()
end = time.clock()
l5m3l = end-start
print (l5m3l)

start = time.clock()
my_listPQ.sneakAPeek()
end = time.clock()
l5m4l = end-start
print (l5m4l)

start = time.clock()
my_listPQ.isEmpty()
end = time.clock()
l5m5l = end-start
print (l5m5l)

start = time.clock()
my_listPQ.size()
end = time.clock()
l5m6l = end-start
print (l5m6l)
print ("end of list 5")


#LIST 6

start = time.clock()
my_heapPQ = PQ_Heap(List_10000) #print first 10 numbers, use size to prove the rest is there
end = time.clock()
l6m1h = end-start
print (l6m1h)

start = time.clock()
my_heapPQ.enQueue(1500)
end = time.clock()
l6m2h = end-start
print (l6m2h)

start = time.clock()
my_heapPQ.deQueue()
end = time.clock()
l6m3h = end-start
print (l6m3h)

start = time.clock()
my_heapPQ.sneakAPeek()
end = time.clock()
l6m4h = end-start
print (l6m4h)

start = time.clock()
my_heapPQ.isEmpty()
end = time.clock()
l6m5h = end-start
print (l6m5h)

start = time.clock()
my_heapPQ.size()
end = time.clock()
l6m6h = end-start
print (l6m6h)



start = time.clock()
my_listPQ = PQ_List(List_10000) #print first 10 numbers, use size to prove the rest is there
end = time.clock()
l6m1l = end-start
print (l6m1l)

start = time.clock()
my_listPQ.enQueue(1500)
end = time.clock()
l6m2l = end-start
print (l6m2l)

start = time.clock()
my_listPQ.deQueue()
end = time.clock()
l6m3l = end-start
print (l6m3l)

start = time.clock()
my_listPQ.sneakAPeek()
end = time.clock()
l6m4l = end-start
print (l6m4l)

start = time.clock()
my_listPQ.isEmpty()
end = time.clock()
l6m5l = end-start
print (l6m5l)

start = time.clock()
my_listPQ.size()
end = time.clock()
l6m6l = end-start
print (l6m6l)
print ("end of list 6")



#LIST 7

start = time.clock()
my_heapPQ = PQ_Heap(List_50000) #print first 10 numbers, use size to prove the rest is there
end = time.clock()
l7m1h = end-start
print (l7m1h)

start = time.clock()
my_heapPQ.enQueue(1500)
end = time.clock()
l7m2h = end-start
print (l7m2h)

start = time.clock()
my_heapPQ.deQueue()
end = time.clock()
l7m3h = end-start
print (l7m3h)

start = time.clock()
my_heapPQ.sneakAPeek()
end = time.clock()
l7m4h = end-start
print (l7m4h)

start = time.clock()
my_heapPQ.isEmpty()
end = time.clock()
l7m5h = end-start
print (l7m5h)

start = time.clock()
my_heapPQ.size()
end = time.clock()
l7m6h = end-start
print (l7m6h)



start = time.clock()
my_listPQ = PQ_List(List_50000) #print first 10 numbers, use size to prove the rest is there
end = time.clock()
l7m1l = end-start
print (l7m1l)

start = time.clock()
my_listPQ.enQueue(1500)
end = time.clock()
l7m2l = end-start
print (l7m2l)

start = time.clock()
my_listPQ.deQueue()
end = time.clock()
l7m3l = end-start
print (l7m3l)

start = time.clock()
my_listPQ.sneakAPeek()
end = time.clock()
l7m4l = end-start
print (l7m4l)

start = time.clock()
my_listPQ.isEmpty()
end = time.clock()
l7m5l = end-start
print (l7m5l)

start = time.clock()
my_listPQ.size()
end = time.clock()
l7m6l = end-start
print (l7m6l)
print ("end of list 7")

print("\n")
print("\n")
print ("I learned how to make these tables online because i tried to install a table module but I couldn't get it to work. I rounded the seconds to five decimal places for spacing purposes")

#Time each module for each list, and print the results in a table
# (rows - modules, columns - heap, list) (10 points)
print("\n")
print("\n")
print("Table for runtimes of PQ_Heaps")
print ("\n")
print ("\n")
heaps = [['Module', 'List 1', 'List 2', 'List 3', 'List 4', 'List 5', 'List 6', 'List 7'],
         ['Create Heap',("%.5f" % l1m1h),("%.5f" % l2m1h),("%.5f" % l3m1h),("%.5f" % l4m1h),("%.5f" % l5m1h),("%.5f" % l6m1h),("%.5f" % l7m1h)],
         ['enQueue',("%.5f" % l1m2h),("%.5f" % l2m2h),("%.5f" % l3m2h),("%.5f" % l4m2h),("%.5f" % l5m2h),("%.5f" % l6m2h),("%.5f" % l7m2h)],
         ['deQueue',("%.5f" % l1m3h),("%.5f" % l2m3h),("%.5f" % l3m3h),("%.5f" % l4m3h),("%.5f" % l5m3h),("%.5f" % l6m3h),("%.5f" % l7m3h)],
         ['SneakAPeek',("%.5f" % l1m4h),("%.5f" % l2m4h),("%.5f" % l3m4h),("%.5f" % l4m4h),("%.5f" % l5m4h),("%.5f" % l6m4h),("%.5f" % l7m4h)],
         ['IsEmpty',("%.5f" % l1m5h),("%.5f" % l2m5h),("%.5f" % l3m5h),("%.5f" % l4m5h),("%.5f" % l5m5h),("%.5f" % l6m5h),("%.5f" % l7m5h)],
         ['Size',("%.5f" % l1m6h),("%.5f" % l2m6h),("%.5f" % l3m6h),("%.5f" % l4m6h),("%.5f" % l5m6h),("%.5f" % l6m6h),("%.5f" % l7m6h)]]
columnWidth = max(len(str(seconds)) for row in heaps for seconds in row) + 2
for row in heaps:
    print ("".join(str(seconds).center(columnWidth) for seconds in row))

print ("\n")
print ("\n")
print ("\n")

print("Table for runtimes of PQ_Lists")
print ("\n")
print ("\n")




lists = [['Module', 'List 1', 'List 2', 'List 3', 'List 4', 'List 5', 'List 6', 'List 7'],
         ['Create List',("%.5f" % l1m1l),("%.5f" % l2m1l),("%.5f" % l3m1l),("%.5f" % l4m1l),("%.5f" % l5m1l),("%.5f" % l6m1l),("%.5f" % l7m1l)],
         ['enQueue',("%.5f" % l1m2l),("%.5f" % l2m2l),("%.5f" % l3m2l),("%.5f" % l4m2l),("%.5f" % l5m2l),("%.5f" % l6m2l),("%.5f" % l7m2l)],
         ['deQueue',("%.5f" % l1m3l),("%.5f" % l2m3l),("%.5f" % l3m3l),("%.5f" % l4m3l),("%.5f" % l5m3l),("%.5f" % l6m3l),("%.5f" % l7m3l)],
         ['SneakAPeek',("%.5f" % l1m4l),("%.5f" % l2m4l),("%.5f" % l3m4l),("%.5f" % l4m4l),("%.5f" % l5m4l),("%.5f" % l6m4l),("%.5f" % l7m4l)],
         ['IsEmpty',("%.5f" % l1m5l),("%.5f" % l2m5l),("%.5f" % l3m5l),("%.5f" % l4m5l),("%.5f" % l5m5l),("%.5f" % l6m5l),("%.5f" % l7m5l)],
         ['Size',("%.5f" % l1m6l),("%.5f" % l2m6l),("%.5f" % l3m6l),("%.5f" % l4m6l),("%.5f" % l5m6l),("%.5f" % l6m6l),("%.5f" % l7m6l)]]
columnWidth = max(len(str(seconds)) for row in lists for seconds in row) + 2
for row in lists:
    print ("".join(str(seconds).center(columnWidth) for seconds in row))

#   Once you have your classes working, you will use your PQ_Heap class and PQ_List class
#   to create and compare a rudimentary job scheduler.  
#          1) create a file named sample_queue.txt with 10 random numbers (by hand)
#             we will create our own txt file to test your code.
#          2) Your 2 job schedulers will do the following:
#               start time
#               enqueue the jobs one at a time 
#               loop until all jobs are complete
#                  looks at top of queue and print it out (doesn't delete)
#                  Removes 1 job from the queue 
#               stop time


#Time both your schedulers and print out results for each here (5 points)


print ("\n")
print ("\n")
print ("\n")
print ("\n")
newsampleList = open("sample_queue.txt", "r")
u = newsampleList.read().split(',')
jobsched1 = PQ_Heap(u)
start = time.clock()
for x in newsampleList:
    jobsched1.enQueue(x)
while len(u) > 0:
    print(u[0])
    del(u[0])
end = time.clock()
m10dqh = end-start
print(m10dqh)

print ("\n")
print ("\n")

newList_50 = open("sample_queue.txt", "r")
i = newList_50.read().split(',')
jobsched2 = PQ_List(i)
start = time.clock()
for x in newList_50:
    jobsched2.enQueue(x)
while len(i) > 0:
    print(i[0])
    del(i[0])
end = time.clock()
m10dql = end-start
print(m10dql)

print ("\n")
print ("\n")
print ("\n")
print ("Job Scheduler #1")
print ("\n")

myheap = [['Module', 'Sample Queue PQ_Heap'],
         ['enQueue/Look at top/Remove',("%.5f" % m10dqh)]]
columnWidth = max(len(str(seconds)) for row in myheap for seconds in row) + 2 
for row in myheap:
    print ("".join(str(seconds).center(columnWidth) for seconds in row))

print ("\n")
print ("\n")
print ("\n")
print ("Job Scheduler #2")
print ("\n")

mylist = [['Module', 'Sample Queue PQ_List'],
         ['enQueue/Look at top/Remove',("%.5f" % m10dql)]]
columnWidth = max(len(str(seconds)) for row in mylist for seconds in row) + 2
for row in mylist:
    print ("".join(str(seconds).center(columnWidth) for seconds in row))

print ("\n")
print ("\n")
print ("\n")
#Once you have your time trials complete, create a table that lists each module (rows)
#and time efficiency for worst case (Big O) and print here. (10 points)
print ("Time Effiency Table for PQ_Heap")
print ("\n")
timeEffTable = [['Module', 'Time Efficiency for Worse Case (Big O)'],
          ['enQueue','O(logn)'],
          ['deQueue','O(logn)'],
          ['SneakAPeek','O(1)'],
          ['IsEmpty','O(n)'],
          ['Size','O(n)']]
columnWidth = max(len(str(timeEff)) for row in timeEffTable for timeEff in row) + 2 
for row in timeEffTable:
    print ("".join(str(timeEff).center(columnWidth) for timeEff in row))

print ("\n")
print ("\n")
print ("\n")
print ("Time Effiency Table for PQ_List")
print ("\n")
timeEffTable2 = [['Module', 'Time Efficiency for Worse Case (Big O)'],
          ['enQueue','O(1)'],
          ['deQueue','O(1)'],
          ['SneakAPeek','O(n)'],
          ['IsEmpty','O(n)'],
          ['Size','O(n)']]
columnWidth = max(len(str(timeEff)) for row in timeEffTable2 for timeEff in row) + 2 
for row in timeEffTable2:
    print ("".join(str(timeEff).center(columnWidth) for timeEff in row))

	
input('enter to close')
