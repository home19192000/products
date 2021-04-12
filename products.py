products = []

while True:
	name = input('請輸入products名稱:')
	if name == 'q':
		break
	price = input('請輸入價錢:')	
	price = int(price)
	products.append([name,price])

print(products)

for p in products:
	print (p[0],'的價錢是',p[1])

with open ('products.csv','w',encoding = 'utf-8') as f:
	f.write('products,價錢\n')
	for p in products:
		f.write(p[0] + ','+ str (p[1]) + '\n')