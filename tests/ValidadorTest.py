import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(project_root, 'src'))

from Validador import validar_cpf

testes_validos = {
    "CPF válido com máscara": "529.982.247-25",
    "CPF válido sem máscara": "52998224725",
    "CPF válido com espaços": " 529.982.247-25 ",
}

# CPFs que DEVEM ser considerados INVÁLIDOS
testes_invalidos = {
    "Entrada Nula (None)": None,
    "Entrada Vazia": "",
    "Entrada com apenas espaços": "   ",
    "Tamanho menor que 11": "1234567890",
    "Tamanho maior que 11": "123456789012",
    "Com caractere inválido": "529.982.247-2X",
    "Sequência de '1' repetidos": "11111111111",
    "Sequência de '0' repetidos": "000.000.000-00",
    "DV1 incorreto": "529.982.247-15",
    "DV2 incorreto": "529.982.247-24",
    "Ambos DVs incorretos": "123.456.789-00",
}

def executar_testes():
    """
    Executa todos os testes definidos e imprime os resultados.
    """
    print("--- INICIANDO TESTES DO VALIDADOR DE CPF ---")
    total_testes = 0
    falhas = 0

    #  casos que devem retornar True
    print("\n[+] Testando CPFS VÁLIDOS:")
    for nome_teste, cpf in testes_validos.items():
        total_testes += 1
        if validar_cpf(cpf):
            print(f"  PASSOU: {nome_teste}")
        else:
            print(f"  FALHOU: {nome_teste} (esperado: True, obtido: False)")
            falhas += 1

    #  casos que devem retornar False
    print("\n[+] Testando CPFs INVÁLIDOS:")
    for nome_teste, cpf in testes_invalidos.items():
        total_testes += 1
        if not validar_cpf(cpf):
            print(f"  PASSOU: {nome_teste}")
        else:
            print(f"  FALHOU: {nome_teste} (esperado: False, obtido: True)")
            falhas += 1
            
    # Relatório final
    print("\n--- FIM DOS TESTES ---")
    if falhas == 0:
        print(f"Resultado: SUCESSO! Todos os {total_testes} testes passaram.")
    else:
        print(f"Resultado: FALHA! {falhas} de {total_testes} testes falharam.")
    print("-" * 26)


if __name__ == "__main__":
    executar_testes()