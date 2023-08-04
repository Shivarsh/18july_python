string =input("Enter Your String:")
print(string)

not_index = string.find('not')
poor_index = string.find('poor')

if not_index != -1 and poor_index != -1 and not_index < poor_index:
     print(string[:not_index] + 'good' + string[poor_index+4:])
else:
    print(string)



