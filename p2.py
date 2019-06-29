perimetro = 1000
solucao = 0
for a in range(1,perimetro+1):
	for b in range(a+1,perimetro+1):
		c = perimetro -a -b
		if a*a + b*b == c*c:
			solucao = a*b*c

print(solucao)
