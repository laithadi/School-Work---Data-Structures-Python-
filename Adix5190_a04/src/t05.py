''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-02-10 
...................................................
'''

from Queue_circular import Queue
fh = open("movies.txt", "r")
a = fh.readlines() 
q = Queue(2)
print('Check if Queue is empty')
print(q.is_empty())
print('Insert into Queue. Peek at Queue, check is empty')
q.insert(a[1])
print(q.peek())
print(q.is_empty())
print('Fill Queue, check if queue is full')
q.insert(a[2])
print(q.is_full())
print('Remove from Queue, check is empty and, Queue is full')
q.remove()
q.remove()
print(q.is_empty())
print(q.is_full())
fh.close()
