# __author__ = 'alexlyman'

def get_info(message):
    try:
        user_input = str(raw_input(message))
        if user_input is.digit() and user_input is not 0:
            return user_input
        elif user_input == 0
            print "You can't enter 0"
        return None
    except NameError:
        print "You must enter a digit"
    return None