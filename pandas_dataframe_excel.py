import pandas as pd

def criar_dataframe():
    # Criando um DataFrame vazio
    df = pd.DataFrame(columns=['Nome', 'Idade', 'Sexo'])
    return df

def adicionar_dados(df, nome, idade, sexo):
    # Adicionando uma nova linha ao DataFrame
    new_row = pd.DataFrame({'Nome': [nome], 'Idade': [idade], 'Sexo': [sexo]})
    df = pd.concat([df, new_row], ignore_index=True)
    return df

def filtrar_dados(df, coluna, valor):
    # Filtrando o DataFrame com base em uma coluna e valor específicos
    df_filtrado = df[df[coluna] == valor]
    return df_filtrado

def exportar_para_excel(df, nome_arquivo):
    # Exportando o DataFrame para um arquivo Excel usando 'xlsxwriter' como engine
    df.to_excel(nome_arquivo + ".xlsx", index=False, engine='xlsxwriter')
    print(f"DataFrame exportado para '{nome_arquivo}.xlsx' com sucesso!")

def main():
    # Criar um DataFrame vazio
    df = criar_dataframe()

    while True:
        print("\nOpções:")
        print("1. Adicionar dados")
        print("2. Filtrar dados")
        print("3. Exportar para Excel")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            sexo = input("Sexo: ")
            df = adicionar_dados(df, nome, idade, sexo)
            print("Dados adicionados com sucesso!")

        elif opcao == '2':
            coluna = input("Nome da coluna para filtrar: ")
            valor = input("Valor para filtrar: ")
            df_filtrado = filtrar_dados(df, coluna, valor)
            print("\nDados filtrados:")
            print(df_filtrado)

        elif opcao == '3':
            nome_arquivo = input("Nome do arquivo Excel para exportar: ")
            exportar_para_excel(df, nome_arquivo)

        elif opcao == '4':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()