tipo1 = input()
tipo2 = input()
tipo3 = input()

if tipo1 == 'vertebrado':
  if tipo2 == 'ave':
    if tipo3 == 'carnivoro': print('aguia')
    elif tipo3 == 'onivoro': print('pomba')
  elif tipo2 == 'mamifero':
    if tipo3 == 'onivoro': print('homem')
    elif tipo3 == 'herbivoro': print('vaca')
elif tipo1 == 'invertebrado':
  if tipo2 == 'inseto':
    if tipo3 == 'hematofago': print('pulga')
    elif tipo3 == 'herbivoro': print('lagarta')
  elif tipo2 == 'anelideo':
    if tipo3 == 'hematofago': print('sanguessuga')
    elif tipo3 == 'onivoro': print('minhoca')