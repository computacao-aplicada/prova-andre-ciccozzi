import re

def _calcular_digito(cpf_parcial: str) -> int:
    try:
        digitos = [int(d) for d in cpf_parcial]
        # Pesos decrescentes (10..2 para DV1, 11..2 para DV2)
        pesos = range(len(digitos) + 1, 1, -1)
        
        soma_ponderada = sum(d * p for d, p in zip(digitos, pesos))
        resto = soma_ponderada % 11
        
        return 0 if resto < 2 else 11 - resto
    except (ValueError, TypeError):
        return -1 # Retorna um valor inválido em caso de erro

def validar_cpf(cpf: str) -> bool:
    # Garante que a entrada é uma string e não está vazia
    if not isinstance(cpf, str) or not cpf.strip():
        return False

    # Sanitiza a entrada, removendo caracteres não numéricos
    cpf_limpo = re.sub(r'\D', '', cpf)

    # 3. Verifica se o CPF tem 11 dígitos
    if len(cpf_limpo) != 11:
        return False

    # 4. Rejeita sequências de dígitos repetidos
    if len(set(cpf_limpo)) == 1:
        return False
        
    # 5. Calcula e compara os dígitos verificadores
    try:
        # Calcula e compara o primeiro dígito verificador (DV1)
        dv1_calculado = _calcular_digito(cpf_limpo[:9])
        if dv1_calculado != int(cpf_limpo[9]):
            return False
        
        # Calcula e compara o segundo dígito verificador (DV2)
        dv2_calculado = _calcular_digito(cpf_limpo[:10])
        if dv2_calculado != int(cpf_limpo[10]):
            return False
    except (ValueError, IndexError):
        return False # contra erros de conversão ou índice

    return True