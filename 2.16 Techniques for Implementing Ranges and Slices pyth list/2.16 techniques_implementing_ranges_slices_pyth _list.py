tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
  'computer science'
]

tag_range = tags[1:-1:2] # nos devuelve el primer,ultimo,el segundo empezando por el final
tag_range = tags[::-1] # nos devuelve una lista nueva, no modifica la lista original al reves

print(tag_range)

tags.sort(reverse=True) #nos devuelve nada, solo ordena alfabeticamente

print(tags)