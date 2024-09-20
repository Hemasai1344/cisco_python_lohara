"""
import threading
import time
def print_numbers():
    for i in range(1000):
        print(i)
        time.sleep(0.25)

thread1 = threading.Thread(target=print_numbers)
#thread2 = threading.Thread(target=print_numbers)
thread1.start()  # Start the thread
#thread1.join()   # Wait for the thread to finish
#print()  
#thread2.start()
#thread2.join()
print_numbers()
"""

import time
import threading

def print_numbers():
    id = threading.get_ident()
    for i in range(5):
        print(f'{i}@{id}')
        #time.sleep(0.25)

threads = []
for i in range(5):
    thread = threading.Thread(target=print_numbers)
    threads.append(thread)
    thread.start()

for i in range(5):
    thread.join()

print_numbers()