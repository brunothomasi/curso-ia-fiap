# Aplicação de Agricultura Digital - FarmTech Solutions
# Culturas: Soja (área retangular) e Milho (área circular)

culturas = ['Soja', 'Milho']
dados_soja = []  # Cada item: {'largura': float, 'comprimento': float, 'insumo': str, 'qtd_por_m2': float, 'ruas': int}
dados_milho = [] # Cada item: {'raio': float, 'insumo': str, 'qtd_por_m2': float, 'ruas': int}

#nome do arquivo que irá persistir os dados para consulta no R e para manter dados após reiniciar aplicação
filename = '../data/dados.csv'

#importa biblioteca math para cálculos matemáticos (pi)
import math

#importa biblioteca csv para manipulação de base de dados para uso no código R
import csv

#define função para calcular área da soja
def calcular_area_soja(largura, comprimento):
    return largura * comprimento

#define função para calcular área do milho
def calcular_area_milho(raio):
    return math.pi * raio ** 2

#define função para entrada de dados
def entrada_dados():
    while True:
        print('Escolha a cultura:')
        for i, c in enumerate(culturas):
            print(f'{i+1} - {c}')
        print('0 - Voltar ao menu')
        op = int(input('Opção: '))
        if op == 1:
            largura = float(input('Largura da área (m): '))
            comprimento = float(input('Comprimento da área (m): '))
            insumo = input('Nome do insumo: ')
            qtd = float(input('Quantidade do insumo por m²: '))
            ruas = int(input('Quantidade de ruas: '))

            total_insumo = calcular_area_soja(largura, comprimento) * qtd * ruas

            dados_soja.append({'area': calcular_area_soja(largura, comprimento), 'largura': largura, 'comprimento': comprimento, 'insumo': insumo, 'qtd_por_m2': qtd, 'ruas': ruas, 'total_insumo': total_insumo})

            salva_csv()
            break
        elif op == 2:

            raio = float(input('Raio da área (m): '))
            insumo = input('Nome do insumo: ')
            qtd = float(input('Quantidade do insumo por m²: '))
            ruas = int(input('Quantidade de ruas: '))

            total_insumo = calcular_area_milho(raio) * qtd * ruas

            dados_milho.append({'area': calcular_area_milho(raio), 'raio': raio, 'insumo': insumo, 'qtd_por_m2': qtd, 'ruas': ruas, 'total_insumo': total_insumo})
            salva_csv()
            break
        elif op == 0:
            break
        else:
            print('Opção inválida!')

#define função para saída de dados
def saida_dados(cultura=None):

    if cultura == 'Soja' or cultura is None:
        
        # Cabeçalho com tipo de cultura
        print('\n+---------------------------------------------------------------------------------------------+')
        print('| DADOS SOJA                                                                                  |')

        if(dados_soja):
            # Cabeçalho com colunas da tabela
            print('+----+------------------+---------+-------------+-------------+--------+------+---------------+')
            print('| ID | Insumo           | Largura | Comprimento |  Área (m²)  | Qtd/m² | Ruas |  Total Insumo |')
            print('|----|------------------|---------|-------------|-------------|--------|------+---------------|')

            for i, d in enumerate(dados_soja):
                print(f'|{i:>3} | {d["insumo"]:<16} | {d["largura"]:>7.2f} | {d["comprimento"]:>11.2f} |   {d["area"]:>9.2f} | {d["qtd_por_m2"]:>6} | {d["ruas"]:>4} | {d["total_insumo"]:>13.2f} |')

        else:
            print('| Nenhum dado de soja registrado                                                     |')

        print('+----+------------------+---------+-------------+-------------+--------+------+---------------+')
    if cultura == 'Milho' or cultura is None:
        # Cabeçalho com tipo de cultura
        print('\n+----------------------------------------------------------------------------------+')
        print('| DADOS MILHO                                                                      |')

        if(dados_milho):
            # Cabeçalho com colunas da tabela
            print('+----+------------------+---------+-------------+-------------+--------+-----------+')
            print('| ID | Insumo           |   Raio  |  Área (m²)  |   Qtd/m²    |  Ruas  |   Total   |')
            print('+----+------------------+---------+-------------+-------------+--------+-----------+')

            for i, d in enumerate(dados_milho):
                area = calcular_area_milho(d['raio'])
                total_insumo = area * d['qtd_por_m2'] * d['ruas']
                print(f'|{i:>3} | {d["insumo"]:<16} | {d["raio"]:>7.2f} | {area:>11.2f} |      {d["qtd_por_m2"]:>6} |   {d["ruas"]:>4} |{total_insumo:>10.2f} |')

        else:
            print('| Nenhum dado de milho registrado                                              |')

    print('+----+------------------+---------+-------------+-------------+--------+-----------+')
    #se cultura estiver definida e não estiver no array de culturas
    if cultura is not None and cultura not in culturas:
        print('Cultura inválida!')

