**Calculadora de Média Ponderada Acadêmica**

Este é um script em Python desenvolvido para facilitar o cálculo da média final de alunos, permitindo a entrada de múltiplas disciplinas e o uso de pesos diferenciados para cada uma. É uma ferramenta útil para estudantes que desejam prever seu desempenho acadêmico com base na importância (peso) de cada matéria.

🚀 Funcionalidades
Entrada Dinâmica: O usuário define a quantidade de disciplinas que deseja calcular.
Média Ponderada: Suporte para pesos customizados por matéria.
Tratamento de Peso Padrão: Caso o peso não seja informado, o sistema assume automaticamente o valor 1.0.
Feedback de Status: Exibe se o aluno foi APROVADO ou REPROVADO com base na média 5.0.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.x

Paradigma: Programação Estruturada

📋 Lógica do Cálculo
O cálculo da média ponderada é realizado seguindo a fórmula matemática:

Media Final=  ∑(Nota i * Peso i) / ∑Peso i
 
🔧 Como Executar

Certifique-se de ter o Python instalado em sua máquina.
Clone o repositório ou baixe o arquivo .py.
Abra o terminal ou prompt de comando na pasta do arquivo.

Execute o comando:

💻 Exemplo de Uso
Plaintext
---------------------------------------------
SEJA BEM-VINDO AO CALCULO DA MÉDIA DA SUA SALA
---------------------------------------------
Digite o nome do aluno: Nicolly
Digite a quantidade de disciplinas: 2

Disciplina 1:
Nome da disciplina: Programação C
Nota do aluno em Programação C: 8.5
Peso para Programação C (Pressione Enter para peso 1): 2

Disciplina 2:
Nome da disciplina: Cálculo I
Nota do aluno em Cálculo I: 6.0
Peso para Cálculo I (Pressione Enter para peso 1): 1

==============================
       RESULTADO FINAL
==============================
Nome do aluno: Nicolly
Média do aluno: 7.7
Resultado: APROVADO
==============================
