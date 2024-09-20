import multiprocessing
import os,time
def print_numbers():
    pid = os.getpid()
    for i in range(5):
        print(f'{i}@{pid}')
        time.sleep(0.25)

if __name__ == '__main__':
    processes=[]
    for i in range(5):
        process = multiprocessing.Process(target=print_numbers)
        processes.append(process)
        process.start()
    #for i in range(5):
     #   processes[i].join()
    print_numbers()