from typing import TypeVar, Type

T = TypeVar('T')

def pedir_tipado(msg: str, tipo: Type[T]) -> T:
     while True: 
        try: 
            return tipo(input(msg))
        except (ValueError, TypeError):
            print(f"Digite um valor do tipo '{tipo.__name__}'!")

