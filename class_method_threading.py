from threading import Thread , current_thread
class Example:
    @classmethod
    def display(self,n,msg):
         for i in range(n):
             print("Hello ")
e1 = Example()
t1 = Thread(target =Example.display, args =(5, 'Hello'))
t1.start()
             
for i in range(5):
    print("welcome")