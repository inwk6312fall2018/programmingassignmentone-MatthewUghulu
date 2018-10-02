"""1task1  part A and B"""

""" The output of this python function will return the tuple (interfacename,"nameif"- value)"""
def int_and_int_name(file_name):
	file=open(file_name)
	my_list1=[]
	my_list2=[]	#will contain all the interface in the running_config
	my_list3=[]	#will contain all the interface name in the running config
	my_list4=[]	#will contain the output as in the form of tuple of (interface,interface name)
	for line in file:
		line=line.strip()
		for word in line.split():
			my_list1.append(word)	#adding all words in my_list1
	for i in range(len(my_list1)):
		if my_list1[i]=='interface':
			my_list2.append(my_list1[i+1])	#making all interface as a list
		elif my_list1[i]=='nameif' or (my_list1[i]=='no' and my_list1[i+1]=='nameif'):
			#making all the interface name a list
			if my_list1[i]=='no' and my_list1[i+1]=='nameif':
				my_list3.append('no name')
			elif my_list1[i-1]!='no' and my_list1[i]=='nameif':
				my_list3.append(my_list1[i+1])
	for i in range(len(my_list2)):			#make list of tuple (interface,interface name)
		my_list4.append((my_list2[i],my_list3[i]))
	return my_list4

"""Program function called "list_ifname_ip" to scan the configuration and return a dictionary that contains the "interface" as
the key and "nameif,VLAN,IPaddress,NetMask" list as the value"""
def list_ifname_ip(file_name):
	file=open(file_name)
	my_list1=[]
	my_list2=[]	#list of all interface's
	my_list3=[]	#list of all interface name's
	my_list4=[]	#list of all vlan's
	my_list5=[]	#list of all ip add's
	my_list6=[]	#list of all netmask
	my_list7=[]	#list of values (intName,vlan,ip add, netMask)
	dict={}	#dict
	for line in file:
		line=line.strip()
		for word in line.split():
			my_list1.append(word)
	for i in range(len(my_list1)):
		if my_list1[i]=='interface':
			my_list2.append(my_list1[i+1])  #making all interface as a list
		elif my_list1[i]=='nameif' or (my_list1[i]=='no' and my_list1[i+1]=='nameif'):
			#making all the interface name a list
			if my_list1[i]=='no' and my_list1[i+1]=='nameif':
				my_list3.append('no name')
				my_list4.append('no vlan')	#adding no name,no ip, no netmask to networks which have none
				my_list5.append('no ip address')
				my_list6.append('no netmask')
			elif my_list1[i-1]!='no' and my_list1[i]=='nameif':
				my_list3.append(my_list1[i+1])
				my_list5.append(my_list1[i+6])
				my_list6.append(my_list1[i+7])
				if my_list1[i-1]=='management-only':	#creating management_only for management network
					my_list4.append('no vlan')
				else:
					my_list4.append(my_list1[i-2]+my_list1[i-1])
	for i in range(len(my_list2)):
		my_list7=[]
		my_list7.append(my_list3[i])
		my_list7.append(my_list4[i])
		my_list7.append(my_list5[i])
		my_list7.append(my_list6[i])
		dict[my_list2[i]]=my_list7	#adding the output my_list7 to dict 
	return dict

if __name__=='__main__':
	print('list that contains the tuple (interfacename,"nameif"- value) is:\n',int_and_int_name('running-config.cfg'))
	print('a dictionary that contains the "interfacename" as the key and "nameif,VLAN,IPaddress,NetMask" list as the value is :\n',list_ifname_ip('running-config.cfg'))
