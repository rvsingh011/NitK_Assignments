import math

class Common_modulus:
	def __init__(self, e1, e2, N, c1, c2, f):
		self.e1 = e1
		self.e2 = e2
		self.N = N
		self.c1 = c1
		self.f = f
		self.c2 = c2
		self.phi_n = None
		self.d1 = None
		self.d2 = None
		self.find_phi_n()
		self.modinv(self.e1, self.phi_n, 1)
		self.modinv(self.e2, self.phi_n, 2)
		self.x = None
		self.y = None
		self.m = None
		self.xgcd(self.e1, self.e2)
		self.get_mess(self.x, self.y)
		self.print()

	def find_phi_n(self):
		amount = 0
		for k in range(1, self.N + 1):
			if math.gcd(self.N, k) == 1:
				amount += 1
		self.phi_n = amount

	def egcd(self, a, b):
		if a == 0:
			return (b, 0, 1)
		else:
			g, y, x = self.egcd(b % a, a)
			return (g, x - (b // a) * y, y)

	def modinv(self, a, m, parameter):
		g, x, y = self.egcd(a, m)
		if g != 1:
			raise Exception('modular inverse does not exist')
		else:
			k = x % m
			if parameter == 1:
				if k < 0:
					self.d1 = k + self.N
				else:
					self.d1 = k
			else:
				if k < 0:
					self.d2 = k + self.N
				else:
					self.d2 = k

	def xgcd(self, b, a):
		if math.gcd(b, a) != 1:
			print("The gcd of not one")
			exit(1)
		x0, x1, y0, y1 = 1, 0, 0, 1
		while a != 0:
			q, b, a = b // a, a, b % a
			x0, x1 = x1, x0 - q * x1
			y0, y1 = y1, y0 - q * y1
		self.x = x0
		self.y = y0

	def get_mess(self, p, q):
		if p < 0:
			mess = (self.pow_inv(self.c1, -1 * p, self.N) * pow(self.c2, q, self.N)) % self.N
		else:
			mess = (pow(self.c1, p, self.N) * self.pow_inv(self.c2, -1 * q, self.N)) % self.N
		self.m = mess

	def print(self):
		print("The message is ", self.m)
		print("The value of phi_N", self.phi_n)
		print("The value of d1 is {} and d2 is {}".format(self.d1, self.d2))
		print("The value of x is {} and y is {}".format(self.x, self.y))
		f.write("\n")
		f.write("The value of phi_n is"+ str(self.phi_n))
		f.write("\n")
		f.write("The message is " + str(self.m))
		f.write("\n")
		f.write("The value of d1 and d2 is" + str(self.d1) + " " + str(self.d2))
		f.write("\n")
		f.write("The value of x and y is" + str(self.x) + " " + str(self.y))

	def pow_inv(self, C, x, N):
		r = pow(C, x, N)
		d = 1
		b = True
		if r == 1:
			b = True
		elif r == 0:
			b = False
		elif r < N:
			for i in range(2, r + 1):
				r1 = N % i
				r2 = r % i
				if r1 == 0 and r2 == 0:
					b = False

		while (b):
			y = (d * r) % N
			if y == 1:
				# print("THE VALUE OF D: ", d)
				# file.write("THE VALUE OF D: " + str(d) + '\n')
				break
			else:
				d = d + 1
		if not b:
			return "INVERSE OF E DOES NOT EXIST!!!"
		else:
			return d


if __name__ == "__main__":
	with open("./output.txt", "a+") as f:
		print("Enter the value of N")
		f.write("Enter the value of N\n")
		N = int(input())
		f.write(str(N))
		f.write("\n")
		print("Enter the value of e1")
		f.write("Enter the value of e\n")
		e1 = int(input())
		f.write(str(e1))
		f.write("\n")
		print("Enter the value of e2")
		f.write("Enter the value of e2\n")
		e2 = int(input())
		f.write(str(e2))
		f.write("\n")
		print("enter the c1")
		f.write("Enter the value of c1\n")
		c1 = int(input())
		f.write(str(c1))
		f.write("\n")
		print("enter the c2")
		f.write("Enter the value of c2\n")
		c2 = int(input())
		f.write(str(c2))
		f.write("\n")
		obj = Common_modulus(e1, e2, N, c1, c2, f)
