import csv

def ask_videogame():
    nombre = input('Nombre: ').strip()
    genero = input('Genero: ').strip()
    desarrollador = input('Desarrollador: ').strip()
    esrb = input('Clasificacion Esrb: ').strip()
    
    return {
        'nombre': nombre,
        'genero': genero,
        'desarrollador': desarrollador,
        'Clasificacion Esrb': esrb
    
    }

def save_csv(videogames, output_file):
    headers = ['nombre', 'genero', 'desarrollador', 'Clasificacion Esrb']
    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers, delimiter='\t')
        writer.writeheader()
        writer.writerows(videogames)

    print(f'\nSe han guardados {len(videogames)} videojuegos en el archivo \'{output_file}\'.')

def main():
    videogames = []
    number_videogames = int(input('Cuantos videojuegos deseas guardar: '))

    for i in range(number_videogames):
        print(f'\nVideojuego {i+1}:')
        videogame = ask_videogame()
        videogames.append(videogame)
    save_csv(videogames, 'videogames.tsv')

if __name__ == "__main__":
    main()