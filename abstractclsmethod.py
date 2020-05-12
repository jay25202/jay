from abc import ABC,abstractmethod

class computer(ABC):
    @abstractmethod
    def process(self):
        pass

class laptop(computer):
    def process(self):
        print("its running")

class whiteboard(laptop):
    def write(self):
        print("its writing")

class programmer:
    def work(self,com):
        print("solving bug")
        com.process


lap = laptop()
lap.process()
com1=whiteboard()

#com = computer()
#com.process()
prog1= programmer()
prog1.work(com1)