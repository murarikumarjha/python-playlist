from time import sleep
from threading import Thread 
video = ['oop syllabus', 'constructor','destructor','file handling']

class Myclass(Thread):
  def __init__(self):
    print("constructor called")
    Thread.__init__(self)
  def run(self):
    for vid in video:
      print(f"{vid} started uploding...")
      sleep(3)
      print(f"{vid} uploaded.")
t1 = Myclass()
t1.start()
  
for i in range(4):
  sleep(0.5)
  print("checking copyright")