#define função para atualizar dados
def atualizar_dados():
    while True:
        print('Escolha a cultura para atualizar:')
        for i, c in enumerate(culturas):
            print(f'{i+1} - {c}')
        print('0 - Voltar ao menu')

        op = int(input('Opção: '))
        if op == 1:
            saida_dados(culturas[op-1])
            if len(dados_soja) > 0:
                idx = int(input('Índice do dado a atualizar:'))
                if idx >= 0 and idx < len(dados_soja):
                    print(f'Atualizando dados da soja: {idx} (Deixe vazio para manter valor anterior)')
                    largura = input(f'Largura Anterior {dados_soja[idx]["largura"]}: Nova largura (m): ')
                    comprimento = input(f'Comprimento Anterior {dados_soja[idx]["comprimento"]}: Novo comprimento (m): ')
                    insumo = (f'Insumo Anterior {dados_soja[idx]["insumo"]}: Novo insumo: ')
                    qtd = input(f'Qtd/m² Anterior {dados_soja[idx]["qtd_por_m2"]}: Nova qtd por m²: ')
                    ruas = input(f'Ruas Anterior {dados_soja[idx]["ruas"]}: Nova qtd de ruas: ')

                    #se dados forem vazios mantem valor anterior
                    if not largura: largura = dados_soja[idx]["largura"]
                    if not comprimento: comprimento = dados_soja[idx]["comprimento"]
                    if not insumo: insumo = dados_soja[idx]["insumo"]
                    if not qtd: qtd = dados_soja[idx]["qtd_por_m2"]
                    if not ruas: ruas = dados_soja[idx]["ruas"]

                    total_insumo = calcular_area_soja(float(largura), float(comprimento)) * float(qtd) * int(ruas)

                    dados_soja[idx] = {
                        'area': calcular_area_soja(float(largura), float(comprimento)),
                        'largura': float(largura), 
                        'comprimento': float(comprimento),
                        'insumo': insumo,
                        'total_insumo': total_insumo,
                        'qtd_por_m2': float(qtd),
                        'ruas': int(ruas)
                    }

                    salva_csv()
                    break
                else:
                    print('Índice inválido!')
            else:
                print('Nenhum dado de soja registrado.')
                break
        elif op == 2:
            saida_dados(culturas[op-1])
            if len(dados_milho) > 0:
                idx = int(input('Índice do dado a atualizar:'))
                if idx >= 0 and idx < len(dados_milho):
                    print(f'Atualizando dados do milho: {idx} (Deixe vazio para manter valor anterior)')
                    raio = input(f'Raio anterior {dados_milho[idx]["raio"]}: Novo raio (m): ')
                    insumo = input(f'Insumo anterior {dados_milho[idx]["insumo"]}: Novo insumo: ')
                    qtd = input(f'Qtd/m² anterior {dados_milho[idx]["qtd_por_m2"]}: Nova qtd por m²: ')
                    ruas = input(f'Ruas anterior {dados_milho[idx]["ruas"]}: Nova qtd de ruas: ')

                    #se dados forem vazios mantem valor anterior
                    if not raio: raio = dados_milho[idx]["raio"]
                    if not insumo: insumo = dados_milho[idx]["insumo"]
                    if not qtd: qtd = dados_milho[idx]["qtd_por_m2"]
                    if not ruas: ruas = dados_milho[idx]["ruas"]

                    total_insumo = calcular_area_milho(float(raio)) * float(qtd) * int(ruas)

                    dados_milho[idx] = {
                        'area': calcular_area_milho(float(raio)),
                        'raio': float(raio),
                        'insumo': insumo,
                        'qtd_por_m2': float(qtd),
                        'ruas': int(ruas),
                        'total_insumo': total_insumo
                    }
                    salva_csv()
                    break
                else:
                    print('Índice inválido!')
            else:
                print('Nenhum dado de milho registrado.')
                break
        elif op == 0:
            break
        else:
            print('Opção inválida!')


