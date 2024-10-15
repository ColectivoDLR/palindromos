limit_inf = int(input("Ingresa el rango inferior: "))
limit_sup = int(input("Ingresa el rango superior: "))

# Verificar que el límite inferior no sea mayor que el superior
if limit_inf > limit_sup:

    print("El límite inferior debe ser menor que el superior.")
else:

    palindromo = []

    # Iterar a través del rango especificado
    for numero in range(limit_inf, limit_sup):  # hace falta incluir el límite superior
        numero_1 = str(numero)
        if numero_1 == numero_1[::-1]:
            palindromo.append(numero)

    print(f"los numeros encontrados e"
          f"n el rango son : {palindromo}")