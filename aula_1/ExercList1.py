pow2 = [2 ** x for x in range(10)]
print(pow2)

pow2 = [2 ** x for x in range(10) if x > 5]
odd = [x for x in range(20) if x % 2 == 1]
conc = [x+y for x in ['Python','C'] for y in ['Language', 'Programming']] 
print(pow2)
print(odd)
print(conc)

