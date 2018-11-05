# THE DECORATOR IDEA IS TO ADD NEW FUNCTIONALITY (NEW CODE)
# TO AN EXISTING FUNCTION (WERAPP THE EXISTING FUNCTION WITH NEW CODE)
# IN A WAY THAT IT WOULD BE EASY TO ADD/REMOVE THIS ADDITONAL FUNCTIONALITY/CODE

def decorator1(func):

    def wrap_function():
        # some code before the original function.
        print ("some code before decorated function...")

        # the original function
        func()

        # some code after the original function
        print ("some code after decorated function")

    # now we return the newly decorated functon = function with added code
    return wrap_function

# THIS IS WHAT DECORATORS DO IN ESSENSE - WRAPP EXISTING FUNCTION WITH NEW CODE

# SEE THE EXAMPLE OF APPLYING OUR DECORATOR TO A FUNCTION:

# ONE WAY OF ADDING CODE = DECORATING:
def function_that_needs_decorator():
    print ("I need more code, please decorate me")

function_that_needs_decorator = decorator1(function_that_needs_decorator)

function_that_needs_decorator()

# A BETTER WAY OF DECORATING:
@decorator1
def function_that_needs_decorator():
    print ("I need more code, please decorate me")

function_that_needs_decorator()
