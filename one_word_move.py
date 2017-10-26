import time

a = raw_input("input: ")

a_length = len(a)
a_length2 = a_length
blank_n = 10 - len(a)
blank_n2 = 9
num_count = 1
blank = ""

#print if len(a) were shorter than 10
if len(a) <= 10:
	while True:
		while blank_n > -1:
			for x in range(blank_n):
				print(blank),
			print(a)
			blank_n -= 1
			time.sleep(1)
		for z in range(1,a_length+1):
			print(a[z:])
			time.sleep(1)
		blank_n = 10 - len(a)
		break
	while True:
		while blank_n2 > -1:
			for y in range(blank_n2):
				print(blank),
			print(a[:num_count])
			blank_n2 -= 1
			num_count += 1
			if num_count > 10:
				num_count = 1
			time.sleep(1)
		for k in range(1,a_length+1):
			print(a[k:])
			time.sleep(1)
		blank_n2 = 9	


#print if len(a) were longer than 10
else:
	while True:
		for x in range(len(a)-9):
			print(a[x:x+10])
			time.sleep(1)
		for z in range(a_length-9,a_length+1):
			print(a[z:])
			time.sleep(1)
		break	
	while True:
		while blank_n2 > -1:
			for y in range(blank_n2):
				print(blank),
			print(a[:num_count])
			blank_n2 -= 1
			num_count += 1
			if num_count > 10:
				num_count = 1
			time.sleep(1)
		for x in range(1,a_length+1):
			print(a[x:x+10])
			time.sleep(1)
		blank_n2 = 9

#// by blog ryu //



		
	



		

	

	