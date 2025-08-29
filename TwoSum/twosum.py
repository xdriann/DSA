def two_sum(nums,target):
    my_list = []
    my_dict = {}
    for num in nums:
        my_dict[num] = True
    for num1 in nums:
        if (target - num1) in my_dict:
            num2 = target - num1
            my_list.append([num,num2])
    print(my_list)
    
    
    
    
print(two_sum([5, 1, 7, 2, 9, 3], 10))  
print(two_sum([4, 2, 11, 7, 6, 3], 9))  
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
print(two_sum([1, 3, 5, 7, 9], 10))  
print ( two_sum([1, 2, 3, 4, 5], 10) )
print ( two_sum([1, 2, 3, 4, 5], 7) )
print ( two_sum([1, 2, 3, 4, 5], 3) )
print ( two_sum([], 0) )