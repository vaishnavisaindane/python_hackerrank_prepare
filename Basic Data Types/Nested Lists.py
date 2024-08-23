if __name__ == '__main__':
    lst=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name,score])
    findscore=[x[1]for x in lst]
    setscore=sorted(set(findscore))
    findname=sorted([y[0]for y in lst if(setscore[1]==y[1])])
    for z in findname:
        print(z)




https://youtu.be/Pv-9Oweb3SY?si=SFpEWbUykx-Os2FG
