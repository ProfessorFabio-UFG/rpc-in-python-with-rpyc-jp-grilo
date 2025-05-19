import rpyc
from constRPYC import *

def menu():
    print("\nEscolha uma operação:")
    print("1 - Ver lista")
    print("2 - Adicionar elemento")
    print("3 - Remover elemento")
    print("4 - Atualizar elemento")
    print("5 - Buscar elemento por índice")
    print("6 - Limpar lista")
    print("7 - Tamanho da lista")
    print("8 - Ver tutorial")
    print("9 - Rodar demonstração automática")
    print("0 - Sair")

def tutorial():
    print("""
=== Tutorial de Uso do Cliente RPC ===

1. Execute o servidor normalmente:
   python3 server.py

2. Em outro terminal, execute o cliente:
   python3 client.py

3. No menu do cliente, escolha a operação desejada digitando o número correspondente:
   1: Ver a lista atual.
   2: Adicionar um elemento ao final da lista.
   3: Remover um elemento (primeira ocorrência).
   4: Atualizar o valor de um elemento em um índice específico.
   5: Buscar o valor de um elemento por índice.
   6: Limpar toda a lista.
   7: Ver o tamanho da lista.
   8: Ver este tutorial novamente.
   9: Rodar demonstração automática.
   0: Sair do programa.

4. Siga as instruções na tela para inserir valores ou índices quando solicitado.
""")

def demo(conn):
    print("\n--- Demonstração automática ---")
    print("Limpando lista para demonstração:", conn.root.clear())
    print("Adicionando 'a':", conn.root.append('a'))
    print("Adicionando 'b':", conn.root.append('b'))
    print("Adicionando 'c':", conn.root.append('c'))
    print("Lista atual:", conn.root.value())
    print("Atualizando índice 1 para 'z':", conn.root.update(1, 'z'))
    print("Lista atual:", conn.root.value())
    print("Removendo 'a':", conn.root.remove('a'))
    print("Lista atual:", conn.root.value())
    print("Elemento no índice 0:", conn.root.get(0))
    print("Tamanho da lista:", conn.root.length())
    print("Limpando lista:", conn.root.clear())
    print("Lista final:", conn.root.value())
    print("--- Fim da demonstração ---\n")

conn = rpyc.connect(SERVER, PORT)
print("Bem-vindo ao cliente RPC para manipulação de vetor remoto!")

while True:
    menu()
    op = input("Opção: ").strip()
    if op == "1":
        print("Lista atual:", conn.root.value())
    elif op == "2":
        val = input("Valor para adicionar: ")
        print("Lista após append:", conn.root.append(val))
    elif op == "3":
        val = input("Valor para remover: ")
        print("Resultado:", conn.root.remove(val))
    elif op == "4":
        idx = int(input("Índice a atualizar: "))
        val = input("Novo valor: ")
        print("Lista após update:", conn.root.update(idx, val))
    elif op == "5":
        idx = int(input("Índice a buscar: "))
        print("Elemento:", conn.root.get(idx))
    elif op == "6":
        print("Lista limpa:", conn.root.clear())
    elif op == "7":
        print("Tamanho da lista:", conn.root.length())
    elif op == "8":
        tutorial()
    elif op == "9":
        demo(conn)
    elif op == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")