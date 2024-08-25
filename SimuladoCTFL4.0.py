# biblioteca utilizadas no projeto
import os
import random

# Listas de perguntas organizadas por capítulos
chapter_1_questions = [
    {
        "question": "Qual é o objetivo principal do teste de software?",
        "options": ["a) Encontrar todos os defeitos no software.",
                    "b) Substituir a revisão de código.",
                    "c) Demonstrar que o software não tem defeitos.",
                    "d) Aumentar a confiança na qualidade do software."],
        "correct_answer": "d"
    },
    {
        "question": "Qual dos seguintes NÃO é um dos sete princípios do teste?",
        "options": ["a) Testes mostram a presença de defeitos.",
                    "b) Teste exaustivo é possível.",
                    "c) Defeitos agrupados.",
                    "d) Teste depende do contexto."],
        "correct_answer": "b"
    },
    {
        "question": "O que significa 'efeito pesticida' no contexto de testes de software?",
        "options": ["a) A tendência de novos defeitos surgirem após a correção de defeitos anteriores.",
                    "b) A necessidade de alterar casos de teste para continuar encontrando defeitos.",
                    "c) A automatização de testes para aumentar a eficiência.",
                    "d) A repetição dos mesmos testes que não encontra novos defeitos."],
        "correct_answer": "b"
    },
    {
        "question": "Em que etapa do ciclo de vida do software o teste deve ser iniciado?",
        "options": ["a) Somente após a implementação estar concluída.",
                    "b) Durante a fase de manutenção.",
                    "c) Durante a fase de especificação de requisitos.",
                    "d) Somente durante a fase de aceitação."],
        "correct_answer": "c"
    },
    {
        "question": "Qual é o objetivo principal da revisão de um documento de requisitos?",
        "options": ["a) Identificar defeitos o mais cedo possível.",
                    "b) Confirmar a completude dos requisitos.",
                    "c) Estimar o esforço necessário para o teste.",
                    "d) Priorizar os casos de teste."],
        "correct_answer": "a"
    },
    {
        "question": "Qual das seguintes afirmações sobre teste de software está correta?",
        "options": ["a) Testes só são necessários em projetos críticos.",
                    "b) Testes não são necessários se o software foi bem desenvolvido.",
                    "c) Testes ajudam a aumentar a qualidade do software ao encontrar defeitos.",
                    "d) Testes de software são uma perda de tempo."],
        "correct_answer": "c"
    },
    {
        "question": "Qual é uma das razões para usar uma abordagem de teste baseada em risco?",
        "options": ["a) Reduzir o número de casos de teste.",
                    "b) Aumentar o tempo de execução dos testes.",
                    "c) Focar o esforço de teste nas áreas mais críticas do software.",
                    "d) Garantir que todos os testes sejam executados simultaneamente."],
        "correct_answer": "c"
    },
    {
        "question": "O que é verificação no contexto de teste de software?",
        "options": ["a) O processo de avaliação de um sistema ou componente para determinar se os produtos de uma fase de desenvolvimento satisfazem as condições impostas no início daquela fase.",
                    "b) O processo de avaliação de software ao final do desenvolvimento para verificar se ele atende aos requisitos do cliente.",
                    "c) A execução de testes automatizados.",
                    "d) A revisão do código fonte para encontrar defeitos."],
        "correct_answer": "a"
    },
    {
        "question": "Qual das seguintes opções descreve corretamente o princípio da ""ausência de erros""?",
        "options": ["a) Mesmo que um software esteja livre de erros, ele pode não estar de acordo com os requisitos do usuário.",
                    "b) A ausência de erros em um software significa que ele está pronto para ser entregue.",
                    "c) Um software sem defeitos sempre satisfaz as necessidades do cliente.",
                    "d) A ausência de erros é garantida pela realização de testes exaustivos."],
        "correct_answer": "a"
    },
    {
        "question": "Em qual situação é mais apropriado realizar testes exploratórios?",
        "options": ["a) Quando o tempo de teste é limitado e a documentação está incompleta.",
                    "b) Durante a fase inicial de desenvolvimento.",
                    "c) Para substituir os testes de unidade.",
                    "d) Somente durante testes de aceitação pelo usuário."],
        "correct_answer": "a"
    },
    # Adicione mais perguntas do Capítulo 1 aqui
]

