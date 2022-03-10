def sort_list():
	list=[]
	n=4
	for i in range(n):
		number=input("please input for an element in the list: ")
		list.append(number)
	i=0
	while i < n :
		j=i
		while(j<n):
			print(j)
			if(list[i]>list[j]):
				temp=list[i]
				list[i]=list[j]
				list[j]=temp
				print(list)
			j+=1
		i+=1
	return list
print(sort_list())
