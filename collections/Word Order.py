# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
word_count={}
distinct_words=[]
for i in range(n):
    word=input()
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
        distinct_words.append(word)
print(len(distinct_words))
print(" ".join(str(word_count[word])for word in word_count))

https://youtu.be/4W8_9zaLAY4?si=_nouFDH-w2iDRWe-
