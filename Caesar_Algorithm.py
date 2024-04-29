#Algoritmo Caesar Vigenere
#En este algoritmo encriptaremos un input pasado como 'message' con una 'key' definiendo la vareiable enc_alg (encryption_alorithm)
#Defino los inputs del usuario
quest = input('Inserte \'E\' si desea encriptar un mensaje o \'D\' si desea desencriptar un mensaje:\n')
message = input('Inserta el mensaje a encriptar o desencriptar:\n')
key = input('Inserta la llave de encriptado o desencriptado:\n')

def enc_alg(message , key, direction=1):
    # arriba declaramos los parametros, el parametro direction tiene como valor predeterminado el 1, si no se declara en la llamada a la funcion
    # defino el alfabeto para encriptar
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # defino la variable encryption que sera la encriptacion o desencriptacion final
    encryption = ''
    # defino la variable new_index para los indices sobre los que se tomaran las letras del abecedario que formaran el mensaje encriptado
    new_index = ''
    # defino key_index en 0 para ir sumando uno a uno conforme se vayan completando las letras
    key_index = 0
    for char in message.lower():
        if not char.isalpha():
            #isalpha es una funcion built-in para detectar valores que no son letras
            encryption += char
        else:
            # encuentro los caracteres de la key en el alfabeto
            key_char = alphabet.find(key[key_index % len(key)])
            key_index += 1
            # encuentro el indice de cada letra del mensaje en el alfabeto
            index = alphabet.find(char)
            # hago new_index con el sumatorio de los indices hallados de la letra que sigue el mensaje y la letra de la key
            new_index = alphabet[(index + (key_char * direction)) % len(alphabet)]
            # sumo cada letra a encryption hasta formar el mensaje encriptado o desencriptado
            encryption += new_index
    return encryption
    #usamos return como ultima instruccion de la funcion, y declarar el final de la misma

encryption_alg = enc_alg(message, key, 1)
decryption_alg = enc_alg(message, key, -1)
#multiplicamos por -1 en direction para que la funcion se ejecute justo al reves para desencriptar
if quest.upper() == 'E':
    print(f'your encrypted message is \'{encryption_alg}\'')
elif quest.upper() == 'D':
    print(f'your decrypted message is \'{decryption_alg}\'')