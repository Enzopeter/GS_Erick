## Evidências e casos de teste — Citizen Assist AI

---

Referência: Global Solution 2026.2 — Citizen Tech / DSA
Situação: 22 testes reportados como aprovados após correções
Observação: o resultado observado abaixo é o status de aprovação informado pelo desenvolvedor. Não representa uma transcrição literal ou uma captura do terminal. Adicione arquivos reais à pasta evidencias/ e faça referência a eles antes da entrega.

Para executar de maneira reproduzível, reinicie Main.py antes de cada caso, exceto quando a sequência do caso exigir operações sucessivas. Os três registros iniciais têm IDs 1 (CIN), 2 (CPF) e 3 (Título de Eleitor).

| ID | Caso | Entrada / procedimento | Resultado esperado | Resultado observado (informado) |
| --- | --- | --- | --- | --- |
| T01 | Cadastro válido | Menu 1; ID 4; título `Passaporte`; preencher demais campos | Cadastro confirmado | Aprovado |
| T02 | ID duplicado | Menu 1; ID 3 | Impede duplicidade de ID | Aprovado |
| T03 | Título duplicado | Menu 1; ID 4; `Título de Eleitor` | Impede duplicidade de título | Aprovado |
| T04 | ID inválido | Menu 1; ID `abc` | Informa ID inválido | Aprovado |
| T05 | Campo vazio | Menu 1; ID 4; deixar título vazio; preencher demais campos | Rejeita campo vazio | Aprovado |
| T06 | Busca existente | Menu 3; ID 2 | Exibe Regularização do CPF | Aprovado |
| T07 | Busca inexistente | Menu 3; ID 999 | Serviço não encontrado | Aprovado |
| T08 | Categoria existente | Menu 4; `identidade` | Encontra Emissão da CIN | Aprovado |
| T09 | Categoria inexistente | Menu 4; `Transporte` | Nenhum serviço encontrado nessa categoria | Aprovado após correção |
| T10 | Atualização válida | Menu 5; ID 1; novo título `Solicitação da CIN`; preencher demais campos | Altera os dados e preserva ID | Aprovado |
| T11 | Título duplicado na atualização | Menu 5; ID 2; novo título `Título de Eleitor` | Impede alteração; mantém título do ID 2 | Aprovado após correção |
| T12 | Exclusão válida | Menu 6; ID 2; depois menu 2 | CPF não aparece na lista | Aprovado |
| T13 | Exclusão inexistente | Menu 6; ID 999 | Serviço não encontrado | Aprovado |
| T14 | Ordenação | Menu 7 | Títulos em ordem alfabética | Aprovado |
| T15 | Estatísticas | Menu 8 | Total 3 e uma entrada para cada categoria inicial | Aprovado |
| T16 | Opção inválida | Digitar `99` | Informa opção inválida | Aprovado |
| T17 | Encerramento | Menu 0 | Encerra normalmente | Aprovado |
| T18 | Listagem vazia | Excluir IDs 1, 2 e 3; menu 2 | Nenhum serviço cadastrado | Aprovado |
| T19 | Busca vazia | Após excluir IDs 1, 2 e 3; menu 3; ID 1 | Serviço não encontrado | Aprovado |
| T20 | Exclusão vazia | Após excluir IDs 1, 2 e 3; menu 6; ID 1 | A lista está vazia | Aprovado |
| T21 | Ordenação vazia | Após excluir IDs 1, 2 e 3; menu 7 | Informa lista vazia, sem erro | Aprovado |
| T22 | Indicadores vazios | Após excluir IDs 1, 2 e 3; menu 8 | Informa lista vazia, sem erro | Aprovado |

---

## Síntese da validação
Primeira bateria: 15/17 aprovados; T09 e T11 falharam.
Após correções: T09 e T11 aprovados; 17/17 aprovados.
Bateria complementar: T18 a T22 aprovados; 5/5 aprovados.
Total final reportado: 22/22 aprovados (100%).

---

## Evidências para anexar
Sugestão de capturas de tela do terminal, produzidas durante a execução real:
1. evidencias/01-menu-listagem.png — menu e lista inicial com três serviços.
2. evidencias/02-cadastro-validacoes.png — cadastro válido e rejeição de título/ID duplicados.
3. evidencias/03-buscas.png — busca existente e categoria inexistente (T09).
4. evidencias/04-atualizacao.png — rejeição de título duplicado na atualização (T11).
5. evidencias/05-ordenacao-estatisticas.png — ordenação e indicadores.
6. evidencias/06-lista-vazia.png — mensagem de lista vazia após remover todos os nós.
Não marque como anexadas evidências que ainda não foram capturadas. Se o professor solicitar demonstração em vídeo, grave uma execução real do menu e explique os trechos de inserir, excluir, buscar_por_id e ordenar no código.
