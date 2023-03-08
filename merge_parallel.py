from threading import Thread
import threading
import time
import random

random.seed()
array = [i for i in range(10000)]
random.shuffle(array)
print("Trước khi sắp xếp: ", array)

class _Thread(Thread):
	def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
		Thread.__init__(self, group = group, target = target, name = name, args = args, kwargs = kwargs)
		self._return = None
		self._Thread__target = target
		self._Thread__args = args
	def run(self):
		if self._Thread__target is not None:
			self._return = self._Thread__target(*self._Thread__args)
	def join(self):
		Thread.join(self)
		return self._return

def merge_sort(arr):
	cp = arr
	if len(cp) <= 1:
		return cp

	#chia mảng thành 2 mảng con và xử lí song song
	mid = len(arr)//2

	t1 = _Thread(target = merge_sort, args = (cp[:mid],))
	t2 = _Thread(target = merge_sort, args = (cp[mid:],))
	t1.start()
	t2.start()
	left = t1.join()
	right = t2.join()

	#Kết hợp
	cp = []
	i, j = 0, 0

	while i<len(left) and j<len(right):
		if left[i]<right[j]:
			cp.append(left[i])
			i+=1
		else:
			cp.append(right[j])
			j+=1

	if i<len(left):
		for a in left[i:]:
			cp.append(a)
	if j<len(right):
		for a in right[j:]:
			cp.append(a)

	time.sleep(0.01)
	return cp

array = merge_sort(array)
print("Sau khi sắp xếp: ", array)
