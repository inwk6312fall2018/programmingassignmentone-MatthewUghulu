"""This Python function is to create a new configuration file that 
replaces all (sub-)interface IP addresses that start with '172.' and '192." to "10." 
and also change the security-level to "10" . """

def change_ip(file_name):
	file=open(file_name)
	my_list=[]
	my_list2=[]	#adding all ip address in a list
	my_list3=[]	#adding list of elements in ip add
	my_list4=[]	#updated ip add  making it a list
	for line in file:
		line=line.strip()
		for word in line.split():
			lst.append(word)
	for i in range(len(lst)):
		if lst[i-1]!='no' and lst[i]=='ip' and lst[i+1]=='address':
			my_list2.append(lst[i+2])	#adding all ip add in my_list2
	for i in my_list2:
		my_list3.append(i.split('.'))	#list of elements in ip
	for i in my_list3:		#changing all ip add with '172' or '192' to '10'
		del i[0]	#delete the first element
		i.insert(0,'10')	#insert '10' at at the first index location
		my_list4.append('.'.join(i))	#add upated ip add in list
	return my_list4

print(change_ip('running-config.txt'))
