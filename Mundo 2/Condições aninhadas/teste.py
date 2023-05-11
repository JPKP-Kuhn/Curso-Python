import time
startTime = time.time()
for i in range(0,5):
   print(i)
   # making delay for 1 second
   time.sleep(1)
endTime = time.time()
elapsedTime = endTime - startTime
print("Elapsed Time = %s" % elapsedTime)
