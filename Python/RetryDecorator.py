#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Challenge: Decorator with Arguments
# Write a decorator @retry that retries a function up to n times if it raises an exception. It should take n as an argument.
# Example:
# @retry(3)
# def unstable_function():
#     # Raises an error randomly
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def retry(x):
    def deco(func):
        def wrap(*args):
            i = 0
            retval = None
            while i < x:
                try:
                    retval = func()
                except Exception as e:
                    i += 1
                    print(f"Attempt {i}/{x} -- Exception Occurred: '{e}'")
                else:
                    return retval
            raise Exception('Maximum retries exceeded')
        return wrap
    return deco

@retry(3)
def dz():
    t = 1/0

dz()
