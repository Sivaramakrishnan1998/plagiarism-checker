def calplag(file1_data,text1):
	c=0
	val=0.0
	a=file1_data.split(" ")
	b=text1.split(" ")
	print (len(a))
	print (len(b))

	for i in range(0,len(b)):
		print (b[i])
		for j in range(0,len(a)):
			print (a[j])
			if b[i]==a[j]:
				c+=1;
				print (c)
				break;

	val=c*100
	val=val/len(b);
	print (val)

	return val
f = open('file1.txt')
file1_data = f.read()
g = open('file2.txt')
text1 = g.read()

calplag(file1_data,text1)
