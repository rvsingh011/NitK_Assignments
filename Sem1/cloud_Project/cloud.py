import random
import time
from math import floor
import threading
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = plt.subplot2grid((8, 1), (0, 0), rowspan=3)
ax2 = plt.subplot2grid((8, 1), (4, 0), rowspan=3)

cons_bandwidth_vm1 = []
cons_bandwidth_vm2 = []
cons_bandwidth_vm3 = []
cons_bandwidth_vm4 = []

iterations = []
bandwidth_vm1 = []
bandwidth_vm2 = []
bandwidth_vm3 = []
bandwidth_vm4 = []


class PyMachine:
    def __init__(self, cpu, memory, network):
        self.cpu = cpu
        self.memory = memory
        self.network = network
        self.cpu_list = []
        self.memory_list = []
        self.weight_list = []
        self.network_list = []
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
            if count % 20 == 0:
                self.network = random.randint(100, 200)
                self.create_network()
            time.sleep(2)
            print(self.network)
            self.create_vm_dict()
            self.calculate_normalized_bandwidth()
            self.calculate_average_bandwidth()
            self.divide_vms()
            self.adjust_bandwidth()
            count += 1

    def create_vm(self):
        # create cpu
        b = random.randint(2, self.cpu - 2)
        a = random.randint(1, b - 1)
        c = random.randint(b + 1, self.cpu - 1)
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
        global cons_bandwidth_vm1
        global cons_bandwidth_vm2
        global cons_bandwidth_vm3
        global cons_bandwidth_vm4

        global iterations
        global bandwidth_vm1
        global bandwidth_vm2
        global bandwidth_vm3
        global bandwidth_vm4
        # create network
        b = random.randint(2, self.network - 2)
        a = random.randint(1, b - 1)
        c = random.randint(b + 1, self.network - 1)
        self.network_list = [a, b - a, c - b, self.network - c]

        if iterations:
            iterations.append(iterations[-1] + 1)
        else:
            iterations.append(0)
        bandwidth_vm1.append(0)
        bandwidth_vm2.append(0)
        bandwidth_vm3.append(0)
        bandwidth_vm4.append(0)

        cons_bandwidth_vm1.append(self.network_list[0])
        cons_bandwidth_vm2.append(self.network_list[1])
        cons_bandwidth_vm3.append(self.network_list[2])
        cons_bandwidth_vm4.append(self.network_list[3])
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
            self.vm_dict[index]["n_bw"] = self.vm_dict[index]["network"] / self.vm_dict[index]["weight"]

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

    def adjust_bandwidth(self):
        global iterations
        global bandwidth_vm1
        global bandwidth_vm2
        global bandwidth_vm3
        global bandwidth_vm4
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

        iterations.append(iterations[-1] + 1)
        bandwidth_vm1.append(self.network_list[0])
        bandwidth_vm2.append(self.network_list[1])
        bandwidth_vm3.append(self.network_list[2])
        bandwidth_vm4.append(self.network_list[3])

        cons_bandwidth_vm1.append(cons_bandwidth_vm1[-1])
        cons_bandwidth_vm2.append(cons_bandwidth_vm2[-1])
        cons_bandwidth_vm3.append(cons_bandwidth_vm3[-1])
        cons_bandwidth_vm4.append(cons_bandwidth_vm4[-1])


def main():
    print("I have also started")
    physical_machine = PyMachine(5, 50, 100)


def animate(i):
    global iterations
    global bandwidth_vm1
    global bandwidth_vm2
    global bandwidth_vm3
    global bandwidth_vm4

    ax1.clear()
    ax2.clear()

    ax1.set_ylabel("Bandwith")
    ax1.set_title("Without Fair Scheduling")
    ax1.plot(iterations, bandwidth_vm1)
    ax1.plot(iterations, bandwidth_vm2)
    ax1.plot(iterations, bandwidth_vm3)
    ax1.plot(iterations, bandwidth_vm4)

    ax2.set_xlabel("Iterations")
    ax2.set_ylabel("Bandwidth")
    ax2.set_title("With Fair Scheduling")
    ax2.plot(iterations, cons_bandwidth_vm1)
    ax2.plot(iterations, cons_bandwidth_vm2)
    ax2.plot(iterations, cons_bandwidth_vm3)
    ax2.plot(iterations, cons_bandwidth_vm4)


if __name__ == "__main__":
    main_thread = threading.Thread(name="main", target= main)
    main_thread.start()
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()
    print(threading.enumerate())


