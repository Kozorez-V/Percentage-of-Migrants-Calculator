def check_type(function):
    def wrapper(*arguments):
        if isinstance(function(*arguments), dict) == False:
            print("It's not dictionary")
            exit()
        return function(*arguments)
    return wrapper
