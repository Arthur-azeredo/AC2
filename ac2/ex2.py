def calcula_salario(valor_hora, num_hora, irpf=0.275):
    
    salario_liquido = (valor_hora * num_hora) * irpf

    return salario_liquido

def main():
    print(calcula_salario(2, 10))

main()
    