# Citizen Assist AI

> **Disciplina:** Data Structures and Algorithms (DSA)
> **Linguagem:** Python
> **Tema:** Serviços públicos de documentação
> **Turma:** 1CCPG

---

## Equipe

| Nome | RM |
|:-----|:---|
| Caio Henrique Ferraz da Silva | RM568992 |
| Enzo Caruso Peter | RM570908 |

---

## 1.Objetivo e contexto
O Citizen Assist AI — Documentação é um protótipo funcional em terminal para organizar informações úteis sobre serviços de documentação. Permite cadastrar, consultar, pesquisar, atualizar, excluir, ordenar e analisar registros de serviços. O objetivo acadêmico é aplicar uma lista simplesmente encadeada própria e algoritmos implementados manualmente.

O sistema não realiza emissão de documentos, não consulta sistemas governamentais nem armazena números de CPF/RG de cidadãos. As descrições e os locais dos serviços iniciais são exemplos didáticos e não substituem orientações oficiais.

---

### 2.Modelo dos registros

| Campo | Tipo | Finalidade |
|:------|:----------|:------:|
| **ID** | Inteiro | Identificador único do serviço |
| **Titulo** | Texto | Nome do serviço |
| **categoria** | texto | Grupo do serviço |
| **descricao** | texto | Finalidade ou informação básica |
| **requisitos** | texto | Requisitos cadastrados |
| **local** | texto | Local/canal de atendimento cadastrado |
| **proximo** | referência a outro nó ou None | Ligação com o próximo nó da estrutura |

Três serviços são carregados ao iniciar a execução: Emissão da CIN (ID 1), Regularização do CPF (ID 2) e Título de Eleitor (ID 3).

---

## 3.Estrutura e Arquivos

```
CitizenAssistAI/
├── Main.py
├── lista_encadeada.py
├── README.md
└── TESTES.md
```

Main.py: inicia os registros e apresenta o menu de opções ao usuário.
lista_encadeada.py: contém as classes No e ListaEncadeada e os métodos de manipulação.
README.md: documentação do projeto, arquitetura e Big-O.
TESTES.md: casos de teste, resultados relatados e roteiro de evidências.

inicio → [CIN | próximo] → [CPF | próximo] → [Título | None]

---

## 4.Funcionalidades

| Opção | Ação |
| --- | --- |
| `1` | Cadastrar serviço |
| `2` | Listar serviços |
| `3` | Buscar por ID |
| `4` | Pesquisar por categoria |
| `5` | Atualizar serviço |
| `6` | Excluir serviço |
| `7` | Ordenar alfabeticamente por título |
| `8` | Exibir estatísticas (total e quantidade por categoria) |
| `0` | Encerrar |

Validações confirmadas nos testes: ID repetido; título repetido no cadastro e atualização; ID não numérico; campos vazios; registros inexistentes; opções inválidas; operações com lista vazia. Os títulos são comparados sem diferenciar maiúsculas e minúsculas, conforme a versão ajustada e testada.

---

## 5.Algoritmos utilizados

#Busca sequencial
A partir de inicio, o sistema percorre os nós e compara o ID ou a categoria buscada. A busca por ID termina ao encontrar o primeiro correspondente; a pesquisa por categoria percorre a lista inteira para mostrar todas as correspondências.

#Selection Sort
O algoritmo percorre a lista, identifica o menor título na parte ainda não ordenada e troca todos os campos de dados dos nós envolvidos. As referências proximo permanecem conectadas nas mesmas posições; os dados dos serviços são trocados em conjunto para manter a correspondência entre ID, título e demais atributos. O algoritmo é implementado manualmente, sem usar sort()/`sorted()` como substituto.

#Indicadores
Um percurso da lista contabiliza o total de serviços e utiliza um dicionário para agregar as quantidades por categoria.
