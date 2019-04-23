def divisors(num):
	listResult = [1]
	#start from 2, loop thru the num, if mod == 0 then its a divisor of num, else false
	for counter in range(2, num+1):
		if (num % counter == 0):
			listResult.append(counter)
	#print(listResult)	
	return listResult
