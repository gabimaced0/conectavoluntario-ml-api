# ConectaVoluntário Express – Classificação Inteligente de Prioridade

Este projeto é parte da Global Solution 2025/1 da FIAP, com foco na implementação de um sistema de classificação automática de pedidos emergenciais por prioridade, utilizando Machine Learning (Naive Bayes + Tfidf) e servindo como apoio à plataforma ConectaVoluntário Express.

---

## Objetivo

Desenvolver uma solução capaz de analisar o conteúdo de pedidos de ajuda cadastrados por organizações durante eventos extremos (como enchentes, deslizamentos e secas) e classificá-los automaticamente como alta, média ou baixa prioridade, facilitando a triagem e o engajamento de voluntários.

---

## 📁 Estrutura do Projeto

```
conectavoluntario-ml-api/
├── classificacao_prioridade_conectavoluntario.csv       # Dataset balanceado com 50 exemplos reais
├── modelo_prioridade.pkl                  # Modelo treinado salvo para uso na API
├── app.py                     # API FastAPI para classificação de novos pedidos
├── classificador_prioridade.ipynb  # Notebook com treino e avaliação do modelo
├── README.md                              # Instruções e explicações do projeto

```

---

## Tecnologias Utilizadas

-Python 3.10
-Scikit-learn
-TfidfVectorizer
-FastAPI
-Pandas
-Google Colab

## Como Executar o Projeto

Clone este repositório na sua máquina

### Pré-requisitos

Certifique-se de ter instalado:

- Python 3.10
- Pip atualizado

Instale as dependências com:

```bash
pip install fastapi scikit-learn pandas joblib uvicorn
```

Execute o script dentro da pasta da sua aplicação

```bash
uvicorn app:app --reload
```

Acesse a interface de teste da API:

```bash
http://localhost:8000/docs
```

---

Projeto desenvolvido por Fernando Henrique Vilela Aguiar (557525), Gabrielly Campos Macedo (558962) e Rafael Mocoto Magalhães Seo (554992) — FIAP

