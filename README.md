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
GS_Erick/
├── Main.py
├── lista_encadeada.py
├── README.md
├── TESTES.md
└── evidencias/
    ├── 01_cadastro.jpeg
    ├── 02_busca_id.jpeg
    ├── 03_exclusao.jpeg
    ├── 04_ordenacao.jpeg
    └── 05_estatisticas.jpeg
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

**Busca sequencial**
A partir de inicio, o sistema percorre os nós e compara o ID ou a categoria buscada. A busca por ID termina ao encontrar o primeiro correspondente; a pesquisa por categoria percorre a lista inteira para mostrar todas as correspondências.

**Selection Sort**
O algoritmo percorre a lista, identifica o menor título na parte ainda não ordenada e troca todos os campos de dados dos nós envolvidos. As referências proximo permanecem conectadas nas mesmas posições; os dados dos serviços são trocados em conjunto para manter a correspondência entre ID, título e demais atributos. O algoritmo é implementado manualmente, sem usar sort()/`sorted()` como substituto.

**Indicadores**
Um percurso da lista contabiliza o total de serviços e utiliza um dicionário para agregar as quantidades por categoria.

---

## 6.Análise de complexidade (Big-O)

| Operação | Pior caso | Justificativa |
| --- | --- | --- |
| Inserção no final | **O(n)** | Busca ID repetido e percorre a lista para chegar ao último nó |
| Listagem | **O(n)** | Visita todos os nós |
| Busca por ID | **O(n)** | Pode examinar todos os registros |
| Pesquisa por categoria | **O(n)** | Examina todos os nós para mostrar todas as correspondências |
| Busca por título | **O(n)** | Procura título duplicado por percurso sequencial |
| Atualização de um registro | **O(n)** | Localiza o nó por ID; validação de título no menu também é linear |
| Exclusão por ID | **O(n)** | Procura o registro e ajusta referências |
| Selection Sort | **O(n²)** | Faz sucessivas comparações com os nós restantes |
| Estatísticas | **O(n)**, em média | Percorre a lista e agrega contagens em dicionário |

A complexidade de espaço adicional da ordenação implementada é O(1); a contagem de categorias utiliza O(k) espaço adicional, sendo k o número de categorias distintas. Essas classificações descrevem a implementação adotada, não tempos cronometrados.

---

## 7.Testes
Foram reportados 22 casos de teste aprovados em sua execução final. Houve uma primeira rodada de 17 casos, na qual 15 passaram e 2 falharam (T09 e T11); após ajustes, ambos foram repetidos e aprovados. Em seguida, os cinco testes de lista vazia (T18–T22) foram aprovados.

Resultado final informado: 22/22 aprovados (100%). Veja [`TESTES.md`](TESTES.md) para os casos, entradas e saídas esperadas. As aprovações foram confirmadas pelo desenvolvedor; anexar capturas ou gravação das saídas reais como evidência da execução.

## Evidências de funcionamento

As capturas de tela estão disponíveis na pasta
[evidencias](./evidencias).

- [Cadastro](./evidencias/01_cadastro.jpeg)
- [Busca por ID](./evidencias/02_busca_id.jpeg)
- [Exclusão](./evidencias/03_exclusao.jpeg)
- [Ordenação](./evidencias/04_ordenacao.jpeg)
- [Estatísticas](./evidencias/05_estatisticas.jpeg)

---

## 8.Como executar

1.Instalar Python 3.

2.Manter Main.py e lista_encadeada.py na mesma pasta.

3.Abrir um terminal nessa pasta e executar: python Main.py

---

## 9.Limitações e melhorias futuras
Os dados ficam em memória: ao fechar o programa, os registros criados ou alterados pelo usuário não são preservados. A inicialização adiciona novamente os três exemplos. Persistência com arquivos CSV ou JSON, além de mais filtros de busca, são possíveis melhorias futuras, mas não são requisitos desta entrega.

---

## 10.Conclusão
O projeto aplica lista encadeada, busca sequencial, Selection Sort e operações CRUD a um catálogo de serviços de documentação. As funções principais e os cenários de erro foram validados por uma bateria de 22 testes informados como aprovados. A solução prioriza clareza de implementação, organização e demonstração das estruturas e dos algoritmos, como solicitado na atividade de DSA.
