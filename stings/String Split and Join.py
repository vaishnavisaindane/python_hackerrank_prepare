def split_and_join(line):
    a=line.split()
    
    return '-'.join(a)
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
