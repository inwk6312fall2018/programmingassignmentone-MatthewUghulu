"""Python function to create a list of "access-list" for "global_access" and "fw-management_access_in"""

def access_my_list(file_name):
	file=open(file_name)
	my_list=[]
	for line in file:
		line=line.strip()
		for i in line.split():	#add that line to my_list if line contains global-access or fw-management 
			if i=='global_access' or i=='fw-management_access_in':
				my_list.append(line)
	return my_list
print(access_my_list('running-config.cfg')		
