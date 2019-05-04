def max(a):

	q=a[0]
	for i in range(len(a)):
		if(a[i]>q):
			q=a[i]

	return q	


def max2(a):

	b=a

	q=max(a)
	b.remove(q)
	q2=max(b)
	
	return([q,q2])
		
def maxn(a,n):

	b=a
	

	arr=[]

	for i in range(n):

		q=max(b)
		arr.append(q)
		b.remove(q)
	
	return(arr)


def bit_set(s):

	w=bin(s)
	w=w[2:]

	count=0

	for i in range(len(w)):

		if(w[i]=="1"):

			count+=1

	return(count)
		

def permute(a):
	
	op=[]

	ch=list(a)
	
	for j in range(len(a)):
		w=a[j]
		for i in ch:
			if i not in list(w): 			
				w+=i

		print(w)
		op.append(w)

	return(op)			
				

q1=max([5,10,-3,2,9])
q2=max([-2,-3,-1,0,-8])
w1=max2([10,5,19,12,17,5,20])
e1=maxn([10,5,19,12,17,5,20],2)
e2=maxn([10,5,19,12,17,5,20],3)
r1=bit_set(5)
r2=bit_set(129)
r3=bit_set(234)

print(w1)		
						
		
					




