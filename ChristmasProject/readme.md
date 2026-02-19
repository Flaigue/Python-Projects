Árvore de Natal Dinâmica em Python

Este é um projeto desenvolvido em Python que gera uma árvore de Natal personalizada no terminal. O script vai além do visual básico, utilizando lógica de datas e cores ANSI reais (RGB) para criar uma experiência interativa.

Funcionalidades

Altura Personalizável: O utilizador define o tamanho da árvore através de um input.
Cores RGB no Terminal: Uso de dicionários e sequências de escape ANSI para renderizar cores vivas (Amarelo para a estrela, Verde para as folhas, Castanho para o tronco e Cinzento para a base).
Lógica de Calendário: O script utiliza a biblioteca `datetime` para verificar a data atual e exibir mensagens personalizadas:
    Véspera de Natal (24/12).
    Dia de Natal (25/12).
    Mês de Dezembro.
    Fora da época festiva.
Interface Limpa: Uso de `os.system("clear")` para focar a atenção apenas no desenho gerado.

Tecnologias Utilizadas

Python 3
Biblioteca `os`: Para manipulação do terminal.
Biblioteca `datetime`: Para gestão de lógica temporal.

Aprendizados Técnicos

Neste projeto, consolidei conceitos fundamentais de programação:

F-Strings: Para interpolação de variáveis e formatação de strings complexas de forma legível.
Dicionários: Organização de códigos de cores (ANSI RGB) para facilitar a manutenção e evitar repetição de código.
Matemática de Alinhamento: Lógica para calcular espaços e a quantidade de caracteres por linha, garantindo a forma triangular perfeita independente da altura.
Validação de Input: Implementação de um fecho de programa controlado pelo utilizador, evitando que o terminal feche abruptamente.

Como Executar

1. Certifica-te de que tens o Python instalado no teu sistema (testado em Linux Mint).
2. Clona este repositório: 
   ```bash
   git clone https://github.com/Flaigue/Python-Projects
3. Navega até a pasta do projeto: cd Python-Projects/ChristmasProject
4. Executa o script: python3 ChirstmasTree.py
