import enchant
broker = enchant.Broker()
broker.describe()
langs = broker.list_languages()
d = enchant.Dict("en_US")

# initialize input 
n = 6
words = ['hot', 'dog', 'hotdog', 'tailor', 'tail', 'or', 'sunrise', 'anyway', 'boxcar', 'mostakim', 'birdbox']


def find_substrings(s,n):
	position = -1 # initial guess as negative 
	i = 1
	while(i<=n):
		check_result = d.check(s[0:i])
		if(check_result == True):
			# at this point if i==n that means there is no second string to search 
			if(i == n):
				break 
			# otherwise, check the remaining substring starting position i
			check_remaining_part = d.check(s[i:])
			if(check_remaining_part == True): 
				# string s is finally eligible. return i 
				position = i-1 

		i+=1
	return position

def myfunc(n, words):
	result = list()
	for item in words: 
		if(len(item)==n): 
			position = find_substrings(item,n)
			if(position != -1): 
				result.append(item[0:position+1])
				result.append(item[position+1:])

	return result

final_list = myfunc(n,words)

if not final_list:
	print("no result found")
else: 
	print(final_list)
	