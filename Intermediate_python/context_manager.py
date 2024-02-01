# with open('notes.txt','w') as file:#this more clean
#     file.write('some to doo...')

# # or
    
# file = open('notes.txt','w')
# try:
#     file.write('some to doo...')
# finally:
#     file.close()



# from threading import Lock
# lock = Lock()

# lock.aquire()

# lock.release()

# with lock:


# __enter__ and __exit__ methods are also called as context manager special methods in python. You may come up with the question "what is a context manager ?". A context manager is a manager which has the ability to make avail the data withing the context or within a block of code and destroy it when it is used.


# context_manager based on a class method


# class ManagedFile:
#     def __init__(self,filename):
#         self.filename = filename
#     def __enter__(self):
#         print('enter')
#         self.file = open(self.filename,'w')
#         return self.file
#     def __exit__(self,exc_type,exc_value,exc_traceback):
#         if self.file:
#             self.file.close()
#         print('exit')

# with ManagedFile('notessample.txt') as file:
#     print('do some stuff....')
#     file.write('some todoo...')





# class ManagedFile:
#     def __init__(self,filename):
#         self.filename = filename
#     def __enter__(self):
#         print('enter')
#         self.file = open(self.filename,'w')
#         return self.file
#     def __exit__(self,exc_type,exc_value,exc_traceback):
#         if self.file:
#             self.file.close()
#         if exc_type is not None:
#             print('exception has been handled')
#         # print('exc:',exc_type,exc_value)#exc means exceptions occuring.This is for exception handling.
#         print('exit')
#         return True

# with ManagedFile('notessample.txt') as file:
#     print('do some stuff....')
#     file.write('some todoo...')
#     file.some()

# print('continuing')



# from contextlib import contextmanager

# @contextmanager
# def open_managed_file(filename):
#     f = open(filename,'w')#try part is same as  __enter__ method in class
#     try:
#         yield f 
#     finally:
#         f.close

# with open_managed_file('notefun.txt') as f:
#     f.write('some to doo')




