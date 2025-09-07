import threading 
def print_cube(num):
    print("Cube: {}" .format(num * num * num))
    print(threading.current_thread().name)


def print_square(num):
    print("Square: {}" .format(num * num))
    print(threading.current_thread().name)


if __name__ =="__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    t1.start() # Start thread
    t2.start()

    t1.join()  # Wait for thread to complete
    t2.join()

    print("Done!")
