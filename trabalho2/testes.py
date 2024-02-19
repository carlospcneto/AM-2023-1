import pandas as pd

# Criar o DataFrame original
data = {'IdNum': ['x135', 'x135', 'x114', 'x114', 'x114'],
        'Produtos': ['Leite', 'Nescau', 'Pao', 'Leite', 'Cafe']}
df = pd.DataFrame(data)

# Adicionar uma coluna "Quantidade" para representar a contagem de produtos
df['Quantidade'] = True

# Fazer o pivotamento
pivot_df = df.pivot(index='IdNum', columns='Produtos', values='Quantidade').fillna(False)

# Resetar o índice
pivot_df.reset_index(inplace=True)

# Imprimir o DataFrame pivoteado
print(pivot_df)