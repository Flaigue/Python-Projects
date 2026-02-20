
Aim Flow - Precision Training Tool

Aim Flow é um mini-game de treinamento de precisão (aim training) desenvolvido em Python3. O projeto foca na manipulação de interfaces gráficas (GUI) e no gerenciamento de estados de jogo em tempo real, desafiando o usuário a clicar em alvos gerados dinamicamente sob pressão de tempo.


Arquitetura e Lógica de Desenvolvimento

O projeto foi construído utilizando uma abordagem funcional com foco em Event-Driven Programming (Programação Orientada a Eventos). Abaixo, os principais pilares técnicos:

1. Gerenciamento de Estados (State Management)

O software alterna entre três estados principais:

  Idle (Aguardando): O sistema permanece em espera até o primeiro clique, evitando o desperdício de recursos e tempo do usuário.
  Active (Ativo): O loop de jogo é iniciado, disparando o cronômetro e a lógica de pontuação.
  GameOver (Finalizado): Ocorre a desativação de inputs (`state="disabled"`) e a limpeza da interface para exibição de resultados e opções de reset ou sair.

2. Cronometragem Assíncrona

Diferente de abordagens básicas que utilizam `time.sleep()` (o que causaria o congelamento da interface), este projeto utiliza o método `.after()` do Tkinter. Isso permite que o cronômetro rode de forma não-bloqueante, mantendo a interface fluida e responsiva.

3. Geometria Dinâmica e Responsividade

A lógica de posicionamento do alvo calcula em tempo real as dimensões da janela (`winfo_width` / `winfo_height`). Isso garante que o botão nunca seja gerado fora da área visível, independentemente de o usuário estar com a janela maximizada ou redimensionada.

---

Funcionalidades Principais

  Start On Click: O cronômetro e score só inicia após a primeira interação do usuário.
  Score System: Contador de precisão em tempo real.
  Boundary Detection: Algoritmo simples de detecção de bordas para evitar clipping de UI.
  Game Reset: Função dedicada para reverter todas as variáveis globais e estados da interface ao padrão original, sem necessidade de reinicializar o processo.

---

Como Executar o Projeto

1. Verifique as dependências:
O projeto utiliza apenas bibliotecas nativas do Python (Tkinter, Random, OS).

2. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/flow-aim.git
```

3. Entrar na pasta AimTraining:
```bash
cd AimTraining
```
4. Executar:
```bash
python AimFlow.py
```
---

Nota: Certifique-se de ter o arquivo `Python.png` no diretório configurado para que o ícone da aplicação seja carregado corretamente.

---

Próximos Passos (Roadmap)

Para futuras iterações, pretendo implementar:

[ ] Persistência de Dados: Salvar High Scores em arquivos JSON ou SQLite.
[ ] Níveis de Dificuldade: Redução progressiva do tamanho do botão conforme o score aumenta.
[ ] Refatoração para POO: Migrar a lógica para classes (Programação Orientada a Objetos) para maior escalabilidade.

---

Autor
Leandro Reis - Linkedin - https://www.linkedin.com/in/leandro/alves/nunes

