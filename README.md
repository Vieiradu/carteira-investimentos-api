# 📊 carteira-investimentos-api

> Projeto **2/3** (carro-chefe) do meu portfólio de Dev Júnior — backend Python.

Carteira de investimentos com **Django REST Framework** e **PostgreSQL**. O usuário
cadastra seus ativos e transações; a API calcula a posição atual cruzando com
cotações externas (brapi.dev). CRUD completo, autenticação JWT, testes e CI/CD.

## 🧭 Match com o roadmap
| Ponto do roadmap | Como este projeto cobre |
|---|---|
| Banco relacional — JOINs, indexes, uniques (P1) | Postgres + models User ↔ Ativo ↔ Transação |
| HTTP / API — todos os verbos (P2) | CRUD completo em DRF |
| Segurança da API — JWT (P2) | cada usuário só acessa a própria carteira |
| Testes — pytest, mock (P3) | unitários + integração com banco isolado |
| Classes / objetos / decorators (P8) | camada de services + decorators |
| Design Patterns — Strategy / Singleton (P9) | estratégia por tipo de ativo |
| Deploy automatizado — CI/CD (P7) | GitHub Actions (testa e deploya) |
| Git — rebase / release (P10 e P11) | issues guiadas de conflito e release |

## 🧱 Stack
`Python` · `Django` · `Django REST Framework` · `PostgreSQL` · `pytest` · `Docker`

## ✅ Como acompanhar
As tarefas de construção estão nas **Issues**, agrupadas por **Milestones** que
seguem a ordem de prioridade do roadmap.

---
🤖 Estrutura de estudo organizada com apoio do Claude Code.
