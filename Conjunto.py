a = {'Caiapós', 'Tupinambás', 'Guaranis', 'Charruas', 'Xavantes'}
b = {'Charruas', 'Carajás', 'Xavantes', 'Guajajaras'}

print('Conjunto a:', a)
print('Conjunto b:', b)

uniao = a.union(b)
print('União:', uniao)

interseccao = a.intersection(b)
print('Intersecção:', interseccao)

x = a.copy()
x.intersection_update(b)

print('Conjunto a alterado:', x)
print('Conjunto a original:', a)

#diferenca = a - b 

diferenca = a.difference(b)
print('Diferença do conjunto a com b:', diferenca)

diferenca_simetrica = a.symmetric_difference(b)
print('Diferença simétrica do conjunto a com b (união menos a intersecção):', diferenca_simetrica)

if 'Guaranis' in a:
  print('Existe Guaranis no conjunto a!')

else:
  print('Não existe Guaranis no conjunto a!')

c = {'Carajás', 'Xavantes'} 

if c.issubset(b):
  print('c é subconjunto de b')

else:
  print('c não é subconjunto de b')

if c.issuperset(a):
  print('c é superconjunto de a')

else:
  print('c não é superconjunto de a')

# Verifica se os dois conjuntos possuem intersecção (possuem elementos em comum)

if a.isdisjoint(b):
  print('a é disjunto de b')
  
else:
  print('a não é disjunto de b')