chapter_2_questions = [
   {
        "question": "Qual dos seguintes é um exemplo de teste de sistema?",
        "options": ["a) Teste de unidade de uma função específica.",
                    "b) Verificação de requisitos não funcionais como desempenho.",
                    "c) Teste de integração entre dois módulos.",
                    "d) Revisão de código."],
        "correct_answer": "b"
    },
    {
        "question": "Em qual nível de teste é mais provável que se encontre problemas de integração entre módulos?",
        "options": ["a) Teste de unidade.",
                    "b) Teste de sistema.",
                    "c) Teste de integração.",
                    "d) Teste de aceitação."],
        "correct_answer": "c"
    },
    {
        "question": "Qual é a principal diferença entre teste funcional e não funcional?",
        "options": ["a) O teste funcional foca no comportamento especificado, enquanto o não funcional foca em critérios como desempenho e usabilidade.",
                    "b) O teste funcional é realizado manualmente, enquanto o não funcional é sempre automatizado.",
                    "c) O teste funcional é conduzido apenas durante a fase de aceitação.",
                    "d) O teste não funcional testa apenas interfaces de usuário."],
        "correct_answer": "a"
    },
    {
        "question": "Qual das seguintes opções melhor descreve um teste de regressão?",
        "options": ["a) Teste realizado após mudanças no código para verificar se as funcionalidades existentes ainda funcionam.",
                    "b) Teste conduzido apenas no final do ciclo de desenvolvimento.",
                    "c) Teste de aceitação conduzido pelo cliente.",
                    "d) Teste que foca apenas em novos requisitos adicionados ao software."],
        "correct_answer": "a"
    },
    {
        "question": "Quando é mais apropriado conduzir testes de aceitação?",
        "options": ["a) Antes do teste de integração.",
                    "b) Após o teste de sistema.",
                    "c) Durante o desenvolvimento inicial.",
                    "d) Após a entrega do produto ao cliente."],
        "correct_answer": "b"
    },

    {
        "question": "Qual é o objetivo principal do teste de aceitação?",
        "options": ["a) Verificar a integridade dos componentes individuais do software.",
                    "b) Avaliar se o sistema está pronto para ser liberado para produção.",
                    "c) Identificar defeitos no código fonte.",
                    "d) Validar a integração entre módulos de software."],
        "correct_answer": "b"
    },
    {
        "question": "Qual dos seguintes tipos de teste NÃO é geralmente realizado em um nível de teste específico?",
        "options": ["a) Teste de regressão.",
                    "b) Teste de unidade.",
                    "c) Teste de sistema.",
                    "d) Teste de integração."],
        "correct_answer": "a"
    },
    {
        "question": "Em um ciclo de vida de desenvolvimento ágil, qual é a abordagem recomendada para testes?",
        "options": ["a) Testar apenas no final do ciclo de desenvolvimento.",
                    "b) Testes devem ser realizados de forma contínua e integrada ao desenvolvimento.",
                    "c) Testes devem ser minimizados para acelerar as entregas.",
                    "d) Testes devem ser realizados apenas pelos desenvolvedores."],
        "correct_answer": "b"
    },
    {
        "question": "O teste de integração é melhor realizado:",
        "options": ["a) Após o teste de aceitação.",
                    "b) Quando todos os módulos estão prontos.",
                    "c) De forma incremental, à medida que os módulos são desenvolvidos.",
                    "d) Após o software ser colocado em produção."],
        "correct_answer": "c"
    },
    {
        "question": "O que é um teste de regressão?",
        "options": ["a) Um teste realizado para verificar se o sistema atende aos requisitos do usuário.",
                    "b) Um teste realizado para garantir que novas alterações não introduzam novos defeitos em funcionalidades existentes.",
                    "c) Um teste realizado para medir o desempenho do sistema.",
                    "d) Um teste realizado apenas em casos de uso críticos."],
        "correct_answer": "b"
    },
    # Adicione mais perguntas do Capítulo 2 aqui
]

