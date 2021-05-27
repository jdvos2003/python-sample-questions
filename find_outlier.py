def find_outlier(integers):
    even_index = 0
    even_count = 0
    odd_index = 0
    odd_count = 0
    
    # loop through integers finding even and odd and keeping track of index
    for i in range(len(integers)):
        if integers[i] % 2 == 0:
            even_index = i
            even_count += 1
        elif integers[i] % 2 == 1:
            odd_index = i
            odd_count += 1
            
        # Starting with index 2 (3rd element) check to see if both even and 
        # odd counts are positive if they are we know we have seen both even 
        # and odd, now we have to check which is = 1 and return it.
        
        if even_count > 0 and odd_count > 0 and i >= 2:
            if even_count == 1: 
                return integers[even_index]         
            elif odd_count == 1: 
                return integers[odd_index]
            