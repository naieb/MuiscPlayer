import queue

# is Queue of a maximum   capacity of 1000
q = queue.Queue(maxsize=1000)

def put(items):
    q.put(items)

def get():
    return(q.get())

def isempty():
    return(q.empty())

def isfull():
    return(q.full())   

def size():
    return(q.qsize())    