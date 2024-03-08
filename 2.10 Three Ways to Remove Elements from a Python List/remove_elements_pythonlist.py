users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

print(users)

users.remove('Jordan') # Elimina el elemento que queramos 

print(users)

popped_user = users.pop() #Elimina último elemento de la lista,tb lo retorna para usarlo

print(popped_user) 
print(users)

del users[0] # delete 

print(users)