chapter_3_questions = [
      {
        "question": "Qual das seguintes é uma técnica de teste estático?",
        "options": ["a) Teste de integração.",
                    "b) Análise de valor limite.",
                    "c) Revisão de código.",
                    "d) Teste de desempenho."],
        "correct_answer": "c"
    },
    {
        "question": "Qual é o objetivo principal das revisões em teste estático?",
        "options": ["a) Executar o software para encontrar defeitos.",
                    "b) Avaliar a qualidade de artefatos de software como documentos de requisitos e código.",
                    "c) Medir o tempo de execução do software.",
                    "d) Simular a execução do código."],
        "correct_answer": "b"
    },
    {
        "question": "Qual das seguintes NÃO é uma atividade realizada durante uma revisão formal?",
        "options": ["a) Preparação.",
                    "b) Reunião de revisão.",
                    "c) Execução de casos de teste.",
                    "d) Coleta de métricas."],
        "correct_answer": "c"
    },
    {
        "question": "Em que momento a análise estática é mais eficaz?",
        "options": ["a) Durante a codificação, antes da fase de teste de unidade.",
                    "b) Após a implementação, antes do teste de sistema.",
                    "c) Durante a fase de manutenção do software.",
                    "d) Após a entrega do software ao cliente."],
        "correct_answer": "a"
    },
    {
        "question": "Qual é a principal diferença entre uma revisão informal e uma formal?",
        "options": ["a) Revisões informais são sempre realizadas sem documentação.",
                    "b) Revisões formais seguem um processo estruturado com etapas definidas e métricas coletadas.",
                    "c) Revisões informais são conduzidas por ferramentas automáticas.",
                    "d) Revisões formais são realizadas apenas pelo gerente de projeto."],
        "correct_answer": "b"
    },


    {
        "question": "Qual dos seguintes NÃO é um benefício de testes estáticos?",
        "options": ["a) Identificação precoce de defeitos.",
                    "b) Redução de custos de correção de defeitos.",
                    "c) Eliminação da necessidade de testes dinâmicos.",
                    "d) Aumento da qualidade dos documentos de requisitos."],
        "correct_answer": "c"
    },
    {
        "question": "Em uma revisão formal, qual das seguintes funções é responsável por moderar a reunião?",
        "options": ["a) O autor do documento revisado.",
                    "b) O gerente de projeto.",
                    "c) O moderador.",
                    "d) O responsável pelo teste."],
        "correct_answer": "c"
    },
    {
        "question": "Qual é uma técnica de teste estático que envolve a análise detalhada do código sem execução?",
        "options": ["a) Teste de caixa-branca.",
                    "b) Revisão por pares.",
                    "c) Cobertura de caminho.",
                    "d) Simulação de fluxo de dados."],
        "correct_answer": "b"
    },
    {
        "question": "O que diferencia uma revisão formal de uma informal?",
        "options": ["a) As revisões formais seguem um processo definido, com papéis e resultados documentados.",
                    "b) As revisões informais sempre são realizadas em sessões individuais.",
                    "c) As revisões informais são obrigatórias, enquanto as formais são opcionais.",
                    "d) As revisões formais não envolvem reuniões presenciais."],
        "correct_answer": "a"
    },
    {
        "question": "Qual é o principal objetivo das técnicas de inspeção no contexto de testes estáticos?",
        "options": ["a) Identificar e corrigir defeitos no código e na documentação antes que eles causem falhas.",
                    "b) Executar o código em busca de defeitos.",
                    "c) Validar as especificações de requisitos.",
                    "d) Garantir que todos os casos de teste foram escritos corretamente."],
        "correct_answer": "a"
    },
    # Adicione mais perguntas do Capítulo 3 aqui
]

