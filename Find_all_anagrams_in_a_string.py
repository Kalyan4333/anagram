s=input("enter your first string\n")
p=input("enter your second string\n")
anagrams=[]
i=0
j=len(p)
k=len(s)+1
l=(len(s)-len(p))+1
for (i,j) in zip(range(0,l),range(j,k)):
	r=s[i:j]
	if r!=p and sorted(r)==sorted(p):
		anagrams.append(s.find(r))

print(anagrams)
