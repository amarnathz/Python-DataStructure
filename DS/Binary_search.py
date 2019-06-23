
def binary_search(a, v):
    mid=len(a)//2
    
    while(True ):
        
        #print(a[mid])
        if(a[mid]==v):
            return mid
        elif(mid ==0 or mid ==len(a)-1):
            break
        elif(v<a[mid]):
            #print("Mid1",mid)
            vi=len(a[:mid])//2
            
            mid=vi
            
        elif(v>a[mid]):
            #print("Mid2",mid)
            vi=len(a[mid:])//2
            
            mid+=vi
            
            
        
        continue    
    
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val2) )

#https://www.cs.usfca.edu/~galles/visualization/Search.html
