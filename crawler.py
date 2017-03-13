import queue
import threading
from timeit import default_timer
import time

start  = default_timer()
threadlock = threading.Lock()
q = queue.Queue()

for i in range(0,500000):
    q.put(i)


class crawler(threading.Thread):
    def __init__(self,ThreadID,name):
        threading.Thread.__init__(self)
        self.ThreadID = ThreadID
        self.name = name
    def run(self):
        try:
          while q.empty() != True:
             print(q.get_nowait())
        except queue.Empty:
            return



threads = []
for i in range(0,90):
    thread = crawler("naam"+str(i),1)
    thread.start()
    threads.append(thread)


for i in threads:
    i.join()
print(default_timer() - start)




