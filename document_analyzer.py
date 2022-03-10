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
top5=0
for w in sorted(counted_words,key=counted_words.get, reverse=True):
	print(w,counted_words[w])
	top5+=1
	if (top5>6):
		break
