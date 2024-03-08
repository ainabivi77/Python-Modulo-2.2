tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
]

print(tags[1:4:2]) #obtenemos desde la posición 1 hasta la 4, pero saltando de 2 en 2

slice_obj = slice(1, 4, 2)

print(slice_obj.start) #obtenemos el inicio
print(slice_obj.stop) #obtenemos el final
print(slice_obj.step) #obtenemos el paso

print(tags[slice_obj]) #obtenemos el mismo resultado que con el slice_obj