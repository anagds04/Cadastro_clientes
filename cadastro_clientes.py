# Lista para armazerar os cadastros.
# {}chave []colchetes ()parênteses .

clientes = []

while True:
    print("\nCadastro de clientes")
    nome = input("Nome:")
    idade = int(input("Idade:"))
    cidade = input("Cidade onde nasceu:")
    
    
    #Adicionando o cliente como dicionário na lista.
    
    cliente = {"nome" : nome, "idade": idade, "cidade": cidade}
    clientes.append(cliente)
    
    #Perguntar se quer continuar a cadastrar um novo usuário.
    continuar = input("Deseja cadastrar novos clientes ?(s/n:)").strip().lower()
    if continuar != "s":
        break
    
    #exibindo os cadastros de clientes 
print("\nClientes Cadastrados:")
for i, cliente in enumerate(clientes, start=1):
    print(f"{i}. Nome: {cliente['nome']}, Idade: {cliente['idade']}, Cidade: {cliente['cidade']}")
    
    
