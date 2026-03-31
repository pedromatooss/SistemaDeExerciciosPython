def executar(torre):

    def torre_hanoi(n, origem, destino, auxiliar):
        if n == 1:
            print(f"Mover disco 1 de {origem} para {destino}")
            return
        # Move n-1 discos da origem para o auxiliar
        torre_hanoi(n-1, origem, auxiliar, destino)
        # Move o disco maior para o destino
        print(f"Mover disco {n} de {origem} para {destino}")
        # Move os n-1 discos do auxiliar para o destino
        torre_hanoi(n-1, auxiliar, destino, origem)

    # Exemplo com 3 discos
    torre_hanoi(torre, 'A', 'C', 'B')
