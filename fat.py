import time

def fat(i):
	if i <= 0:
		return 1
	else:
		return i * fat(i - 1)

for i in range(10):
        start_time = time.time()
        print(fat(i))
        print("--- %s seconds ---" % (time.time() - start_time)+"\n")
