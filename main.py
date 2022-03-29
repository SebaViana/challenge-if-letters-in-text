article = open("DATA/magazine-article.txt", "r", encoding= "utf_8").read()
letter = open("DATA/letter.txt", "r", encoding= "utf_8").read()

def returnAlpha(text): # funcion que extrae unicamente los caracteres alpha del un texto pasado como parámetro
    text_alpha = ""
    for character in text:
        if character.isalpha():
            text_alpha += character.lower() # método lower para no hacer distinciones entre mayúsculas y minúsculas
    text_alpha_sorted_list = sorted(text_alpha) # crea una lista para utilizar el metodo sroted, con el cual se ordenan A-Z todas las letras, para utilizar luego ordenadamente en la funcion returnAmmount
    text_alpha_sorted = "".join(text_alpha_sorted_list) # convierte la lista a string
    return text_alpha_sorted # devuelve un nuevo texto con unicamente carácteres alhpa y estando ordenado A-Z.

def returnAmmount(source_text_alpha): # crea un diccionario con letra como key y su cantidad como value.
    char_dict = {}
    for character in source_text_alpha:
        if character in char_dict: # si ya existe en el diccionario la key, suma uno al value.
            char_dict[character] += 1
        else: # si no existe en el diccionario la key, la crea y le asiga 1 como value.
            char_dict[character] = 1
    return char_dict

def checkIfPossible(text_alpha, char_dict): # funcion que comprueba si la consigna es realizable, si existe la letra y la cantidad en el articulo para escribir la carta deseada.
    characters_needed = [] # diccionario donde se agregaran los caracteres faltantes para poder escribir la carta, se utilizara en caso de que la consigna no sea realizable.
    possible = True # variable que asume inicialmente que la consiga es realizable, los condicionales cambiaran su valor en caso de esto no ser posible.
    for character in text_alpha:
        if character in char_dict:
            if char_dict[character] > 0: # si la letra se encuentra en el diccionario y es mayor a cero, resta uno de valor.
                char_dict[character] -= 1
            else: # al no restar más cantidad de una letra, la consigna es irrealizable. 
                possible = False
                characters_needed.append(character)
        else: # el caracter no se encuentra en el diccionario, por lo tanto, tampoco en el articulo de la revista. La consigna es irrealizable.
            possible = False
            characters_needed.append(character)
    
    if possible: # es realizable.
        print(f"Great😁! The letter can be written with the words given in the magazine article.") # resultado positivo
    else: # no es realizable.
        characters_needed_dict = returnAmmount(characters_needed)
        print(f"Oops😔, the letter can't be written with the words given in the magazine article.\nMissing letters: {characters_needed_dict}")

article_alpha = returnAlpha(article)

letter_alpha = returnAlpha(letter)

article_alpha_ammount = returnAmmount(article_alpha)

checkIfPossible(letter_alpha, article_alpha_ammount)        
