# Sistema-Bancario-com-Python

**Objetivo:** Criar um sistema bancário com as operações: `sacar, depositar e visualizar extrato.`

# Situação 

Fomos contratados para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: `depósito, saque e extrato.`

### Operação de depósito

- Deve ser possível valores positivos para a minha conta bancária.
- A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária.
- Todos os depósitos devem ser armazenados em uma variável e exibidos na [operação de extrato](#operação-de-extrato).

### Operação de saque

- O sistema deve permitir realizar 3 saques diários com limite máximo de R$500,00 por saque.
- Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que `não será possível sacar o dinheiro por falta de saldo`.
- Todos os saques devem ser armazenados em uma variável e exibidos na [operação de extrato](#operação-de-extrato).

### Operação de extrato

- Essa operaão deve listar os depósitos e saques realizados na conta.
- No fim da listagem deve ser exibido o saldo atual da conta.
- Se o extrato estiver em branco, exibir a mensagem: `Não foi realizada movimentações.`
- Os valores devem ser exibidos utilizando o formato R$ xxx,xX  `Exemplo: 1500.45 = R$1500.45`

# Informações

- Acabei adicionando a opção de saldo, para o usuário consultar seu saldo caso haja dúvodas de quanto dinheiro ele tem na conta.
- Esse desafio eu fui pela minha lógica, com auxilio também a atividade do instrutor [Referência do instrutor](https://github.com/digitalinnovationone/trilha-python-dio/blob/main/00%20-%20Fundamentos/desafio.py)
- Desafio de projeto proposto pela DIO ❤️.



