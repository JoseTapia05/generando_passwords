import string
import secrets

def contiene_mayusculas(password) -> bool:
    for letra in password:
        if letra.isupper():
            return True
        
    return False

def contiene_simbolos(password) -> bool:
    for letra in password:
        if letra in string.punctuation:
            return True
        
    return False

def generar_password(longitud, tiene_simbolos, tiene_mayusculas) -> str:
    combinacion = string.ascii_lowercase + string.digits
    
    if tiene_simbolos:
        combinacion += string.punctuation
        
    if tiene_mayusculas:
        combinacion += string.ascii_uppercase
        
    longitud_combinacion = len(combinacion)
    
    nuevo_password = ' '
    
    for _ in range(longitud):
        nuevo_password += combinacion[secrets.randbelow(longitud_combinacion)]
        
    return nuevo_password

if __name__=='__main__':
    for i in range(1,6):
        nuevo_pass = generar_password(longitud=15, tiene_simbolos=True, tiene_mayusculas=True)
        especificaciones = (f'Mayusculas: {contiene_mayusculas(nuevo_pass)}, ' f'Simbolos: {contiene_simbolos(nuevo_pass)}')
        print(f'{i} -> {nuevo_pass} ({especificaciones})')