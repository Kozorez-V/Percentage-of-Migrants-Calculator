def check(function):
    def wrapper(argument):
        if not isinstance(function(argument), dict):
            return {
                "success": False,
                "message": "It isn't dictionary"
            }
    return wrapper

