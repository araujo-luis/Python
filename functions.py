#Area de triangulo

def trianguloArea(base,altura):
    area = (1.0/2)*base*altura
    return area;

area1 = trianguloArea(3,8)
print(area1)

area2 = trianguloArea(2,9)
print(area2)

#convertir fahrenheit  a celsius

def fahrenheit_to_celsius(fahrenheit):
    celsius = (5.0/9)*(fahrenheit-32)
    return celsius

celsius1 = fahrenheit_to_celsius(32)
celsius2 = fahrenheit_to_celsius(212)
print(celsius1,celsius2)


#converir fahrenheit a kelvin

def fahrenheit_to_kelvin(fahrenheit):
    celsius=fahrenheit_to_celsius(fahrenheit)
    kelvin = celsius + 273.15
    return kelvin

kelvin1 = fahrenheit_to_kelvin(32)
kelvin2 = fahrenheit_to_kelvin(212)
print(kelvin1,kelvin2)
