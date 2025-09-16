import pandas as pd
from pathlib import Path

csv_path = Path('data/transacoes_exemplo.csv')
df = pd.read_csv(csv_path, parse_dates=['data'])

# Consolida posições por ticker (compras - vendas)
pos = (df[df['tipo'].isin(['COMPRA','VENDA'])]
       .assign(sinal=lambda d: d['tipo'].map({'COMPRA':1,'VENDA':-1}))
       .assign(qt_adj=lambda d: d['quantidade']*d['sinal'],
               vlr=lambda d: d['quantidade']*d['preco']*d['sinal'])
       .groupby('ticker', as_index=False)
       .agg(qt_total=('qt_adj','sum'), custo_total=('vlr','sum')))

# Dividendos por ticker
divs = (df[df['tipo']=='PROVENTO']
        .groupby('ticker', as_index=False)['proventos'].sum()
        .rename(columns={'proventos':'dividendos'}))

res = pos.merge(divs, on='ticker', how='left').fillna({'dividendos':0})
res['pm'] = (res['custo_total'].abs() / res['qt_total']).where(res['qt_total']!=0, 0)
res = res[['ticker','qt_total','pm','custo_total','dividendos']]
Path('data').mkdir(exist_ok=True, parents=True)
res.to_csv('data/carteira_resumo.csv', index=False)
print('Gerado data/carteira_resumo.csv')