#!/usr/bin/env python3
import multiprocessing as mp
source_list = [1,2,3,4,5]
jobs = []
# This is the initialization of the multiprocessing library Queue object.
q = mp.Queue()
squared_list = []

def squares(num,q):
# Here the child process squares the number and puts it onto the queue. 
    q.put(num * num)

if __name__ == '__main__':
    
    for num in source_list:
# Here we pass the queue object as a parameter into our function.
        p = mp.Process(target=squares,args=(num,q))
        jobs.append(p)
        p.start()
    
    for job in jobs:
        job.join()

# Now get the items off the queue and put them into a list. 
    while not q.empty():
        squared_list.append(q.get())
        
# Finally, print the sorted list.      
    print (sorted(squared_list))
