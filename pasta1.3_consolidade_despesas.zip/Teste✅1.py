import pandas as pd

arquivos = ['1T2025.csv', '2T2025.csv', '3T2025.csv']
dfs_validos = []

for arquivo in arquivos:
    print(f"\nLendo arquivo: {arquivo}")

    df = pd.read_csv(arquivo, sep=';', engine='python')

    # Junta todo o texto da linha para facilitar a busca
    contem_eventos = df.astype(str).apply(
        lambda linha: linha.str.contains(
            'Eventos/Sinistros', case=False, na=False
        ).any(),
        axis=1
    ).any()

    if contem_eventos:
        print("✔ Contém Despesas com Eventos/Sinistros")
        dfs_validos.append(df)
    else:
        print("✖ Não contém Eventos/Sinistros — ignorado")

# Junta somente os arquivos válidos
if dfs_validos:
    df_final = pd.concat(dfs_validos)
    print("\nDados finais:")
    print(df_final.head())
else:
    print("\nNenhum arquivo com Eventos/Sinistros foi encontrado.")
