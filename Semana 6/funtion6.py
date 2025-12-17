def alphabetic_string ():
    frase = "caramba-loca-peligro-inminente"
    frase_list = frase.split("-")
    frase_list.sort()
    frase_list = "-".join(frase_list)
    print(frase_list)

alphabetic_string()