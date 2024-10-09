# Exercicio : Calcular  o índice de masa corporal (IMC).


def imc(estatura, peso):
    """
    Calcula o índice de massa corporal.
    """
    return peso / estatura**2


peso = float(input('Digita o teu peso (Kg): '))
estatura = float(input('Digita a tua estatura (m): '))

indice = imc(estatura, peso)

print('O IMC e: {}'.format(indice))
