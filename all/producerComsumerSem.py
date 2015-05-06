#coding = utf-8

import threading
import time
import random

products = 0
N = 5  #producer number
M = 20  #buffer size

class Producer(threading.Thread):
	def __init__(self, threadName, ifull, iempty, imutex):
		threading.Thread.__init__(self, name=threadName)
		self.sleepTime = random.randrange(1,6)
		self.full = ifull
		self.empty = iempty
		self.mutex = imutex

	def run(self):
		global products
		while True:
			self.empty.acquire()
			self.mutex.acquire()
			products += 1
			print "Producer(%s):deliver one, now products:%s" %(self.name, products)
			self.mutex.release()
			self.full.release()
			#print full._Semaphore__value
			time.sleep(self.sleepTime)

class Comsumer(threading.Thread):
	def __init__(self, threadName, ifull, iempty, imutex):
		threading.Thread.__init__(self, name=threadName)
		self.sleepTime = random.randrange(1,6)
		self.full = ifull
		self.empty = iempty
		self.mutex = imutex

	def run(self):
		global products
		while True:
			self.full.acquire()
			self.mutex.acquire()
			products -= 1
			print "Comsumer(%s):comsume one, now products:%s" %(self.name, products)
			self.mutex.release()
			self.empty.release()
			time.sleep(self.sleepTime)


full = threading.Semaphore(0)
empty = threading.Semaphore(M)
mutex = threading.Semaphore(1)

for i in range(N):
	p = Producer(str(i+1),full, empty, mutex)
	p.start()

c = Comsumer("one", full, empty, mutex)
c.start() 


