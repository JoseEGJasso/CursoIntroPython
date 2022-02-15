def agua_sobrante(astronautas, agua_actual, dias):
    for args in (astronautas,agua_actual,dias):
        if not str(args).isnumeric():
            raise TypeError(f'El argumento {args} no es un número')

    consumo_dia = astronautas * 11
    consumo_total = consumo_dia * dias
    restante = agua_actual - consumo_total
    if restante < 0:
        raise RuntimeError(f'PELIGRO! No hay suficiente agua para {astronautas} astronautas en los proximos {dias} dias')
    return f'Agua restante: {restante}'

try:
    agua_sobrante(5, 100, 2)
except RuntimeError as err:
    print(err)

agua_sobrante("3", "200", None)