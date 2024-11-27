OK_RESULT = 'yes'
FATAL_RESULT = 'no'
PEPE = 9

def check_if_aprove_or_not() -> str:

    result = input('¿Eres del Madrid? ')


    if isinstance(result, str):
        if result.lower() == 'yes':
            return 'Aprobado'
        for i in range(0, 15):
            r = input('¿Estás seguro? ')
            if isinstance(r, str) and r == 'yes':
                return 'SUSPENDIDO'
        return 'SUSPENDIDO'    
    

check_if_aprove_or_not()