def quicksort(item):
    '''Takes in a list, finds a pivot point
        and then recursively quicksorts the upper
        and lower threshold before concatenating each side.'''
    if len(item) < 2:
        return item # No need to sort if less than two items
    else:
        pivot = item[0] 
        less = [i for i in item[1:] if i <= pivot] # Setting all values less than pivot to one group
        greater = [i for i in item[1:] if i > pivot] # Setting all values greater to other group

        return quicksort(less) + [pivot] + quicksort(greater) # Recursively sorts and then combines (call stack order)
    
example = [50,10,5,200]

result = quicksort(example)

print(result)

