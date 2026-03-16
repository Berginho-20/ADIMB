import pandas as pd
import numpy as np
from bdd import criar_tabela, inserir_aluno

# 1. Garante que a tabela existe
criar_tabela()

# 2. Carrega a planilha
df = pd.read_excel('Alunos da academia.xlsx')

# Transforma todas as colunas de data em texto simples (String)
for col in df.columns:
    if pd.api.types.is_datetime64_any_dtype(df[col]):
        df[col] = df[col].dt.strftime('%d/%m/%Y') # Transforma em 16/03/2026

# ESSA LINHA É A CHAVE: transforma tudo que é vazio na planilha em None (NULL)
df = df.replace({np.nan: None})

# IMPORTANTE: O nome das colunas no 'df' deve ser igual ao da planilha
for index, linha in df.iterrows():
    dados = (
        linha['Nome'],
        linha['Modalidade'],
        linha['Graduação'],
        linha['Endereço'],
        linha['Nascimento'],
        linha['CPF'],
        linha['Celular'],
        linha['Início'],
        linha['Vencimento'],
        linha['Valor'],
        linha['Plano'],
        linha['Pagamento']
    )
    try:
        inserir_aluno(dados)
        print(f"✅ Salvo: {linha.get('nome')}")
    except Exception as e:
        # Isso vai nos dizer se o erro é no banco ou nos dados
        print(f"❌ Erro em {linha.get('nome')}: {e}")
        # Opcional: print(dados) # Isso ajuda a ver se os dados estão na ordem certa

print("Importação concluída!")
