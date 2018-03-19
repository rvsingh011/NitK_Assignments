import random
from math import ceil


class Blind_Signature:
    def __init__(self, e, d, N, c):
        self.e = e
        self.d = d
        self.N = N
        self.c = c
        self.f = f
        self.signature = None
        self.inverse = None

    def get_signature(self):
        # random_number = random.randint(1, self.N - 1)
        random_number = 78
        self.f.write("/n random number" + str(random_number) + "/n")
        fake_m = (pow(random_number, self.e) * self.c) % self.N
        fake_signature = pow(fake_m, self.d, self.N)
        self.f.write("/n fake signature" + str(fake_signature) + "/n")
        random_number = random_number % self.N
        x = 1
        while (True):
            y = (x * random_number) % self.N
            if y == 1:
                break
            else:
                x = x + 1
        self.signature = (fake_signature * x) % self.N
        print("the signature is", self.signature)
        self.f.write("the signature is" + str(self.signature))

    def verify_signature(self):
        print("The value of message is")
        self.f.write("The value of message is")
        print(pow(self.signature, self.e, self.N))


if __name__ == "__main__":
    with open("./output.txt", "a+") as f:
        print("Enter the value of N")
        f.write("Enter the value of N\n")
        N = int(input())
        f.write(str(N))
        f.write("\n")
        print("Enter the value of e")
        f.write("Enter the value of e\n")
        e = int(input())
        f.write(str(e))
        f.write("\n")
        print("Enter the value of d")
        f.write("Enter the value of d\n")
        d = int(input())
        f.write(str(d))
        f.write("\n")
        print("enter the cipher text")
        f.write("Enter the value of cipher text\n")
        c = int(input())
        f.write(str(c))
        f.write("\n")
        obj = Blind_Signature(e, d, N, c, f)
        obj.get_signature()
        obj.verify_signature()