#define função para deletar dados
def deletar_dados():
    while True:
        print('Escolha a cultura para deletar:')
        for i, c in enumerate(culturas):
            print(f'{i+1} - {c}')
        print('0 - Voltar ao menu')
        op = int(input('Informe a Opção: '))
        if op == 1:
            if(dados_soja):
                saida_dados()
                idx = int(input('Índice do dado a deletar: '))
                if 0 <= idx < len(dados_soja):
                    dados_soja.pop(idx)
                    print('Dado deletado!')
                    salva_csv()
                    break
                else:
                    print('Índice inválido!')
            else:
                print('Nenhum dado de soja registrado.')
                break
        elif op == 2:
            if(dados_milho):
                saida_dados()
                idx = int(input('Índice do dado a deletar: '))
                if 0 <= idx < len(dados_milho):
                    dados_milho.pop(idx)
                    print('Dado deletado!')
                    salva_csv()
                    break
                else:
                    print('Índice inválido!')
            else:
                print('Nenhum dado de milho registrado.')
                break
        elif op == 0:
            break
        else:
            print('Opção inválida!')

#define função para carregar dados do CSV ao iniciar
def carrega_csv():
    global filename
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['cultura'] == 'Soja':
                    dados_soja.append({
                        'area': float(row['area']),
                        'insumo': row['insumo'],
                        'qtd_por_m2': float(row['qtd-por-m2']),
                        'ruas': int(row['ruas']),
                        'largura': float(row['largura']),
                        'comprimento': float(row['comprimento']),
                        'total_insumo': float(row['totalinsumo']),
                    })
                elif row['cultura'] == 'Milho':
                    dados_milho.append({
                        'area': float(row['area']),
                        'insumo': row['insumo'],
                        'qtd_por_m2': float(row['qtd-por-m2']),
                        'ruas': int(row['ruas']),
                        'raio': float(row['raio']),
                        'total_insumo': float(row['totalinsumo']),
                    })

        print(f'Dados carregados de {filename}')
    except FileNotFoundError:
        print(f'Arquivo {filename} não encontrado. Iniciando com dados vazios.')
    except Exception as e:
        print(f'Erro ao carregar dados: {e}')


#define função para salvar dados em CSV
def salva_csv():
    global filename
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['cultura', 'area', 'insumo', 'qtd-por-m2', 'ruas', 'totalinsumo', 'largura', 'comprimento', 'raio'])

        for d in dados_soja:
            writer.writerow(['Soja', f'{d['area']:.2f}', d['insumo'], d['qtd_por_m2'], d['ruas'], f'{d['total_insumo']:.2f}', d['largura'], d['comprimento'], ''])

        for d in dados_milho:
            writer.writerow(['Milho', f'{d['area']:.2f}', d['insumo'], d['qtd_por_m2'], d['ruas'], f'{d['total_insumo']:.2f}', '', '', d['raio']])

    print(f'Dados salvos em {filename}')

#define função do menu
def menu():
    while True:
        print('\n--- Menu Agricultura Digital ---')
        print('1 - Entrada de dados')
        print('2 - Saída de dados')
        print('3 - Atualizar dados')
        print('4 - Deletar dados')
        print('5 - Sair')

        op = input('Escolha uma opção: ')

        match op:
            case '1':
                entrada_dados()
            case '2':
                saida_dados()
            case '3':
                atualizar_dados()
            case '4':
                deletar_dados()
            case '5':
                print('Saindo...')
                break
            case _:
                print('Opção inválida!')

#define função de inicialização
def init():
    carrega_csv()
    menu()

#inicia aplicação
init()