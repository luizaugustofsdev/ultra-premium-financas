import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_csv('data/transacoes_exemplo.csv', parse_dates=['data'])
divs = df[df['tipo']=='PROVENTO'].copy()
if divs.empty:
    print('Sem proventos no CSV de exemplo.')
else:
    divs['mes'] = divs['data'].dt.to_period('M').astype(str)
    por_mes = divs.groupby('mes')['proventos'].sum().reset_index()
    Path('out').mkdir(exist_ok=True, parents=True)
    plt.figure()
    plt.bar(por_mes['mes'], por_mes['proventos'])
    plt.title('Proventos por mês (exemplo)')
    plt.xlabel('Mês')
    plt.ylabel('R$')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('out/dividendos.png', dpi=150)
    print('Gerado out/dividendos.png')