import time

start_time = int(time.time())
minute = 0

while True:
	time_pass = int(time.time() - start_time)
	print str(minute)," : ",str(time_pass)
	if time_pass >= 59:
		minute += 1
		start_time = int(time.time() + 1)
	time.sleep(1)


