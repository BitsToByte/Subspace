from math import prod
n = int(input('Введите число: '))

def Factor(n):
  Ans = []
  d = 2
  while d * d <= n:
    if n % d == 0:
      Ans.append(d)
      n //= d
    else:
      d += 1
  if n > 1:
    Ans.append(n)
  return Ans

simple_lst = []; result = str(n) + '! = '

for i in range(2,n+1):
  lst_temp = Factor(i)
  for y in lst_temp:
    simple_lst.append(y)

set_temp = set(simple_lst)

for i in set_temp:
  rank = simple_lst.count(i)
  result += str(i)
  if rank > 1:
    result += '^' + str(rank) + ' * '
  else:
    result += ' * '

result = result[:-3]
print (result)
# 5! = 2^3 * 3 * 5
# 22! = 2^19 * 3^9 * 5^4 * 7^3 * 11^2 * 13 * 17 * 19
# 25! = 2^22 * 3^10 * 5^6 * 7^3 * 11^2 * 13 * 17 * 19 * 23