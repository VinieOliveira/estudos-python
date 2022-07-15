hora = float(input("que horas são? "))

if hora >= 0.0 and hora < 12.0:
    print("Bom dia!")

elif hora >= 12.0 and hora < 18.0:
    print("Boa tarde!")

elif hora < 24:
    print("Boa noite!")
elif hora < 0 or hora > 24:
    print("Digite uma hora entre 0.00 e 24.00")