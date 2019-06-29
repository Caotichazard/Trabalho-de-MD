start = 1
longest_number = 1
longest_steps = 1
cur_steps = 0
cur_number = 0
while(start < 1000000):
	cur_steps = 0
	start = start + 2
	cur_number = start
	while (cur_number != 1):
		if cur_number%2 == 0:
			cur_number = cur_number/2
			cur_steps = cur_steps+1
		else:
			cur_number = (3*cur_number)+1			
			cur_steps = cur_steps+1
	if cur_steps > longest_steps:
		longest_number = start
		longest_steps = cur_steps
	

print(longest_number)
