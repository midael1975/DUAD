import json

def load_pokemons(file_name):
    """Read the JSON file and return the list of Pokemon."""
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Archivo no encontrado, se creará uno nuevo.")
        return []
    except json.JSONDecodeError:
        print("Error en el formato del archivo, se iniciará vacío.")
        return []

def save_pokemons(file_name, pokemons):
    """Save the list of Pokemon in the JSON file."""
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(pokemons, f, indent=2, ensure_ascii=False)

def ask_pokemon():
    """Request the user for information about a new Pokémon."""
    name = input("Nombre del Pokémon: ")
    type = input("Tipo(s) del Pokémon (separados por coma): ").split(",")
    type = [t.strip() for t in type]

    print("Introduce las estadísticas base:")
    hp = int(input("HP: "))
    attack = int(input("Attack: "))
    defense = int(input("Defense: "))
    sp_attack = int(input("Sp. Attack: "))
    sp_defense = int(input("Sp. Defense: "))
    speed = int(input("Speed: "))

    return {
        "name": {"english": name},
        "type": type,
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed
        }
    }

def main():
    file = "pokemones.json"

    # 1. Leer archivo
    pokemons = load_pokemons(file)

    # 2. Pedir nuevo Pokémon
    new_pokemon = ask_pokemon()

    # 3. Agregar a la lista
    pokemons.append(new_pokemon)

    # 4. Guardar archivo
    save_pokemons(file, pokemons)

    print(f"{new_pokemon['name']['english']} agregado correctamente al archivo {file}.")

if __name__ == "__main__":
    main()
