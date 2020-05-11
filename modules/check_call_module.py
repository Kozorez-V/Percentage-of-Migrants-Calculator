def check(function):
    def wrapper(argument):
        if isinstance(function(argument), dict):
            return {
                "success": True,
                "message": "All right"
            }
    return wrapper
