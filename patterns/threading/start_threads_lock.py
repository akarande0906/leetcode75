import threading 
import time

lock = threading.Lock()

class Threader:
    def print_cube(num):
        global lock
        lock.acquire()
        time.sleep(100)
        print("Cube: {}" .format(num * num * num))
        print(threading.current_thread().name)
        lock.release()

    def print_square(num):
        print("Square: {}" .format(num * num))
        print(threading.current_thread().name)


if __name__ =="__main__":
    t1 = threading.Thread(target=Threader.print_square, args=(10,))
    t2 = threading.Thread(target=Threader.print_square, args=(10,))

    t1.start() # Start thread
    t2.start()

    t1.join()  # Wait for thread to complete
    t2.join()

    print("Done!")
