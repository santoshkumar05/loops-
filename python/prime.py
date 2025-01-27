#check for vowels
n=0
word=str(input())
vowels=["a","e","i","o","u"]
for i in vowels:
    for j in word:
        if(i==j):
            n+=1;
        else:
            n+=0;
print("number of vowles:",n)