'''
The timer() context manager
A colleague of yours is working on a web service that processes Instagram photos. 
Customers are complaining that the service takes too long to identify whether or not an
 image has a cat in it, so your colleague has come to you for help. You decide to write a 
context manager that they can use to time how long their functions take to run.

'''
# Add a decorator that will make timer() a context manager
@contextlib.contextmanager
def timer():
  """Time the execution of a context block.

  Yields:
    None
  """
  start = time.time()
  # Send control back to the context block
  yield
  end = time.time()
  print('Elapsed: {:.2f}s'.format(end - start))

with timer():
  print('This should take approximately 0.25 seconds')
  time.sleep(0.25)


  '''
  A read-only open() context manager
You have a bunch of data files for your next deep learning project that took you months to collect and clean. It would be terrible if you accidentally overwrote one of those files when trying to read it in for training, so you decide to create a read-only version of the open() context manager to use in your project.

The regular open() context manager:

takes a filename and a mode ('r' for read, 'w' for write, or 'a' for append)
opens the file for reading, writing, or appending
yields control back to the context, along with a reference to the file
waits for the context to finish
and then closes the file before exiting
Your context manager will do the same thing, except it will only take the filename as an argument and it will only open the file for reading.

  '''
@contextlib.contextmanager
def open_read_only(filename):
  """Open a file in read-only mode.

  Args:
    filename (str): The location of the file to read

  Yields:
    file object
  """
  read_only_file = open(filename, mode='r')
  # Yield read_only_file so it can be assigned to my_file
  yield read_only_file
  # Close read_only_file
  read_only_file.close()

with open_read_only('my_file.txt') as my_file:
  print(my_file.read())