# from threading import Thread,Lock
# import os
# import time

# database_value = 0


# def increase():
#     global database_value
#     lock.acquire()
#     local_copy = database_value
#     #processing

#     local_copy += 1
#     time.sleep(0.1)
#     database_value = local_copy
#     lock.release()




# if __name__ == "__main__":
#     lock =Lock()
#     print('start value',database_value)
#     thread1 = Thread(target=increase,args =(lock,))
#     thread2 = Thread(target=increase,args =(lock,))

#     thread1.start()
#     thread2.start()

#     thread1.join()
#     thread2.join()

#     print('end value',database_value)

#     print('end main')




# from threading import Thread,Lock
# import time

# database_value = 0


# def increase(lock):
#     global database_value
#     with lock:
#         lock.acquire()
#         local_copy = database_value
#         #processing

#         local_copy += 1
#         time.sleep(0.1)
#         database_value = local_copy
#         lock.release()




# if __name__ == "__main__":
#     lock =Lock()
#     print('start value',database_value)
#     thread1 = Thread(target=increase,args =(lock,))
#     thread2 = Thread(target=increase,args =(lock,))

#     thread1.start()
#     thread2.start()

#     thread1.join()
#     thread2.join()

#     print('end value',database_value)

#     print('end main')


# from threading import Thread,Lock
# import time
# from queue import Queue


# if __name__ == "__main__":
#     q = Queue()
#     q.put(1)
#     q.put(2)
#     q.put(3)
#     first = q.get()
#     print(first)
#     q.task_done()
#     q.join()
#     print('end point')



# from threading import Thread,Lock,current_thread
# import time
# from queue import Queue


# def worker():
#     while True:
#         value = q.get()
#         #processing..
#         print(f'in {current_thread().name} got {value}')




# if __name__ == "__main__":
#     q = Queue()
#     num_threads = 10
#     for i in range(num_threads):
#         thread =Thread(target=worker,args=(q,))
#         thread.daemon=True
#         thread.start()

#     for i in range(1,21):
#         q.put(i)

#     q.join()

#     print('end main')





