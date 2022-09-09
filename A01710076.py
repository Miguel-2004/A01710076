products  = [
    {
        "name" : "Huevo",
        "price" : 15.50,
        "store" : "Walmart Bernardo Quintana"
    },
    {
        "name" : "Aceite",
        "price" : 22.50,
        "store" : "Walmart Bernardo Quintana"
    },
    {
        "name" : "Tortilla",
        "price" : 32.50,
        "store" : "Walmart Bernardo Quintana"
    },
]
def calculate_basic_basket():
    total=0
    for product in products:
        total=total+product["price"]
    return total 
def average_price():
    average = calculate_basic_basket()/len(products)
    return average
    
def valida (num):
    return ((num>=1) and (num<=4))

opcion = int (input("INTRODUCE LA OPCIÓN: "))

if valida(opcion):
    
 if opcion == 1:
     value=calculate_basic_basket()  
     print(f" El valor total de la canasta básica es : {value}")
    
 elif opcion == 2:
     average1=average_price()
     print (f"El precio promedio de la canasta básica es : {average1}")



