# A data cube is a multidimensional representation of data used in data warehousing and online analytical processing (OLAP) systems.
# It allows for the efficient analysis of data from multiple perspectives or dimensions. 
# enables users to perform complex queries and generate reports quickly and effectively. 

class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

products = [
    Product("Laptop", "Electronics", 10000),
    Product("TV", "Electronics", 40000),
    Product("Laptop", "Electronics", 10000),
    Product("Jeans", "Clothing", 2000),
    Product("iPhone", "Electronics", 100000),
    Product("Laptop", "Electronics", 10000),
    Product("iPhone", "Electronics", 100000),
    Product("Laptop", "Electronics", 10000),
    Product("Tops", "Clothing", 1000),
    Product("Jeans", "Clothing", 2000),
    Product("Jeans", "Clothing", 2000)
]

dates = ['2023-10-02', '2023-10-03', '2023-10-04']
countries = ['USA', 'UK', 'Germany']

data_cube = {}

for product in products:
    for date in dates:
        for country in countries:

            if product.category not in data_cube:
                data_cube[product.category] = {}

            if product.name not in data_cube[product.category]:
                data_cube[product.category][product.name] = {}

            if date not in data_cube[product.category][product.name]:
                data_cube[product.category][product.name][date] = {}

            data_cube[product.category][product.name][date][country] = product.price

# Print the data_cube
for category, products in data_cube.items():
    print('Category:', category)
    for product, dates in products.items():
        print('  Product:', product)
        for date, countries in dates.items():
            print('    Date:', date)
            for country, price in countries.items():
                print('      Country:', country, 'Price:', price)

