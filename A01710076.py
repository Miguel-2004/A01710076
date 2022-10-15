def precio_menor (prod_list, p_name):
    product_data = prod_list [p_name]
    menor = product_data[0]
    for dic in product_data:
        if dic["price"]<menor["price"]:
            menor = dic
    return menor 

def show_products (names):
    index = 0 
    while index < len(names):
        value = names[index]
        index = index +1
        print(f"{index}- {value}")
        
#def calculate_basic_basket():
    
    
def valida (num):
    return ((num>=1) and (num<=4))

products_huevo  = [
    {
        "name" : "Huevo",
        "price" : 30.23,
        "store" : "Walmart Bernardo Quintana"
    },
    {
        "name" : "Huevo",
        "price" : 40.98,
        "store" : "HEB Juriquilla"
    },
    {
        "name" : "Huevo",
        "price" : 31.88,
        "store" : "Chedraui Selecto Juriquilla"
    },
]
products_tortilla  = [
    {
        "name" : "Tortilla",
        "price" : 15.50,
        "store" : "Walmart Bernardo Quintana"
    },
    {
        "name" : "Tortilla",
        "price" : 12.30,
        "store" : "HEB Juriquilla"
    },
    {
        "name" : "Tortilla",
        "price" : 22.50,
        "store" : "Chedraui Selecto Juriquilla"
    },
]
products_jitomate  = [
    {
        "name" : "Jitomate",
        "price" : 7.90,
        "store" : "Walmart Bernardo Quintana"
    },
    {
        "name" : "Jitomate",
        "price" : 10.39,
        "store" : "HEB Juriquilla"
    },
    {
        "name" : "Jitomate",
        "price" : 8.50,
        "store" : "Chedraui Selecto Juriquilla"
    },
]

products_aceite  = [
    {
        "name" : "Aceite 1-2-3",
        "price" : 48.90,
        "store" : "Walmart Bernardo Quintana"
    },
    {
        "name" : "Aceite 1-2-3",
        "price" : 50.39,
        "store" : "HEB Juriquilla"
    },
    {
        "name" : "Aceite 1-2-3",
        "price" : 64.5,
        "store" : "Chedraui Selecto Juriquilla"
    },
]

products = {
    "Huevo": products_huevo,
    "Tortilla": products_tortilla,
    "Jitomate": products_jitomate, 
    "Aceite": products_aceite,
}
product_names = ["Huevo", "Tortilla", "Jitomate", "Aceite"]

#precio_m_huevo  = precio_menor(products_huevo)
#prod despupes de m seria el prod que busca el usuario. esto va dentro del segundo if o sea 1 if es op 1 y 2do if es el producto que busca
#print(precio_m_huevo)
#print("El huevo está a ",precio_m_huevo[0]," en ",precio_m_huevo[1])

opcion = int (input("INTRODUCE LA OPCIÓN: "))

if valida(opcion):
    if opcion ==1:
        show_products(product_names)
        option = int(input("Ingrese el número del producto que desee saber el menor costo"))
        p_name = product_names[option-1]
        min_p = precio_menor(products, p_name)
        print(f"El mejor lugar para adquirir el producto es: {min_p['store']}, y su precio es {min_p['price']}")
       
        
 #if opcion == 1:
     #value=calculate_basic_basket() 
     #print(f" El valor total de la canasta básica es : {value}")
    
 #elif opcion == 2:
     #average1=average_price()
     #print (f"El precio promedio de la canasta básica es :# {average1}")
