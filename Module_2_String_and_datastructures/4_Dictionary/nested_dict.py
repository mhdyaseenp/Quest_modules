'nested dictionary'

nested_dict = { 
    'student1' : {
        'name'  : 'Jasil' ,
        'age'   : 22      ,
        'batch' : 'Python full stack' ,
        'ph no' : [9656177550, 5615230255]
    },

    'student2' : {
        'name'  : 'Niyas' ,
        'age'   : 22      ,
        'batch' : 'Java full stack' ,
        'ph no' : 6201202691
    },
}

print(nested_dict)


'Access Element '

# print(nested_dict['student1']['batch'])
# print(nested_dict['student1']['ph no'][1])


'add'

# nested_dict['student2']['ph no'] = (9656177550, 5615230255)
# print(nested_dict['student2'])


'update'

# nested_dict['student2']['name'] = 'Shakir'
# print(nested_dict['student2'])