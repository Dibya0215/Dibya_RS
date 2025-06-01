#duplicate across
my_dict = {
    'a': [1, 2, 3],
    'b': [3, 4, 5],
    'c': [5, 6]
}

already_added = []

for key in my_dict:
    new_values = []
    
  
   
    for number in my_dict[key]:
        
        if number not in already_added:
            new_values.append(number)
            already_added.append(number)
    
   
    my_dict[key] = new_values


print(my_dict)
