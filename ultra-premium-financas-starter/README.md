# Ultra Premium — Finanças e Dividendos

Planilha + scripts Python para acompanhar patrimônio, dividendos (estilo Barsi), metas e simulações com inflação/CDI.

## Como usar rápido (sem instalar nada)
1. **Baixe** o arquivo `UltraPremium_Financas.xlsx` (modelo).
2. Abra a aba **Transacoes** e lance compras/vendas/dividendos.
3. Abra a aba **Carteira** para ver posição consolidada.
4. A aba **Dividendos** calcula o acumulado por ativo e por mês.

## Scripts Python (opcional)
- `scripts/gerar_resumo.py` lê `data/transacoes_exemplo.csv` e gera um `data/carteira_resumo.csv`.
- `scripts/plot_dividendos.py` gera `out/dividendos.png` (gráfico).

### Rodar
```bash
python -m venv .venv && . .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install pandas matplotlib
python scripts/gerar_resumo.py
python scripts/plot_dividendos.py
```

## Estrutura
```
data/
  transacoes_exemplo.csv
scripts/
  gerar_resumo.py
  plot_dividendos.py
out/   (saídas geradas)
UltraPremium_Financas.xlsx
```
