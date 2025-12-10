zork = 0
totalNotas = 0
media = 0
print('Vamos a calcular la media')
for thing in [9, 8, 5, 7, 6, 9] :
    zork = zork + thing
    totalNotas = totalNotas + 1

media = zork / totalNotas
print(media)

smallest_so_far = None
print('Before', smallest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
   print(smallest_so_far, the_num)

print('After', smallest_so_far)