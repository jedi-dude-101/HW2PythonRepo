f = open('document.txt','r')
text=f.read()
words=text.split()
counted_words={}
for i in range(len(words)):
	word=words[i]
	if(not(word in counted_words.keys())):
		counted_words[word]=1
	else:
		counted_words[word]+=1
top5={}
for i in range(5):
	top5[words[i]]=counted_words[words[i]]
for key in counted_words:
	for word in top5:
		if (counted_words[key]>top5[word]):
			top5.pop(word,None)
			top5[word]=counted_words[key]
			break
key_list = list(top5)
for i in range(5):
	j=i
	while(j<len(key_list)):
		if(top5[key_list[i]]==top5[key_list[j]] and key_list[i]>key_list[j]):
			temp=key_list[i]
			key_list[i]=key_list[j]
			key_list[j]=temp
		j+=1
print('\r')
for word in key_list:
	print(f'{word}: {top5[word]}')
