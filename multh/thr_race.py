import threading

# Create a lock
lock = threading.Lock()

# Global variable to be incremented
total = 0

# Function to be executed by each thread
def print_numbers():
    global total
    thread_id = threading.get_ident()
    for i in range(1, 500000 + 1):
        with lock:
            total += 1

# List to hold the thread objects
threads = []

# Create and start 5 threads
for i in range(5):
    thread = threading.Thread(target=print_numbers)
    threads.append(thread)
    thread.start()

# Immediately print the final value of total without waiting for threads to complete
print(f"Final total (without join): {total}")