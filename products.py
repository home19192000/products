#read the file

products = []

with open ('products.csv','r',encoding = 'utf-8') as f:
	for line in f:
		if'products,價錢' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name,price])
print (products)
#讓user 輸入
while True:
	name = input('請輸入products名稱:')
	if name == 'q':
		break
	price = input('請輸入價錢:')	
	price = int(price)
	products.append([name,price])
print(products)

# print out record
for p in products:
	print (p[0],'的價錢是',p[1])
#write in file
with open ('products.csv','w',encoding = 'utf-8') as f:
	f.write('products,價錢\n')
	for p in products:
		f.write(p[0] + ','+ str (p[1]) + '\n')


