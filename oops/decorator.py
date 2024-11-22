def my_decorator(func):
    def wrapper():
        if func:
            print (f'Running {func.__name__}')
            func()
    return wrapper


# Will invoke the decorator in this function
@my_decorator
def do_this():
    print ('Doing this!')

# Will invoke the decorator in this function
@my_decorator
def do_that():
    print ('Doing that!')

match input('What shall I do? '): # Matches user input with the case (switch-case)
    case 'this':
        do_this()
    case 'that':
        do_that()
    case _: # Default
        print ('Not programmed for this!')
