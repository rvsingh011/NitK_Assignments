from datetime import datetime
import threading
from threading import Thread


class Database(object):
    x = {"timestamp": datetime.now(), "value": 5}
    y = {"timestamp": datetime.now(), "value": 10}
    z = {"timestamp": datetime.now(), "value": 30}

    def commit(self):
        lock = threading.Lock()
        lock.acquire()
        
        for variable in self.variable_used:
            if variable == "x":
                self.x['timestamp'] == Database.x['timestamp']
                print(Database.x)
                Database.x = dict(self.x)
            if variable == "y":
                self.y['timestamp'] == Database.y['timestamp']
                Database.y = dict(self.y)
            if variable == "z":
                self.z['timestamp'] == Database.z['timestamp']
                Database.z = dict(self.z)
                
        lock.release()


class Child(Database):

    def __init__(self):
        self.variable_used = ['x']

    def parse(self, transaction):
        operations = transaction.split(" ")
        for individual_operation in operations:
            operation, item = individual_operation.split(',')
            if operation == 'r':
                self.read(item)
            if operation == 'w':
                self.write(item)
            if operation == "c":
                self.commit()

    def read(self, item):
        pass

    def write(self, item):
        if item == "x":
            self.x['timestamp'] = Database.x['timestamp'] = datetime.now()
        elif item == "y":
            self.y['timestamp'] = Database.y['timestamp'] = datetime.now()
        elif item == "z":
            self.z['timestamp'] = Database.z['timestamp'] = datetime.now()

    def commit(self):
        super(Child, self).commit()

if __name__ == "__main__":
    str1 = "r,x r,y r,z"
    str2 = "r,x w,z r,z"
    x = Thread(target=Child().parse, args=(str1,)).start()
    y = Thread(target=Child().parse, args=(str2,)).start()

