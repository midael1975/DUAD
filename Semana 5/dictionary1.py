information_of_hotel = {
    'nombre': 'America',
    'numero_de_estrellas' : 5,
    'habitaciones': [
        {
            'numero': 50,
            'piso': 5,
            'precio_por_noche': 100
        },
        {
            'numero': 60,
            'piso': 6,
            'precio_por_noche': 120
        }
    ]
    
}

print(information_of_hotel['habitaciones'][0]['numero'])
print(information_of_hotel['habitaciones'])
print(information_of_hotel['nombre'])
print(information_of_hotel['numero_de_estrellas'])
