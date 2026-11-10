
# 📘 Assignment: Games in Python

## 🎯 Objective

Implemente um jogo da forca em Python para praticar strings, listas, condicionais, loops e entrada de dados. O jogador deve descobrir uma palavra aleatória antes de esgotar as tentativas.

## 📝 Tasks

### 🛠️ Implementar o ciclo principal do jogo

#### Descrição
Complete o código inicial para selecionar uma palavra secreta e permitir que o jogador tente adivinhá-la, uma letra por vez.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra da lista fornecida.
- Mostrar as letras descobertas e ocultar as demais, por exemplo, `_ _ _ _`.
- Registrar os palpites incorretos e limitar o número de tentativas.
- Encerrar a partida quando a palavra for descoberta ou as tentativas acabarem.
- Exibir uma mensagem de vitória ou derrota e revelar a palavra secreta ao final.

### 🛠️ Validar e acompanhar os palpites

#### Descrição
Melhore a interação do jogo para lidar com entradas inválidas e letras que já foram informadas.

#### Requisitos
O programa concluído deve:

- Aceitar somente um caractere alfabético por palpite.
- Informar quando o jogador inserir uma entrada inválida ou repetir uma letra.
- Não descontar tentativas por entradas inválidas ou letras repetidas.
- Exibir as letras já tentadas durante a partida.