chapter_4_questions = [
    {
        "question": "Qual das seguintes técnicas de modelagem de teste é uma técnica de caixa-preta?",
        "options": ["a) Cobertura de caminho.",
                    "b) Teste de transição de estados.",
                    "c) Cobertura de instrução.",
                    "d) Análise de fluxo de dados."],
        "correct_answer": "b"
    },
    {
        "question": "O que é Particionamento de Equivalência?",
        "options": ["a) Uma técnica que garante a cobertura completa do código.",
                    "b) Uma técnica para dividir dados de entrada em classes de equivalência que são tratadas da mesma forma pelo sistema.",
                    "c) Uma técnica de análise de código estático.",
                    "d) Um método para gerar casos de teste baseados na estrutura interna do software."],
        "correct_answer": "b"
    },
    {
        "question": "Qual das seguintes técnicas é mais adequada para testar casos de uso específicos de um sistema?",
        "options": ["a) Análise de valor limite.",
                    "b) Teste de transição de estados.",
                    "c) Teste de caixa-branca.",
                    "d) Teste baseado em tabela de decisão."],
        "correct_answer": "d"
    },
    {
        "question": "Quando a técnica de Análise de Valor Limite é mais eficaz?",
        "options": ["a) Quando há um grande número de combinações possíveis de entrada.",
                    "b) Quando os requisitos são ambíguos.",
                    "c) Quando os valores de entrada têm limites superior e inferior.",
                    "d) Quando se está testando a usabilidade do sistema."],
        "correct_answer": "c"
    },
    {
        "question": "Qual é a diferença entre Particionamento de Equivalência e Análise de Valor Limite?",
        "options": ["a) Análise de Valor Limite foca em entradas no limite de uma classe de equivalência.",
                    "b) Particionamento de Equivalência é uma técnica de caixa-branca, enquanto Análise de Valor Limite é de caixa-preta.",
                    "c) Particionamento de Equivalência testa limites extremos, enquanto Análise de Valor Limite testa entradas representativas dentro de um intervalo.",
                    "d) Não há diferença; ambos são a mesma técnica."],
        "correct_answer": "a"
    },


    {
        "question": "A técnica de tabela de decisão é mais útil para:",
        "options": ["a) Testar interações complexas com múltiplas combinações de entradas.",
                    "b) Verificar a aparência de uma interface de usuário.",
                    "c) Testar o desempenho do sistema.",
                    "d) Testar o comportamento de um módulo isolado."],
        "correct_answer": "a"
    },
    {
        "question": "Qual das seguintes técnicas de modelagem de teste utiliza grafos de causa e efeito?",
        "options": ["a) Particionamento de equivalência.",
                    "b) Teste de transição de estados.",
                    "c) Análise de valor limite.",
                    "d) Tabela de decisão."],
        "correct_answer": "d"
    },
    {
        "question": "Quando uma técnica de Análise de Valor Limite é mais útil?",
        "options": ["a) Quando se lida com grandes volumes de dados de entrada.",
                    "b) Quando há restrições específicas de valores em intervalos numéricos.",
                    "c) Quando o sistema não tem validações específicas.",
                    "d) Para testar fluxos de trabalho alternativos."],
        "correct_answer": "b"
    },
    {
        "question": "Qual das seguintes técnicas se baseia em explorar as diferentes condições lógicas em um sistema?",
        "options": ["a) Particionamento de equivalência.",
                    "b) Tabela de decisão.",
                    "c) Teste de transição de estados.",
                    "d) Análise de fluxo de dados."],
        "correct_answer": "b"
    },
    {
        "question": "Qual é o principal objetivo da técnica de Particionamento de Equivalência?",
        "options": ["a) Reduzir o número de casos de teste necessários ao identificar classes de entrada que são tratadas de forma semelhante.",
                    "b) Garantir que todos os caminhos possíveis no código sejam testados.",
                    "c) Avaliar a segurança do sistema.",
                    "d) Medir o desempenho do sistema em diferentes condições."],
        "correct_answer": "a"
    },
    # Adicione mais perguntas do Capítulo 4 aqui
]

