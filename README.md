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

### 2. Modelo dos registros

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
