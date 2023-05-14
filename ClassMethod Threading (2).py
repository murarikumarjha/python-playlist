# HOW TO CREATE THREAD FOR classmethod 
from threading import Thread
class Example:
  @classmethod
  def display(self,n):
    for i in range(n):
      print("Hello World!")
      
e1 = Example()
t1 = Thread(target = Example.display,args =(5,))
t1.start()
for i in range(5):
  print('welcome:')