


def palindrome(palabra):
    palabra = palabra.replace(" ", " ")
    palabra =palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input("escribe una palabra: ")
    es_palindrome = palindrome(palabra)
    if es_palindrome ==True:
        print("es palindrome") 
    else:
        print("no es palindrome")


if __name__ == "__main__" :
    run()