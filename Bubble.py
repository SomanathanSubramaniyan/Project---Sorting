#Author : Somu   Date: 01st April 2019
#Bubble Sort
#Bubble sort has a worst-case and average complexity of О(n2)
#The complexity of bubble sort is in both worst and average cases, because the entire array needs to be
# iterated for every element
#REference :: https://www.cs.cmu.edu/~adamchik/15-121/lectures/Sorting%20Algorithms/sorting.html

from datetime import datetime
import time
import random
start_time = time.time()

datai =[]

def bubble_sort (data):
    Ocount, icount = 0,0
    while (Ocount <= len(data) -1):
        Ocount = Ocount + 1
        if len(data) > 1:
            for i in range(0, len(data)-1):
                icount = icount+1
                x = data[i]
                y = data[i+1]
                if x > y:
                    data[i+1] = x
                    data[i] =y
    return(data,Ocount,icount)


def generate_data(count):
    s=0
    while (s<count):
        #datai.append(random.randint(1,10))
        datai = random.randint(1,10)
        print(datai)
        s = s+1
    return datai        


data_input=generate_data(20)
result, Ocount,icount  = bubble_sort(data_input)

print ("Input data elements to the Bubble Sort Function: "+str(data_input))
print ("Output of the Bubble Sort Function             : "+str(result))
print ("Size of the input data elements : " + str(len(datai)))
print ("Number of Outer loop counts     : " + str(Ocount))
print ("Number of inner loop counts     : " + str(icount))
print ("Total Loop counts               : " + str(Ocount+icount))
print ("Execution Time --- %s seconds ---" % (time.time() - start_time))

##def function_int(x):
##    for i in x:
##        liste.append(int[i])
##    return liste


        

            
                
        

        
        
