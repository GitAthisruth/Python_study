# Process: An instance of a program (e.g a Python interpreter)

# 1. Takes advantage of multiple CPUs and cores.
# 2. Seperate memory space -> Memory is not shared between processes.
# 3. Great for CPU-bound processing.
# 4. New process is stated independently from other processes.
# 5. Processes are interruptable/killable
# 6. One GIL(Global Interpreter Lock) for each process --> avoids GIL limitation.

# Global Interpreter Lock

# It is a mechanism in Python that allows only one thread to execute at a time in the interpreter.
# This lock is essential for memory safety in multi-threaded Python programs.

# disadvantages

# - Heavyweight -takes  alot of memory 
# - Starting a process is slower than starting a thread.
# - More memory
# - IPC (inter-process communication) is more complicated.


# Threads:AN entity within a process that can be scheduled (also known as "lightweight process")
# A process can spawn multiple threads.

# 1. All threads within a process share the same memory.
# 2. lightweight.
# 3. Starting a thread is faster than starting a process.
# 4. Great for I/O-bound tasks.

# # disadvantages    

# - Threading is limited by GIL: only one thread at a time.
# - No effect for CPU-bound tasks.
# - Not interruptable/killable.
# - Careful with race conditions(two or more thread to modify same variable at same time).  




# Global Interpreter Lock

# It is a mechanism in Python that allows only one thread to execute at a time in the interpreter.
# This lock is essential for memory safety in multi-threaded Python programs.

# Needed in CPython because memory management is not thread-safe.

# Avoid:
    # 1. Use multiprocessing
    # 2. Use a different, free-threaded Python implementation (Jython, IronPython)
    # 3. Use Python as a wrapper for third-party libraries (C/C++) -> numpy,scipy


#processes

# from multiprocessing import Process
# import os
# import time

# def square_numbers():
#     for i in range(100):
#         i = i
#         time.sleep(0.1)

# processes = []

# num_process = os.cpu_count()

# #create processes

# for i in range(num_process):
#     p = Process(target=square_numbers)
#     processes.append(p)

# #start
    
# for p in processes:
#     p.start()

# #join 
    
# for p in processes:
#     p.join()

# print('end main')



# from threading import Thread
# import os
# import time

# def square_numbers():
#     for i in range(100):
#         i = i
#         time.sleep(0.1)

# threads = []

# num_threads = os.cpu_count()

# #create processes

# for i in range(num_threads):
#     t = Thread(target=square_numbers)
#     threads.append(t)

# #start
    
# for t in threads:
#     t.start()

# #join 
    
# for t in threads:
#     t.join()

# print('end main')