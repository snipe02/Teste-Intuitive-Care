import pandas as pd

# Carregar os arquivos
df1 = pd.read_csv('1T2025.csv', sep=';')
df2 = pd.read_csv('2T2025.csv', sep=';')
df3 = pd.read_csv('3T2025.csv', sep=';')

# Combinar os dados
df = pd.concat([df1, df2, df3])

# Criar colunas Trimestre e Ano baseadas no trimestre de origem
# Adicionar coluna Trimestre indicando de qual arquivo veio cada registro
df1['Trimestre'] = 1
df2['Trimestre'] = 2
df3['Trimestre'] = 3

# Combinar novamente com a coluna Trimestre
df = pd.concat([df1, df2, df3])

# Adicionar coluna Ano (todos os dados são de 2025)
df['Ano'] = 2025

# Verificar e renomear colunas para o formato desejado
# Primeiro, vamos verificar quais colunas existem
print("Colunas disponíveis nos dados:")
print(df.columns.tolist())

# Supondo que as colunas originais tenham nomes diferentes, vamos mapeá-las
# Você precisará ajustar estes nomes conforme seus arquivos CSV

# Exemplo de mapeamento (ajuste conforme seus dados):
# Se a coluna CNPJ existe com outro nome, faça:
if 'CNPJ' in df.columns:
    # Se já existe CNPJ, mantenha
    pass
elif 'cnpj' in df.columns:
    df['CNPJ'] = df['cnpj']
elif 'Cnpj' in df.columns:
    df['CNPJ'] = df['Cnpj']

# Similar para RazaoSocial
if 'RazaoSocial' in df.columns:
    pass
elif 'razao_social' in df.columns:
    df['RazaoSocial'] = df['razao_social']
elif 'Empresa' in df.columns:
    df['RazaoSocial'] = df['Empresa']
elif 'Nome' in df.columns:
    df['RazaoSocial'] = df['Nome']

# Similar para ValorDespesas
if 'ValorDespesas' in df.columns:
    pass
elif 'valor_despesas' in df.columns:
    df['ValorDespesas'] = df['valor_despesas']
elif 'Despesas' in df.columns:
    df['ValorDespesas'] = df['Despesas']
elif 'valor' in df.columns:
    df['ValorDespesas'] = df['valor']

# Tratar problemas identificados:

# 1. CNPJs duplicados com razões sociais diferentes
print(f"\nCNPJs duplicados encontrados: {df['CNPJ'].duplicated().sum()}")

# Para duplicados, manteremos o primeiro registro
df = df.drop_duplicates(subset=['CNPJ', 'Trimestre', 'Ano'], keep='first')

# 2. Valores zerados ou negativos
print(f"Registros com valores zerados ou negativos: {(df['ValorDespesas'] <= 0).sum()}")

# Opção 1: Manter os valores (apenas para análise)
# Opção 2: Remover valores inválidos
df = df[df['ValorDespesas'] > 0]

# 3. Trimestres com formatos inconsistentes (já resolvido ao adicionar coluna Trimestre)

# Selecionar apenas as colunas necessárias
colunas_finais = ['CNPJ', 'RazaoSocial', 'Trimestre', 'Ano', 'ValorDespesas']

# Verificar se todas as colunas existem
colunas_existentes = [col for col in colunas_finais if col in df.columns]
if len(colunas_existentes) < len(colunas_finais):
    print(f"\nAviso: Algumas colunas não foram encontradas")
    print(f"Colunas encontradas: {colunas_existentes}")
    print(f"Colunas esperadas: {colunas_finais}")

    # Tentar criar DataFrame apenas com colunas existentes
    df_final = df[colunas_existentes]
else:
    df_final = df[colunas_finais]

# Salvar o arquivo consolidado
df_final.to_csv('consolidado_2025.csv', index=False, sep=';')

print(f"\nConsolidação concluída!")
print(f"Total de registros: {len(df_final)}")
print(f"Arquivo salvo como: consolidado_2025.csv")
print(f"Colunas finais: {df_final.columns.tolist()}")

# Mostrar amostra dos dados
print("\nAmostra  dados consolidados:")
print(df_final.head())