import os, shutil
class cyclic_attack:
    def __init__(self, p, q, e, c, f):
        self.cipher_text = c
        self.e = e
        self.d = None
        self.phi_n = None
        self.p = p
        self.q = q
        self.mess = None
        self.n = None
        self.k = None
        self.f = f

    def calculate_n(self):
        self.n = self.p * self.q
        self.phi_n = (self.p -1) * (self.q -1)
        print("value of n and phi_n are")
        print(self.phi_n, self.n)
        self.f.write("\nvalue of n and phi_n are\n")
        self.f.write(str(self.n) + " " + str(self.phi_n))
        self.f.write("\n")

    def extended_euclidean(self):
        b = self.e
        n = self.phi_n
        x0, x1, y0, y1 = 1, 0, 0, 1
        while n != 0:
            q, b, n = b // n, n, b % n
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        self.d = x0
        self.f.write("\nValue of d is\n")
        self.f.write(str(self.d))
        self.f.write("\n")

    def cyclic_attack(self,):
        last_value = None
        k = 1
        while True:
            value = pow(self.cipher_text, pow(self.e, k), self.n)
            self.f.write("\nvalue, k\n")
            self.f.write(str(value) + " " + str(k))
            self.f.write("\n")
            print(value)
            if value == c:
                self.mess= last_value
                self.k = k
                self.f.write("\nThe value of mess and k\n")
                self.f.write(str(self.mess) + " " + str(self.k))
                return
            else:
                last_value = value
                k += 1

    def check_mess(self):
        print("converting the message to cipher")
        self.f.write("\nconverting the message to cipher\n")
        x = pow(self.mess, self.e, self.n)
        print(x)
        self.f.write(str(x))
        if self.d < 0:
            print("The value of d is", self.phi_n + self.d)
        else:
            print("The value of d is", self.d)


if __name__ == "__main__":
    with open("./output.txt", "a+") as f:
        print("Enter the value of P")
        f.write("Enter the value of P\n")
        p = int(input())
        f.write(str(p))
        f.write("\n")
        print("Enter the value of Q")
        f.write("Enter the value of q\n")
        q = int(input())
        f.write(str(q))
        f.write("\n")
        print("Enter the value of e")
        f.write("Enter the value of e\n")
        e = int(input())
        f.write(str(e))
        f.write("\n")
        print("enter the cipher text")
        f.write("Enter the value of cipher text\n")
        c = int(input())
        f.write(str(c))
        f.write("\n")
    #     p=47
    #     q=59
    #     e=17
    #     c=2342
        obj = cyclic_attack(p,q, e, c, f)
        obj.calculate_n()
        obj.extended_euclidean()
        obj.cyclic_attack()
        obj.check_mess()




# In[28]:



        
            
            
        
        
        
        
        

