def precio_menor(prod_list, p_name):
    product_data = prod_list[p_name]
    menor = product_data[0]
    for dic in product_data:
        if dic["price"] < menor["price"]:
            menor = dic
    return menor


def show_products(names):
    index = 0
    while index < len(names):
        value = names[index]
        index = index + 1
        print(f"{index}- {value}")


def calculate_basic_basket(prod_list, lista):
    costosmenores = []
    for j in range(0, len(prod_list)):
        a = precio_menor(prod_list, lista[j])
        a = a["price"]
        costosmenores.append(a)
    s = 0
    for n in range(0, len(costosmenores)):
        s = s + costosmenores[n]
    return s


def av_prod_price(listaproducto):  # precio prom de cada producto
    a = 0
    for el in range(0, len(listaproducto)):
        c = listaproducto[el]
        priceprod = c["price"]
        a = a + priceprod
    p = a / (len(listaproducto))
    return p


def average_price(prod_list, lista):
    acbp = 0
    for j in range(0, len(prod_list)):  # n de prod
        clave = lista[j]
        listaproducto = prod_list[clave]
        prom = av_prod_price(listaproducto)
        acbp = prom
    return acbp


def valida(num):
    return ((num >= 1) and (num <= 4))


products_huevo = [
    {
        "name": "Huevo",
        "price": 30.23,
        "store": "Walmart Bernardo Quintana"
    },
    {
        "name": "Huevo",
        "price": 40.98,
        "store": "HEB Juriquilla"
    },
    {
        "name": "Huevo",
        "price": 31.88,
        "store": "Chedraui Selecto Juriquilla"
    },
]
products_tortilla = [
    {
        "name": "Tortilla",
        "price": 15.50,
        "store": "Walmart Bernardo Quintana"
    },
    {
        "name": "Tortilla",
        "price": 12.30,
        "store": "HEB Juriquilla"
    },
    {
        "name": "Tortilla",
        "price": 22.50,
        "store": "Chedraui Selecto Juriquilla"
    },
]
products_jitomate = [
    {
        "name": "Jitomate",
        "price": 7.90,
        "store": "Walmart Bernardo Quintana"
    },
    {
        "name": "Jitomate",
        "price": 10.39,
        "store": "HEB Juriquilla"
    },
    {
        "name": "Jitomate",
        "price": 8.50,
        "store": "Chedraui Selecto Juriquilla"
    },
]

products_aceite = [
    {
        "name": "Aceite 1-2-3",
        "price": 48.90,
        "store": "Walmart Bernardo Quintana"
    },
    {
        "name": "Aceite 1-2-3",
        "price": 50.39,
        "store": "HEB Juriquilla"
    },
    {
        "name": "Aceite 1-2-3",
        "price": 64.5,
        "store": "Chedraui Selecto Juriquilla"
    },
]
products_frijol = [
    {
        "name": "Frijol flor de mayo",
        "price": 38.90,
        "store": "Walmart Bernardo Quintana"
    },
    {
        "name": "Frijol flor de mayo",
        "price": 29.39,
        "store": "HEB Juriquilla"
    },
    {
        "name": "Frijol flor de mayo",
        "price": 31.5,
        "store": "Chedraui Selecto Juriquilla"
    },
]

products_azucar = [
    {
        "name": "Azucar Morena",
        "price": 19.90,
        "store": "Walmart Bernardo Quintana"
    },
    {
        "name": "Azucar Morena",
        "price": 18.39,
        "store": "HEB Juriquilla"
    },
    {
        "name": "Azucar Morena",
        "price": 21.5,
        "store": "Chedraui Selecto Juriquilla"
    },
]
products = {
    "Huevo": products_huevo,
    "Tortilla": products_tortilla,
    "Jitomate": products_jitomate,
    "Aceite": products_aceite,
    "Frijol": products_frijol,
    "Azucar": products_azucar,


}
product_names = ["Huevo", "Tortilla", "Jitomate", "Aceite", "Frijol", "Azucar", ]
print("1. Mostrar el precio más bajo de algún producto")
print("2. Calcular el precio de la canasta básica")
print("3. Mostrar el precio promedio de todos los productos de la canasta básica")
opcion = int(input("INTRODUCE LA OPCIÓN: "))

if valida(opcion):
    if opcion == 1:
        show_products(product_names)
        option = int(input("Ingrese el número del producto que desee saber el menor costo"))
        p_name = product_names[option - 1]
        min_p = precio_menor(products, p_name)
        print(f"El mejor lugar para adquirir el producto es: {min_p['store']}, y su precio es de: ${min_p['price']}")

    elif opcion == 2:
        value = calculate_basic_basket(products, product_names)
        print(f" El valor total de la canasta básica es de: ${value}")

    elif opcion == 3:
        average1 = average_price(products, product_names)
        print(f"El precio promedio de todos los productos de la canasta básica es de: ${average1}")