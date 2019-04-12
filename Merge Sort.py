#Author : Somu   Date: 01st April 2019
#Merge Sort


from datetime import datetime
import time
start_time = time.time()

def MG_split (data):
    if len(data)> 3 :
        midpoint = int((len(data))/2) - 1
        MG1 = data[0: midpoint+1]
        MG2 = data[midpoint+1 :len(data)]
    return (MG1,MG2)

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


data=[8,7,6,5]
MG1,MG2 = MG_split(data)

datai = MG1
x = str(MG1)
print(str(MG1))
result, Ocount,icount  = bubble_sort(datai)
print(str(x))
print ("Input data elements to the Bubble Sort Function: "+str(x))
print ("Output of the Bubble Sort Function             : "+str(datai))
print ("Size of the input data elements : " + str(len(datai)))
print ("Number of Outer loop counts     : " + str(Ocount))
print ("Number of inner loop counts     : " + str(icount))
print ("Total Loop counts               : " + str(Ocount+icount))
print ("Execution Time --- %s seconds ---" % (time.time() - start_time))
        

            
                
        

        
        
