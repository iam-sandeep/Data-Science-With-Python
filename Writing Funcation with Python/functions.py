'''
Building a command line data app
You are building a command line tool that lets a user interactively
 explore a data set. We've defined four functions: mean(), std(), minimum(), 
 and maximum() that users can call to analyze 
their data. Help finish this section of the code so that your users can call 
any of these functions by typing the function name at the input prompt.

Note: The function get_user_input() in this exercise is a mock version of 
asking the user to enter a command. It randomly returns one of the four function names. 
In real life, you would ask for input and wait until the user entered a value.



'''
# Add the missing function references to the function map
function_map = {
  'mean': mean,
  'std': std,
  'minimum': minimum,
  'maximum': maximum
}

data = load_data()
print(data)

func_name = get_user_input()

# Call the chosen function and pass "data" as an argument
function_map[func_name](data)



'''
Defining a decorator
Your buddy has been working on a decorator that prints a "before" message before the decorated function is called and prints an "after" message after the decorated function is called. They are having trouble remembering how wrapping the decorated function is supposed to work. Help them out by finishing their print_before_and_after() decorator.

'''

def print_before_and_after(func):
      def wrapper(*args):
    print('Before {}'.format(func.__name__))
    # Call the function being decorated with *args
    func(*args)
    print('After {}'.format(func.__name__))
  # Return the nested function
  return wrapper

@print_before_and_after
def multiply(a, b):
  print(a * b)

multiply(5, 10)