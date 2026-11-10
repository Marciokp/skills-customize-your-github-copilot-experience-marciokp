# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST introdutória com FastAPI, praticando rotas HTTP, respostas JSON e validação de dados. Ao final, a API permitirá listar, consultar e cadastrar tarefas em memória.

## 📝 Tarefas

### 🛠️ Criar uma rota de status

#### Descrição
Complete a rota raiz no código inicial para confirmar que a API está ativa e execute o servidor localmente.

#### Requisitos
O programa concluído deve:

- Responder a uma requisição `GET /` com um objeto JSON contendo uma mensagem de status.
- Iniciar com `uvicorn starter-code:app --reload`.
- Exibir a documentação interativa disponível em `/docs`.

### 🛠️ Consultar tarefas

#### Descrição
Implemente rotas para listar as tarefas disponíveis e consultar uma tarefa pelo identificador. Os dados devem permanecer na lista em memória fornecida no código inicial.

#### Requisitos
O programa concluído deve:

- Responder a `GET /tasks` com a lista de tarefas em formato JSON.
- Responder a `GET /tasks/{task_id}` com a tarefa que corresponde ao identificador informado.
- Retornar o status HTTP `404` quando o identificador não existir.

### 🛠️ Cadastrar tarefas com validação

#### Descrição
Use o modelo Pydantic fornecido para receber os dados de uma nova tarefa e implemente a rota de cadastro.

#### Requisitos
O programa concluído deve:

- Aceitar requisições `POST /tasks` com um título e um estado de conclusão opcional.
- Recusar títulos vazios por meio da validação do modelo.
- Atribuir um identificador único à nova tarefa e adicioná-la à lista em memória.
- Retornar a tarefa criada com o status HTTP `201`.