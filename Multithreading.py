# THREAD

# Thread is a functionality of logics which executes simultaneously along with the other part of the program.
# Thread is a lightweight process, the smallest unit of processing.

# PROCESS

# A program which is under execution is called a process.
# We can define functionality of logic as a thread by overriding the run method of the thread class.
# Thread class is a predefined class which is defined in threading model.
# Threads can be executed group through start() method of thread class.

# import threading
# class x(threading.Thread):
#     def run(self):
#         for i in range(1,101):
#             print(i)
# class y(threading.Thread):
#     def run(self):
#         for i in range(101,201):
#             print(i)
# t1 = x()
# t2 = y()
# t1.start()
# t2.start()
# for j in range(201,301):
#     print(j)

# SCHEDULING

# Among multiple threads, which thread will get the chance first is decided by the scheduler.
# Scheduling is based on scheduling algorithm, and every OS is following dynamic scheduling algorithm.
# So that, the scheduling is hightly dynamic and unpredictable.
# For every thread, one name is assigned to thread class

# THREAD NAME

# Python interpreter assigns one unique name to each and every thread.
# We can get the name of the thread by using getName() method of thread class.
# We can also assign our own name to the thread by using setName() method of thread class.

# import threading
# class x(threading.Thread):
#     def run(self):
#         print(self.getName())
# class y(threading.Thread):
#     def run(self):
#         print(self.getName())
# t1 = x()
# t2 = y()
# t1.setName('Smit')
# t2.setName('Anjali')
# t1.start()
# t2.start()

# SUSPENDING THE EXECUTION OF THREAD

# We can suspend the execution of thread by using sleep() method or join() method of time module.
# sleep() method is used to suspend the execution of current thread for a specific time. It is defined in time module.
# join() method is used to suspend the execution of current thread until the completion of another thread. It is defined in thread class.

# import time
# for p in range(1,6):
#     print(p)
#     time.sleep(2)

# import time
# import threading
# class x(threading.Thread):
#     def run(self):
#         time.sleep(10)
#         for p in range(1,11):
#             print("RAMA RAMA")
# class y(threading.Thread):
#     def run(self):
#         for p in range(1,6):
#             print("JAI SIYA RAAM")
# t1=x()
# t2=y()
# t1.start()
# t2.start()

# import time
# import threading
# class x(threading.Thread):
#     def run(self):
#         time.sleep(5)
#         for p in range(1,101):
#             print(p)
# class y(threading.Thread):
#     def run(self):
#         for p in range(101,201):
#             print(p)
# t1=x()
# t2=y()
# t1.start()
# t2.start()

# import time
# import threading
# class x(threading.Thread):
#     def run(self):
#         for p in range(1,6):
#             print("JAI SIYA RAM")
#             time.sleep(2)
# t1=x()
# t1.start()
# t1.join(5)
# for p in range(1,6):
#     print("RAMA RAMA")

# import time
# import threading
# class x(threading.Thread):
#     def run(self):
#         s=0
#         time.sleep(5)
#         for p in range(1,100):
#             s+=p
#         print(s)
# t1=x()
# t1.start()
# for p in range(101,201):
#     print(p)
#     if p==150:
#         t1.join()