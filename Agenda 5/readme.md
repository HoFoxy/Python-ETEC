# ⚡ Cálculo de Consumo e Gasto de Aparelhos

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Energy](https://img.shields.io/badge/Energy-⚡-yellow?style=for-the-badge)

Este projeto realiza a estimativa do consumo de energia elétrica de um aparelho e calcula o seu custo mensal em reais.

A linguagem utilizada foi **Python**.

---

## 📌 Cálculo do consumo

O consumo mensal de energia é calculado com a seguinte fórmula:

(P × H × D) / 1000

Onde:
- **P** = potência do aparelho (em Watts)
- **H** = tempo médio de uso diário (em horas)
- **D** = número de dias (considerado 30 dias)

A divisão por 1000 converte o valor de **Watts para quilowatt-hora (kWh)**, unidade utilizada nas contas de energia elétrica.

---

## 💰 Cálculo do custo

Após obter o consumo em kWh, o valor gasto é calculado por:

custo mensal = consumo (kWh) × valor do kWh

---

## ▶️ Como executar

1. Baixe o arquivo do código
2. Execute o script em Python
3. Insira as informações solicitadas:
   - Nome do aparelho
   - Potência (W)
   - Tempo de uso diário (h)

O programa retornará o consumo mensal e o custo estimado.

---

## 🎯 Objetivo

Projeto desenvolvido com foco em prática de lógica de programação e conceitos básicos de consumo de energia elétrica.