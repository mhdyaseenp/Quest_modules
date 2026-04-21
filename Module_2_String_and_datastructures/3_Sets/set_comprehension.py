# numbers={2,3,4,5,46,7,4,7,2,8,9,15}
# multiple_of_3={i for i in numbers if i%3==0}
# print(multiple_of_3)


# even or odd
# numbers={2,3,4,5,46,7,4,7,2,8,9,15} 
# even_or_odd={'Even' if num%2==0 else 'odd' for num in numbers}                  #{'Even', 'odd'}. bcz set donot print duplicate values
# even_or_odd=['Even' if num%2==0 else 'odd' for num in numbers]                  #['Even', 'odd', 'Even', 'odd', 'odd', 'Even', 'odd', 'Even', 'odd']
# print(even_or_odd )


# zero or one
# numbers={2,3,4,5,46,7,4,7,2,8,9,15} 
# even_or_odd={'zero' if num<5 else 'one' for num in numbers}      
# one_or_zero=[0 if num<5 else 1 for num in numbers]
# print(one_or_zero)            


numbers={66,7,8,2,3,4,5,46,7,4,7,2,8,9,15} 
# even_or_odd={'zero' if num<5 else 'one' for num in numbers}      
one_or_zero=['0 less than 5' if num<5 else "1 grater than 5" if num>5 else 5  for num in numbers]
print(one_or_zero)            
