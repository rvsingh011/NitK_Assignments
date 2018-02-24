from datetime import datetime
import threading
from threading import Thread
import time


class Database(object):
    """
    This class Simulate the behaviour of a real Disk Database.
    It has following class variables -
    x, y, z (representing 3 data items)
    It has the following methods -
    commit() - Simulate the behaviour of Database commit operation.
    """

    x = {
        "read_timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], "value": 5,
        "write_timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    }
    y = {
        "read_timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], "value": 10,
        "write_timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    }
    z = {
        "read_timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], "value": 30,
        "write_timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    }

    @staticmethod
    def commit(item_x, item_y, item_z, variable_used):
        """Simulate the Real Database commit Operation"""
        
        lock = threading.Lock()  # Make lock object

        # Not locking Individual Item as shown in error_case because restarting a atmost complete
        # transaction is more costlier than stoping a transaction for few seconds
        # Acquire Lock
        lock.acquire()
        # Count variables are
        count = 0
        for variable in variable_used:
            if variable == "x":
                if item_x['write_timestamp'] == Database.x['write_timestamp']:
                    Database.x['write_timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                    count += 1
            if variable == "y":
                if item_y['write_timestamp'] == Database.y['write_timestamp']:
                    Database.y['write_timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                    count += 1
            if variable == "z":
                if item_z['write_timestamp'] == Database.z['write_timestamp']:
                    Database.z['write_timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                    count += 1
        # Does Every comparision is done successful way.
        if len(variable_used) == count:
            lock.release()
            return 1
        else:
            lock.release()
            return 0


class Client:
    """
    This class has simulate the real behaviour of client side
    It contain the following methods -
    __init__ : Initialization function for the class
    parse : This method parse the transition parsed as string.
    commit : Local commit operation on client side.
    write : Local write operation on Client side
    read : Local read operation on client Side
    """

    def __init__(self, time_stamp):
        """The Initialization function of this class. """
        self.variable_used = []
        self.database = Database()
        self.time_stamp = time_stamp
        self.x = dict(self.database.x)
        self.y = dict(self.database.y)
        self.z = dict(self.database.z)

    def parse(self, transaction):
        """This function parse the transaction passed as string"""
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
        """This function simulate the read operation on client side. """
        if item == "x":
            self.x['read_timestamp'] = self.database.x['read_timestamp'] = self.time_stamp
        elif item == "y":
            self.y['read_timestamp'] = self.database.y['read_timestamp'] = self.time_stamp
        elif item == "z":
            self.z['read_timestamp'] = self.database.z['read_timestamp'] = self.time_stamp

    def write(self, item):
        """This function simulate the write operation on client side. """
        count = 1
        if item == "x":
            self.variable_used.append("x")
            self.x['write_timestamp'] = self.database.x['write_timestamp'] = self.time_stamp
        elif item == "y":
            # Stop First client and simulate a network delay
            if count == 1:
                count += 1
                print(threading.current_thread().getName())
                time.sleep(5)
            self.variable_used.append("y")
            self.y['write_timestamp'] = self.database.y['write_timestamp'] = self.time_stamp
        elif item == "z":
            self.variable_used.append("z")
            self.z['write_timestamp'] = self.database.z['write_timestamp'] = self.time_stamp

    def commit(self):
        """This function simulate client commit operation."""
        status = self.database.commit(self.x, self.y, self.z, self.variable_used)
        if status == 1:
            print(threading.current_thread().getName() + " Transaction successful")
        elif status == 0:
            print(threading.current_thread().getName() + " Transaction Unsuccessful")


if __name__ == "__main__":
    """The main Method"""
    # First Transaction in string form.
    str1 = "w,z w,y r,z c,end"
    # Second Transaction in String form.
    str2 = "r,x w,z r,z c,end"

    # Create first Client as a Thread
    first_Client = Thread(
        name="Client Process 1",
        target=Client(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]).parse,
        args=(str1,)
    ).start()

    # Create Second Client as a Thread
    Second_Client = Thread(
        name="Client Process 2",
        target=Client(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]).parse,
        args=(str2,)
    ).start()

