def print_formatted(number):
    l=len("{:b}".format(number))
    for i in range(1,number+1):
        d="{:>{l}d}".format(i,l=l)
        o="{:>{l}o}".format(i,l=l)
        X="{:>{l}X}".format(i,l=l)
        b="{:>{l}b}".format(i,l=l)
        print(d,o,X,b)
        
    # your code goes here

if __name__ == '__main__':




https://youtu.be/69pzFxqlbjI?si=yxViMDltoBHBizrj
