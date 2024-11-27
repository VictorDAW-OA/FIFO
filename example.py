OK_RESULT = 'yes'
FATAL_RESULT = 'no'
PEPE = 9
CONTO = 121654951651651
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
    

def pay_referee_taxes():

    def check_conto():
        return CONTO

    if check_conto > 100000:
        CONTO - 100000

check_if_aprove_or_not()
pay_referee_taxes()