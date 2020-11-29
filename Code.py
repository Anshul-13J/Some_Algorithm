def get_numbers():
    '''
    To convert string  of letters to list of numbers 
    '''
    data = input("Enter data seperated by ' '\n")
    data = data.split(" ")

    for i in range(len(data)):
            try:
                data[i]= int(data[i])
            except:
                print("You entered a wrong value: {} . Please enter a valid number..".format(data[i]))
                data[i]= int(input())
    
    return data



def play():
    print("\nEnter two numbers. First one denotes the number of rows and the second one denotes number of elements you want to pull out of data")
    start_num = get_numbers()
    if len(start_num)<2:                                                         ##In case there are less than 2 elements
        print("Insufficient number of numbers. Filling rest of them with 0")                 
        while len(start_num)< 2:
            start_num.append(0)
    start_num = start_num[:2]                                                    ##In case there are more than 2 elements
   
    rows = start_num[0]
    counter = 0
    row_len=[None]*rows
    row=[None]*rows
    for x in range(rows):
        print("Enter numbers, where first number tells how many numbers you want to enter followed by the numbers..")
        row_data = get_numbers()
        
        
        
        
        row_len[counter] = row_data[0]
        row[counter] = []
        for i in row_data[1:]:
            row[counter].append(i)
        if len(row[counter])<row_len[counter]:
            print("Insufficient number of numbers. Filling rest of them with 0")
            while len(row[counter])<row_len[counter]:
                row[counter].append(0)
            
        counter +=1
    
    for i in range(start_num[1]):
        
        print("Enter the row and the index you want to search: ")
        search = get_numbers()
        if len(search)<2:
            print("You entered less than 2 numbers.. adding 0 to rest of them..")
            while len(search) < 2:
                search.append(0)
        try:
            print("You searched for: {}".format(row[search[0]][search[1]]))
        except:
            print("Index is empty!")


play()        
            
            
    
    
