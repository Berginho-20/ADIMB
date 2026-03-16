from bdd import listar_alunos, inserir_aluno, buscar_aluno_por_nome, excluir_aluno


def menu():
    while True:
        print("\n" + "=" * 30)
        print("   SISTEMA ACADEMIA v1.0")
        print("=" * 30)
        print("1 - Inserir Novo Aluno")
        print("2 - Listar Todos os Alunos")
        print("3 - Buscar Aluno por Nome")
        print("4 - Apagar Aluno (por ID)")
        print("5 - Atualizar Aluno (por ID)")
        print("0 - Sair")

        opcao = input("\nO que você deseja fazer? ")

        if opcao == '1':
            print("\n" + "-" * 30)
            print("CADASTRO COMPLETO DE ALUNO")
            print("-" * 30)

            # Coletando TODAS as informações
            nome = input("1. Nome Completo: ")
            if not nome:
                print("❌ Erro: O nome é obrigatório para o cadastro.")
                continue

            modalidade = input("2. Modalidade (ex: Jiu-Jitsu, Muay Thai): ")
            graduacao = input("3. Graduação/Faixa: ")
            endereco = input("4. Endereço: ")
            nascimento = input("5. Data de Nascimento (dd/mm/aaaa): ")
            cpf = input("6. CPF: ")
            celular = input("7. Celular/WhatsApp: ")
            data_ini = input("8. Data de Início (dd/mm/aaaa): ")
            vencimento = input("9. Dia do Vencimento (apenas o número): ")
            valor = input("10. Valor da Mensalidade: ")
            plano = input("11. Plano (Mensal, Trimestral, Anual): ")
            pagamento = input("12. Forma de Pagamento (Pix, Cartão, Dinheiro): ")

            # Organizando os dados exatamente na ordem que o bdd.py espera (12 campos)
            dados = (
                nome, modalidade, graduacao, endereco, nascimento,
                cpf, celular, data_ini, vencimento, valor, plano, pagamento
            )

            try:
                inserir_aluno(dados)
                print(f"\n✅ Aluno {nome} cadastrado com sucesso em todos os tópicos!")
            except Exception as e:
                print(f"\n❌ Erro ao salvar no banco de dados: {e}")

        elif opcao == '2':
            print("\n--- LISTA DE ALUNOS ---")
            alunos = listar_alunos()
            for a in alunos:
                print(f"ID: {a[0]} | Nome: {a[1]} | Modalidade: {a[2]}")


        elif opcao == '3':

            nome_busca = input("Digite o nome para buscar: ")

            resultados = buscar_aluno_por_nome(nome_busca)

            if resultados:

                # Cabeçalho da tabela (Ajuste as larguras conforme achar melhor)

                # O sinal de < significa alinhado à esquerda e o número é o espaço

                header = (f"{'ID':<4} | {'NOME':<25} | {'MODAL':<12} | {'GRAD':<10} | "

                          f"{'VENC':<5} | {'VALOR':<8} | {'CELULAR':<15} | {'PLANO':<10}")

                print("\n" + header)

                print("-" * len(header))

                for r in resultados:
                    # r[0]=ID, r[1]=Nome, r[2]=Modalidade, r[3]=Graduação,

                    # r[9]=Vencimento, r[10]=Valor, r[7]=Celular, r[11]=Plano

                    print(f"{str(r[0]):<4} | {str(r[1])[:25]:<25} | {str(r[2])[:12]:<12} | "

                          f"{str(r[3])[:10]:<10} | {str(r[9]):<5} | {str(r[10]):<8} | "

                          f"{str(r[7]):<15} | {str(r[11]):<10}")

            else:

                print("\n❌ Nenhum aluno encontrado.")

        elif opcao == '4':
            id_del = input("Digite o ID do aluno que deseja APAGAR: ")
            confirmar = input(f"Tem certeza que deseja apagar o ID {id_del}? (s/n): ")
            if confirmar.lower() == 's':
                excluir_aluno(id_del)
                print("🗑️ Aluno removido!")

        elif opcao == '5':
            id_alu = input("Digite o ID do aluno que deseja atualizar: ")

            # Dicionário para facilitar a escolha da coluna
            colunas = {
                '1': 'nome', '2': 'modalidade', '3': 'graduacao',
                '4': 'endereco', '5': 'nascimento', '6': 'cpf',
                '7': 'celular', '8': 'data_inicio', '9': 'vencimento_dia',
                '10': 'valor', '11': 'plano', '12': 'pagamento'
            }

            print("\nQual informação deseja alterar?")
            for num, nome in colunas.items():
                print(f"{num} - {nome.capitalize()}")

            escolha = input("\nEscolha o número do campo: ")

            if escolha in colunas:
                campo_selecionado = colunas[escolha]
                novo_dado = input(f"Digite o novo valor para {campo_selecionado}: ")

                try:
                    from bdd import atualizar_aluno  # Garante que a função está disponível
                    atualizar_aluno(id_alu, campo_selecionado, novo_dado)
                    print(f"\n✅ {campo_selecionado.capitalize()} atualizado com sucesso!")
                except Exception as e:
                    print(f"❌ Erro ao atualizar: {e}")
            else:
                print("⚠️ Opção de campo inválida!")

        elif opcao == '0':
            print("Saindo do sistema... Até logo!")
            break

        else:
            print("⚠️ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