chapter_5_questions = [
{
        "question": "Qual é a principal responsabilidade do gerente de teste?",
        "options": ["a) Executar testes unitários.",
                    "b) Revisar o código fonte.",
                    "c) Escrever casos de teste.",
                    "d) Planejar e controlar as atividades de teste."],
        "correct_answer": "d"
    },
    {
        "question": "O que é uma estratégia de teste?",
        "options": ["a) Um plano de alto nível que define a abordagem de teste para o projeto.",
                    "b) Uma descrição detalhada de como os casos de teste serão executados.",
                    "c) Um relatório que documenta os defeitos encontrados durante os testes.",
                    "d) Um conjunto de scripts de teste automatizados."],
        "correct_answer": "a"
    },
    {
        "question": "Qual é o objetivo da priorização dos casos de teste?",
        "options": ["a) Garantir que todos os casos de teste sejam executados no mesmo dia.",
                    "b) Maximizar a cobertura de teste nas áreas mais críticas do sistema.",
                    "c) Reduzir o número de testes necessários.",
                    "d) Evitar a execução de testes repetidos."],
        "correct_answer": "b"
    },
    {
        "question": "O que é um risco de teste?",
        "options": ["a) Um teste que falha.",
                    "b) Um defeito encontrado no software.",
                    "c) Um evento incerto que pode impactar o sucesso do projeto de teste.",
                    "d) Uma técnica para priorizar testes."],
        "correct_answer": "c"
    },
    {
        "question": "O que é um critério de saída em um plano de teste?",
        "options": ["a) As condições que devem ser atendidas para considerar que o teste foi completado.",
                    "b) O número mínimo de defeitos que devem ser encontrados.",
                    "c) A quantidade de tempo permitida para executar os testes.",
                    "d) A porcentagem de casos de teste que devem passar."],
        "correct_answer": "a"
    },


    {
        "question": "Qual é o principal motivo para definir critérios de entrada para as atividades de teste?",
        "options": ["a) Garantir que os testes sejam concluídos antes do prazo.",
                    "b) Definir quando uma atividade de teste deve começar, assegurando que todos os pré-requisitos estejam cumpridos.",
                    "c) Verificar se todos os defeitos foram corrigidos.",
                    "d) Avaliar a qualidade dos testes realizados."],
        "correct_answer": "b"
    },
    {
        "question": "Em um plano de testes, qual dos seguintes itens geralmente NÃO é incluído?",
        "options": ["a) Critérios de aceitação.",
                    "b) Objetivos de teste.",
                    "c) Custo estimado dos testes.",
                    "d) Resultados dos testes executados."],
        "correct_answer": "d"
    },
    {
        "question": "O que significa 'cobertura de teste' no contexto de gerenciamento de teste?",
        "options": ["a) A quantidade de código revisado manualmente.",
                    "b) A proporção de requisitos ou funcionalidades que foram validados por meio de testes.",
                    "c) O número de defeitos encontrados.",
                    "d) A quantidade de documentação produzida durante o teste."],
        "correct_answer": "b"
    },
    {
        "question": "Em qual fase do gerenciamento de teste é realizado o monitoramento e controle?",
        "options": ["a) Planejamento.",
                    "b) Execução.",
                    "c) Relato.",
                    "d) Monitoramento é uma atividade contínua durante todo o ciclo de vida do teste."],
        "correct_answer": "d"
    },
    {
        "question": "O que é um risco residual?",
        "options": ["a) Um defeito que ainda está presente após a correção.",
                    "b) Um risco que permanece após a aplicação de medidas de mitigação.",
                    "c) Um risco identificado antes da execução do teste.",
                    "d) Um risco que foi completamente eliminado."],
        "correct_answer": "b"
    },
    # Adicione mais perguntas do Capítulo 5 aqui
]

