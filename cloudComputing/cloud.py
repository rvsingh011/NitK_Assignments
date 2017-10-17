import random
import time
from math import floor
class PyMachine:

    def __init__(self, cpu, memory, network):
        self.cpu = cpu
        self.memory = memory
        self.network = network
        self.cpu_list = []
        self.memory_list=[]
        self.weight_list=[]
        self.network_list=[]
        self.virtual_machines = 4
        self.vm_dict = {}
        self.average_bw = 0
        self.strong_vm = []
        self.weak_vm = []
        self.create_vm()
        self.create_memory()
        self.create_wight()
        self.create_network()
        self.start()


    def start(self):
        count = 1
        while 1:
            if count % 3 == 0:
                self.network = random.randint(100, 200)
                self.create_network()
            time.sleep(5)
            print(self.network)
            self.create_vm_dict()
            self.calculate_normalized_bandwidth()
            self.calculate_average_bandwidth()
            self.divide_vms()
            self.adjust_bandwidth()
            count += 1

    def create_vm(self):
        # create cpu
        b = random.randint(2, self.cpu-2)
        a = random.randint(1, b - 1)
        c = random.randint(b + 1, self.cpu-1)
        self.cpu_list = [a, b - a, c - b, self.cpu - c]
        # print(self.cpu_list)

    def create_memory(self):
        # create memory
        b = random.randint(2, self.memory - 2)
        a = random.randint(1, b - 1)
        c = random.randint(b + 1, self.memory - 1)
        self.memory_list = [a, b - a, c - b, self.memory - c]
        # print(self.memory_list)

    def create_network(self):
        # create network
        b = random.randint(2, self.network - 2)
        a = random.randint(1, b - 1)
        c = random.randint(b + 1, self.network - 1)
        self.network_list = [a, b - a, c - b, self.network - c]
        # print(self.network_list)

    def create_wight(self):
        # create weight
        r = [random.random() for i in range(0, 4)]
        s = sum(r)
        self.weight_list = [i / s for i in r]

    def create_vm_dict(self):
        # creating the vm dictionary
        for index in range(self.virtual_machines):
            self.vm_dict[index] = {
                "cpu": self.cpu_list[index],
                "memory": self.memory_list[index],
                "network": self.network_list[index],
                "weight": self.weight_list[index]
            }
        # print(self.vm_dict)

    def calculate_normalized_bandwidth(self):
        """Adding Normalized Bandwidth"""
        for index in range(self.virtual_machines):
            self.vm_dict[index]["n_bw"] = self.vm_dict[index]["network"]/self.vm_dict[index]["weight"]

    def calculate_average_bandwidth(self):
        """Calculating Average bandwidth"""
        for index in range(self.virtual_machines):
            self.average_bw += self.vm_dict[index]["n_bw"]
        # print("Vm dictionary", self.vm_dict)

        self.average_bw = self.average_bw / self.virtual_machines
        print("Average bandwidth", self.average_bw)

    def divide_vms(self):
        """Make virtual machines partitions"""
        self.weak_vm, self.strong_vm = [], []
        for index in range(self.virtual_machines):
            if self.vm_dict[index]["n_bw"] < self.average_bw:
                self.weak_vm.append(index)
            else:
                self.strong_vm.append(index)

        print("list of strong and weak vms", self.strong_vm, self.weak_vm, sep="\n")


    def choose_delta(self):
        return floor((max(self.network_list) - min(self.network_list)) / self.virtual_machines)

        # max_band, min_band = 0,1000
        # for key, values in self.vm_dict.items():
        #     if values["n_bw"] > max_band:
        #         max_band = values["n_bw"]
        #     if values["n_bw"] < min_band:
        #         min_band = values["n_bw"]
        # return (max_band - min_band)/self.virtual_machines




    def adjust_bandwidth(self):
        delta = self.choose_delta()
        bandwidth_gain = 0
        print(delta)
        print(self.network_list)
        for strong_vm in self.strong_vm:
            if self.network_list[strong_vm] - delta > 5:
                bandwidth_gain += delta
                self.network_list[strong_vm] -= delta
            # else:
            #     diff = delta + (self.network_list[strong_vm] - delta)
        print(self.network_list)
        for weak_vm in self.weak_vm:
            self.network_list[weak_vm] += floor(bandwidth_gain / len(self.weak_vm))
        print(self.network_list, "end")




        
    def change_bandwidth(self, new_bandwidth):
        print(new_bandwidth)
        self.network = new_bandwidth
        self.create_network()
        self.create_vm_dict()
        self.calculate_normalized_bandwidth()
        self.calculate_average_bandwidth()
        self.divide_vms()
        self.adjust_bandwidth()


if __name__ == "__main__":
    physical_machine = PyMachine(5, 50, 100)


    # for x in range(5):
    #     time.sleep(60)
    #     physical_machine.change_bandwidth(random.randint(100, 200))
