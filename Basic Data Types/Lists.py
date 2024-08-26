if __name__ == '__main__':
    N = int(input())
    my_list=[]
    for iteration in range(N):
        user_input=input().split()
        
        if user_input[0]=='insert':
            my_list.insert(int(user_input[1]), int(user_input[2]))
        elif user_input[0]=='print':
            print(my_list) 
        elif user_input[0]=='remove': 
            my_list.remove(int(user_input[1]))
        elif user_input[0]=='append': 
            my_list.append(int(user_input[1])) 
        elif user_input[0]=='sort': 
            my_list.sort()
        elif user_input[0]=='pop':
            my_list.pop() 
        elif user_input[0]=='reverse':
            my_list.reverse()
            
       
            
        
        