chapter_6_questions = [
    {
        "question": "Qual das seguintes é uma vantagem do uso de ferramentas de automação de teste?",
        "options": ["a) Garantir que todos os defeitos serão encontrados.",
                    "b) Reduzir o tempo de execução dos testes repetitivos.",
                    "c) Substituir completamente o teste manual.",
                    "d) Eliminar a necessidade de casos de teste."],
        "correct_answer": "b"
    },
    {
        "question": "Qual é o principal objetivo de uma ferramenta de gerenciamento de testes?",
        "options": ["a) Automatizar a execução de testes.",
                    "b) Monitorar o desempenho do software.",
                    "c) Controlar e documentar as atividades de teste, incluindo planejamento e rastreamento de defeitos.",
                    "d) Gerar relatórios de desempenho."],
        "correct_answer": "c"
    },
    {
        "question": "Quando é mais apropriado usar uma ferramenta de captura e reprodução?",
        "options": ["a) Quando se precisa de scripts de teste altamente personalizados.",
                    "b) Em testes de desempenho.",
                    "c) Para revisar o código fonte.",
                    "d) Para automatizar testes de interface do usuário que são repetitivos."],
        "correct_answer": "d"
    },
    {
        "question": "Qual é um dos principais desafios ao implementar ferramentas de automação de teste?",
        "options": ["a) A dificuldade em criar casos de teste.",
                    "b) O alto custo de aquisição.",
                    "c) A necessidade de manutenção contínua dos scripts de teste.",
                    "d) A impossibilidade de integrar a ferramenta com outros sistemas."],
        "correct_answer": "c"
    },
    {
        "question": "Qual dos seguintes NÃO é um benefício das ferramentas de teste?",
        "options": ["a) Redução do tempo necessário para executar testes repetitivos.",
                    "b) A eliminação da necessidade de planejamento de testes.",
                    "c) Aumento na cobertura de teste.",
                    "d) Melhoria na consistência dos testes executados."],
        "correct_answer": "b"
    },


    {
        "question": "Qual é o principal objetivo de uma ferramenta de rastreamento de defeitos?",
        "options": ["a) Automatizar a execução de testes.",
                    "b) Identificar quais testes precisam ser executados.",
                    "c) Registrar e acompanhar os defeitos encontrados durante o teste.",
                    "d) Melhorar o desempenho do software."],
        "correct_answer": "c"
    },
    {
        "question": "Qual das seguintes NÃO é uma funcionalidade comum em ferramentas de gerenciamento de testes?",
        "options": ["a) Controle de versões de código-fonte.",
                    "b) Planejamento de testes.",
                    "c) Relatórios de execução de testes.",
                    "d) Rastreamento de defeitos."],
        "correct_answer": "a"
    },
    {
        "question": "Em qual situação o uso de uma ferramenta de automação de testes pode não ser vantajoso?",
        "options": ["a) Quando os testes precisam ser repetidos frequentemente.",
                    "b) Quando o custo de manutenção da automação supera os benefícios.",
                    "c) Quando os casos de teste são muito simples.",
                    "d) Quando se precisa de alta precisão nos resultados."],
        "correct_answer": "b"
    },
    {
        "question": "Qual das seguintes ferramentas é mais adequada para medir o desempenho do software?",
        "options": ["a) Ferramenta de captura e reprodução.",
                    "b) Ferramenta de rastreamento de defeitos.",
                    "c) Ferramenta de gerenciamento de configuração.",
                    "d) Ferramenta de teste de carga e desempenho."],
        "correct_answer": "d"
    },
    {
        "question": "Qual é um dos principais desafios na implementação de uma nova ferramenta de teste em uma organização?",
        "options": ["a) Facilidade de uso da ferramenta.",
                    "b) Integração com as ferramentas e processos já existentes.",
                    "c) Seleção dos casos de teste a serem automatizados.",
                    "d) Documentação das funcionalidades da ferramenta."],
        "correct_answer": "b"
    },
    # Adicione mais perguntas do Capítulo 6 aqui
]

