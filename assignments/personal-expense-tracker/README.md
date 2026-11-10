# 📘 Assignment: Controle de Gastos Pessoais

## 🎯 Objetivo

Use funções, listas e dicionários para registrar, organizar e analisar gastos do dia a dia.

## 📝 Tarefas

### 🛠️ Registrar gastos

#### Descrição
Implemente a função `registrar_gasto` para adicionar um gasto à lista de gastos.

#### Requisitos
O programa concluído deve:

- Receber a lista `gastos`, a `descricao`, a `categoria` e o `valor`
- Adicionar à lista um dicionário com as chaves `descricao`, `categoria` e `valor`
- Ignorar (não registrar) valores menores ou iguais a zero
- Retornar a lista atualizada

Exemplo:

```python
gastos = []
registrar_gasto(gastos, "Almoço", "alimentação", 25.5)
print(gastos)
# [{'descricao': 'Almoço', 'categoria': 'alimentação', 'valor': 25.5}]
```

### 🛠️ Total por categoria

#### Descrição
Implemente a função `total_por_categoria` para somar os gastos de cada categoria.

#### Requisitos
O programa concluído deve:

- Receber a lista de gastos e retornar um dicionário `{categoria: total}`
- Arredondar os totais para duas casas decimais
- Não incluir categorias que não possuem gastos

Exemplo:

```python
gastos = [
    {'descricao': 'Almoço', 'categoria': 'alimentação', 'valor': 25.5},
    {'descricao': 'Ônibus', 'categoria': 'transporte', 'valor': 4.4},
    {'descricao': 'Jantar', 'categoria': 'alimentação', 'valor': 30.0},
]
print(total_por_categoria(gastos))
# {'alimentação': 55.5, 'transporte': 4.4}
```

### 🛠️ Controle de orçamento e programa final

#### Descrição
Implemente a função `categorias_acima_do_limite` e um programa principal que conversa com o usuário.

#### Requisitos
O programa concluído deve:

- Implementar `categorias_acima_do_limite(totais, limites)`, que retorna a lista de categorias cujo total ultrapassa o limite definido
- Ignorar categorias que não possuem limite definido
- No programa principal, pedir ao usuário a descrição, a categoria e o valor de cada gasto, repetindo até ele digitar `fim`
- Exibir os totais por categoria e um alerta para cada categoria acima do limite

Exemplo de alerta:

```
⚠️ Atenção: alimentação ultrapassou o limite de R$ 50.00
```
