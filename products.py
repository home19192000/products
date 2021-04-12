products = []

while True:
	name = input('請輸入products名稱:')
	if name == 'q':
		break
	price = input('請輸入價錢:')	
	products.append([name,price])

print(products)

for p in products:
	print (p[0],'的價錢是',p[1])
