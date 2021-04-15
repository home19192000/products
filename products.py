import os  # operation system

#read file
def read_file(filename):
    products = []
    with open (filename,'r',encoding = 'utf-8') as f:
        for line in f:
            if'products,價錢' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name,price])
    return products


#讓user 輸入
def user_input(products):
    while True:
        name = input('請輸入products名稱:')
        if name == 'q':
            break
        price = input('請輸入價錢:')	
        price = int(price)
        products.append([name,price])
    print(products)
    return products

# print out record
def print_products(products):
    for p in products:
        print (p[0],'的價錢是',p[1])
#write in file
def write_file(filename,products):
    with open (filename,'w',encoding = 'utf-8') as f:
        f.write('products,價錢\n')
        for p in products:
            f.write(p[0] + ','+ str (p[1]) + '\n')

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('file found')
        products = read_file(filename)
    else:
        print('找不到file')

    products = user_input(products)
    print_products(products)
    write_file('products.csv',products)
main()