# Função para limpar a tela
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para rodar o quiz
def run_quiz(questions):
    clear_screen()  # Limpa a tela antes de iniciar o quiz
    random.shuffle(questions)  # Embaralha as perguntas antes de iniciar o quiz
    user_answers = []

    # Loop para percorrer todas as perguntas
    for i, q in enumerate(questions):
        print(f"Pergunta {i+1}: {q['question']}")
        for option in q["options"]:
            print(option)
        answer = input("Sua resposta (a, b, c, d): ").lower()
        user_answers.append(answer)
        print("\n")

    # Após todas as perguntas, exibe as respostas corretas
    print("Resultado do Simulado:\n")
    correct_count = 0

    for i, q in enumerate(questions):
        print(f"Pergunta {i+1}: {q['question']}")
        print(f"Sua resposta: {user_answers[i]}")
        print(f"Resposta correta: {q['correct_answer']}\n")
        
        if user_answers[i] == q['correct_answer']:
            correct_count += 1

    print(f"Você acertou {correct_count} de {len(questions)} perguntas.")

# Função para o menu final
def end_menu():
    while True:
        print("Menu:")
        print("1. Refazer o simulado")
        print("2. Menu principal")
        print("3. Fechar programa")
        
        choice = input("Escolha uma opção (1-3): ")

        if choice == '1':
            clear_screen()  # Limpa a tela antes de refazer o simulado
            run_quiz(current_questions)
        elif choice == '2':
            clear_screen()  # Limpa a tela antes de ir ao menu principal
            main_menu()
        elif choice == '3':
            print("Saindo do programa...")
            exit()
        else:
            print("Opção inválida! Por favor, escolha um número entre 1 e 3.\n")

# Variável global para armazenar as questões atuais
current_questions = []

# Menu interativo principal
def main_menu():
    global current_questions
    
    while True:
        clear_screen()  # Limpa a tela sempre que o menu principal for exibido
        print("SIMULADO CTFL 4.0\n")
        print("Criado por Antonio Dionisio\n")
        print("Objetivo de estudos focado na CTFl 4.0\n")
        print("Lista de simulados:")
        print("1. Capítulo 1: Fundamentos de Teste")
        print("2. Capítulo 2: Testes ao Longo do Ciclo de Vida de Desenvolvimento de Software")
        print("3. Capítulo 3: Teste Estático")
        print("4. Capítulo 4: Análise e Modelagem de Teste")
        print("5. Capítulo 5: Gerenciamento das Atividades de Teste")
        print("6. Capítulo 6: Ferramentas de Teste")
        print("7. Sair")

        choice = input("Escolha um capítulo para iniciar o simulado (1-7): ")

        if choice == '1':
            print("\n--- Capítulo 1: Fundamentos de Teste ---\n")
            current_questions = chapter_1_questions
            run_quiz(current_questions)
            end_menu()  # Chamar o menu de opções ao final do quiz
        elif choice == '2':
            print("\n--- Capítulo 2: Testes ao Longo do Ciclo de Vida de Desenvolvimento de Software ---\n")
            current_questions = chapter_2_questions
            run_quiz(current_questions)
            end_menu()
        elif choice == '3':
            print("\n--- Capítulo 3: Teste Estático ---\n")
            current_questions = chapter_3_questions
            run_quiz(current_questions)
            end_menu()
        elif choice == '4':
            print("\n--- Capítulo 4: Análise e Modelagem de Teste ---\n")
            current_questions = chapter_4_questions
            run_quiz(current_questions)
            end_menu()
        elif choice == '5':
            print("\n--- Capítulo 5: Gerenciamento das Atividades de Teste ---\n")
            current_questions = chapter_5_questions
            run_quiz(current_questions)
            end_menu()
        elif choice == '6':
            print("\n--- Capítulo 6: Ferramentas de Teste ---\n")
            current_questions = chapter_6_questions
            run_quiz(current_questions)
            end_menu()
        elif choice == '7':
            print("Saindo do programa...")
            exit()
        else:
            print("Opção inválida! Por favor, escolha um número entre 1 e 7.\n")

if __name__ == "__main__":
    main_menu()