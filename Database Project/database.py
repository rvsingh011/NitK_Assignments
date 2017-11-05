from datetime import datetime
import threading
from threading import Thread
import time


class Database(object):
    x = {"timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "value": 5}
    y = {"timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "value": 10}
    z = {"timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "value": 30}

    @staticmethod
    def commit(item_x, item_y, item_z, variable_used):
        lock = threading.Lock()
        lock.acquire()
        count = 0
        for variable in variable_used:
            if variable == "x":
                if item_x['timestamp'] == Database.x['timestamp']:
                    Database.x['timestamp'] = item_x['timestamp']
                    count += 1
            if variable == "y":
                if item_y['timestamp'] == Database.y['timestamp']:
                    Database.y['timestamp'] = item_y['timestamp']
                    count += 1
            if variable == "z":
                if item_z['timestamp'] == Database.z['timestamp']:
                    Database.z['timestamp'] = item_z['timestamp']
                    count += 1

            if len(variable_used) == count:
                lock.release()
                return 1
            else:
                lock.release()
                return 0


class Child:

    def __init__(self):
        self.variable_used = []
        self.database = Database()
        self.x = dict(self.database.x)
        self.y = dict(self.database.y)
        self.z = dict(self.database.z)

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
        count = 1
        if item == "x":
            self.variable_used.append("x")
            self.x['timestamp'] = self.database.x['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        elif item == "y":
            if count == 1:
                count += 1
                time.sleep(5)
            self.variable_used.append("y")
            self.y['timestamp'] = self.database.y['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        elif item == "z":
            self.variable_used.append("z")
            self.z['timestamp'] = self.database.z['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def commit(self):
        status = self.database.commit(self.x, self.y, self.z, self.variable_used)
        if status == 1:
            print("transaction successful")
        elif status == 0:
            print("Transaction Unsuccessful")


if __name__ == "__main__":
    str1 = "w,z w,y r,z c,end"
    str2 = "r,x w,z r,z c,end"
    x = Thread(target=Child().parse, args=(str1,)).start()
    y = Thread(target=Child().parse, args=(str2,)).start()

