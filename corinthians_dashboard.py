import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
import numpy as np
import warnings
warnings.filterwarnings('ignore')

jogos_raw = [
    ("2024-01-21","Paulistão","Guarani",1,0,"Casa"),
    ("2024-02-01","Paulistão","Portuguesa",3,0,"Fora"),
    ("2024-02-10","Paulistão","Botafogo-SP",3,1,"Casa"),
    ("2024-02-18","Paulistão","Palmeiras",0,0,"Fora"),
    ("2024-02-25","Paulistão","São Paulo",0,1,"Casa"),
    ("2024-03-28","Paulistão","Palmeiras",0,2,"Casa"),
    ("2024-04-10","Copa do Brasil","Cianorte",3,0,"Fora"),
    ("2024-04-24","Copa do Brasil","São Bernardo",2,0,"Fora"),
    ("2024-05-15","Copa do Brasil","América-RN",2,1,"Fora"),
    ("2024-05-22","Copa do Brasil","América-RN",2,1,"Casa"),
    ("2024-06-05","Copa do Brasil","Juventude",1,0,"Casa"),
    ("2024-06-26","Copa do Brasil","Juventude",1,0,"Fora"),
    ("2024-07-17","Copa do Brasil","Flamengo",0,0,"Fora"),
    ("2024-07-24","Copa do Brasil","Flamengo",2,1,"Casa"),
    ("2024-09-18","Copa do Brasil","Flamengo",0,1,"Fora"),
    ("2024-10-20","Copa do Brasil","Flamengo",0,0,"Casa"),
    ("2024-04-02","Sul-Americana","Racing-URU",1,1,"Fora"),
    ("2024-04-10","Sul-Americana","Nacional-PAR",4,0,"Casa"),
    ("2024-04-24","Sul-Americana","Sportivo Luqueño",3,1,"Casa"),
    ("2024-05-08","Sul-Americana","Racing-URU",2,0,"Casa"),
    ("2024-05-22","Sul-Americana","Nacional-PAR",1,0,"Fora"),
    ("2024-06-05","Sul-Americana","Sportivo Luqueño",1,2,"Fora"),
    ("2024-07-24","Sul-Americana","Boca Juniors",2,1,"Casa"),
    ("2024-07-31","Sul-Americana","Boca Juniors",1,0,"Fora"),
    ("2024-08-21","Sul-Americana","Fortaleza",1,0,"Fora"),
    ("2024-09-11","Sul-Americana","Fortaleza",0,0,"Casa"),
    ("2024-10-24","Sul-Americana","Racing-ARG",2,2,"Casa"),
    ("2024-10-31","Sul-Americana","Racing-ARG",1,2,"Fora"),
    ("2024-04-14","Brasileirão","Atlético-MG",0,0,"Casa"),
    ("2024-04-21","Brasileirão","Grêmio",1,1,"Fora"),
    ("2024-04-28","Brasileirão","Cuiabá",1,0,"Casa"),
    ("2024-05-05","Brasileirão","Bragantino",1,1,"Fora"),
    ("2024-05-12","Brasileirão","Fluminense",0,2,"Casa"),
    ("2024-05-19","Brasileirão","Vitória",0,1,"Fora"),
    ("2024-05-26","Brasileirão","Cruzeiro",1,2,"Casa"),
    ("2024-06-01","Brasileirão","Athletico-PR",0,0,"Fora"),
    ("2024-06-15","Brasileirão","Bahia",1,1,"Casa"),
    ("2024-06-22","Brasileirão","Criciúma",1,2,"Fora"),
    ("2024-06-30","Brasileirão","Fortaleza",0,1,"Casa"),
    ("2024-07-07","Brasileirão","São Paulo",0,1,"Fora"),
    ("2024-07-14","Brasileirão","Vasco",1,1,"Casa"),
    ("2024-07-21","Brasileirão","Botafogo",0,2,"Fora"),
    ("2024-07-28","Brasileirão","Juventude",2,2,"Casa"),
    ("2024-08-04","Brasileirão","Flamengo",0,0,"Fora"),
    ("2024-08-11","Brasileirão","Atlético-MG",1,2,"Fora"),
    ("2024-08-18","Brasileirão","Internacional",1,2,"Casa"),
    ("2024-08-25","Brasileirão","Palmeiras",0,1,"Fora"),
    ("2024-09-01","Brasileirão","Grêmio",2,1,"Casa"),
    ("2024-09-15","Brasileirão","Cuiabá",2,0,"Fora"),
    ("2024-09-22","Brasileirão","Bragantino",1,1,"Casa"),
    ("2024-09-29","Brasileirão","Fluminense",1,0,"Fora"),
    ("2024-10-06","Brasileirão","Vitória",1,0,"Casa"),
    ("2024-10-13","Brasileirão","Internacional",1,1,"Fora"),
    ("2024-10-17","Brasileirão","Athletico-PR",5,2,"Casa"),
    ("2024-10-23","Brasileirão","Cuiabá",1,0,"Fora"),
    ("2024-10-27","Brasileirão","Palmeiras",2,0,"Casa"),
    ("2024-11-03","Brasileirão","Bahia",1,0,"Fora"),
    ("2024-11-10","Brasileirão","Cruzeiro",2,0,"Casa"),
    ("2024-11-20","Brasileirão","Criciúma",4,2,"Fora"),
    ("2024-11-24","Brasileirão","Athletico-PR",2,1,"Casa"),
    ("2024-11-27","Brasileirão","São Paulo",2,1,"Casa"),
    ("2024-12-01","Brasileirão","Vasco",3,1,"Fora"),
    ("2024-12-04","Brasileirão","Juventude",2,0,"Fora"),
    ("2024-12-08","Brasileirão","Botafogo",1,1,"Casa"),
    ("2025-04-30","Copa do Brasil","Novorizontino",1,0,"Fora"),
    ("2025-05-14","Copa do Brasil","Novorizontino",2,0,"Casa"),
    ("2025-06-04","Copa do Brasil","Palmeiras",1,0,"Fora"),
    ("2025-06-18","Copa do Brasil","Palmeiras",1,1,"Casa"),
    ("2025-07-09","Copa do Brasil","Athletico-PR",1,0,"Fora"),
    ("2025-07-23","Copa do Brasil","Athletico-PR",2,1,"Casa"),
    ("2025-08-20","Copa do Brasil","Cruzeiro",2,0,"Casa"),
    ("2025-09-10","Copa do Brasil","Cruzeiro",1,1,"Fora"),
    ("2025-12-14","Copa do Brasil","Vasco",0,0,"Casa"),
    ("2025-12-21","Copa do Brasil","Vasco",2,1,"Fora"),
    ("2026-02-01","Supercopa","Flamengo",2,0,"Neutro"),
]

df = pd.DataFrame(jogos_raw, columns=['data','competicao','adversario','gols_cor','gols_adv','local'])
df['data'] = pd.to_datetime(df['data'])
df['resultado'] = df.apply(lambda r: 'V' if r.gols_cor > r.gols_adv else ('E' if r.gols_cor == r.gols_adv else 'D'), axis=1)
df['saldo'] = df['gols_cor'] - df['gols_adv']

def fase(d):
    if d < pd.Timestamp('2024-07-01'): return '1_Crise'
    elif d < pd.Timestamp('2024-10-17'): return '2_Transicao'
    elif d < pd.Timestamp('2025-01-01'): return '3_Virada'
    elif d < pd.Timestamp('2026-01-01'): return '4_Recuperacao'
    else: return '5_Campeao'

df['fase'] = df['data'].apply(fase)
df['mes_ano'] = df['data'].dt.to_period('M')

COR_V='#2e7d32'; COR_E='#e65100'; COR_D='#c62828'
COR_BG='#0f0f0f'; COR_TX='#ffffff'; COR_ST='#aaaaaa'; COR_GR='#2a2a2a'

plt.rcParams.update({'font.family':'DejaVu Sans','text.color':COR_TX,'axes.labelcolor':COR_TX,
    'xtick.color':COR_ST,'ytick.color':COR_ST,'axes.facecolor':'#1a1a1a',
    'figure.facecolor':COR_BG,'axes.edgecolor':COR_GR,'grid.color':COR_GR,
    'axes.grid':True,'grid.alpha':0.4})

fig = plt.figure(figsize=(22,16), facecolor=COR_BG)
fig.suptitle('SPORT CLUB CORINTHIANS PAULISTA  ·  From Relegation Candidate to National Champion  ·  2024–2026',
             fontsize=16, fontweight='bold', color=COR_TX, y=0.97)

gs = gridspec.GridSpec(4,4,figure=fig,hspace=0.6,wspace=0.4,
    height_ratios=[0.5,1.2,1.4,1.4],left=0.06,right=0.97,top=0.93,bottom=0.06)

total=len(df); v=(df.resultado=='V').sum(); e=(df.resultado=='E').sum(); d=(df.resultado=='D').sum()
gp=df.gols_cor.sum(); gc=df.gols_adv.sum(); saldo=gp-gc

kpis=[('Matches',str(total),'2024–2026'),('Wins',str(v),f'{round(v/total*100)}% win rate'),
      ('Draws',str(e),f'{round(e/total*100)}%'),('Losses',str(d),f'{round(d/total*100)}%'),
      ('Goals Scored',str(gp),f'{round(gp/total,1)}/match'),('Goals Conceded',str(gc),f'{round(gc/total,1)}/match'),
      ('Goal Diff.',('+' if saldo>0 else '')+str(saldo),'overall'),('Win Rate',f'{round(v/total*100)}%','all comps')]

gs_k=gridspec.GridSpecFromSubplotSpec(1,8,subplot_spec=gs[1,:],wspace=0.2)
for i,(lbl,val,sub) in enumerate(kpis):
    ax=fig.add_subplot(gs_k[i]); ax.set_facecolor('#1e1e1e'); ax.axis('off')
    cv=COR_V if 'Win' in lbl else (COR_D if ('Loss' in lbl or 'Conceded' in lbl or '-' in val) else ('#4fc3f7' if '+' in val else COR_TX))
    ax.text(0.5,0.72,lbl,transform=ax.transAxes,fontsize=8,color=COR_ST,ha='center',style='italic')
    ax.text(0.5,0.45,val,transform=ax.transAxes,fontsize=20,fontweight='bold',color=cv,ha='center')
    ax.text(0.5,0.15,sub,transform=ax.transAxes,fontsize=7.5,color=COR_ST,ha='center')

def aprov(g): return round((g.resultado=='V').sum()/len(g)*100,1)
am=df.groupby('mes_ano').apply(aprov).reset_index(); am.columns=['mes_ano','ap']
am['ms']=am['mes_ano'].dt.strftime('%b/%y')
def corf(p):
    if p<pd.Period('2024-07','M'): return COR_D
    elif p<pd.Period('2024-10','M'): return COR_E
    elif p<pd.Period('2025-01','M'): return COR_V
    else: return '#4fc3f7'
am['cor']=am['mes_ano'].apply(corf)

ax1=fig.add_subplot(gs[2,:2]); ax1.set_facecolor('#1a1a1a')
x=np.arange(len(am)); y=am['ap'].values
ax1.plot(x,y,color='#cccccc',linewidth=2,zorder=3)
for i in range(len(x)-1):
    ax1.fill_between([x[i],x[i+1]],[y[i],y[i+1]],alpha=0.3,color=am['cor'].iloc[i],zorder=2)
for xi,yi,c in zip(x,y,am['cor']): ax1.scatter(xi,yi,color=c,s=50,zorder=5,edgecolors=COR_BG,linewidths=1)
ax1.axhline(y=50,color=COR_E,linewidth=1,linestyle='--',alpha=0.7)
ax1.annotate('Ramón Díaz\nchega',xy=(7,y[7] if len(y)>7 else 40),xytext=(5,22),fontsize=7,color=COR_ST,
    arrowprops=dict(arrowstyle='->',color=COR_ST,lw=0.8))
ax1.annotate('Memphis\nDepay + 9 wins!',xy=(10,y[10] if len(y)>10 else 55),xytext=(9,72),fontsize=7,color='#4fc3f7',
    arrowprops=dict(arrowstyle='->',color='#4fc3f7',lw=0.8))
ax1.annotate('0.004% chance\nCopa BR 2025',xy=(10,y[10] if len(y)>10 else 55),xytext=(11,22),fontsize=6.5,color=COR_E,
    arrowprops=dict(arrowstyle='->',color=COR_E,lw=0.8))
ax1.set_xticks(x); ax1.set_xticklabels(am['ms'],rotation=45,ha='right',fontsize=7)
ax1.set_ylabel('Win Rate (%)',fontsize=9,color=COR_ST); ax1.set_ylim(0,100)
ax1.set_title('Monthly Win Rate Trend  ·  2024–2026',fontsize=10,color=COR_TX,pad=8,fontweight='bold')
patches=[mpatches.Patch(color=COR_D,alpha=0.7,label='Crisis H1/24'),
         mpatches.Patch(color=COR_E,alpha=0.7,label='Transition mid/24'),
         mpatches.Patch(color=COR_V,alpha=0.7,label='Turnaround late/24'),
         mpatches.Patch(color='#4fc3f7',alpha=0.7,label='Champions 25-26')]
ax1.legend(handles=patches,fontsize=7,loc='upper left',facecolor='#111111',edgecolor=COR_GR,labelcolor=COR_TX)

pc=df.groupby('competicao').agg(jogos=('resultado','count'),vitorias=('resultado',lambda x:(x=='V').sum()),
    empates=('resultado',lambda x:(x=='E').sum()),derrotas=('resultado',lambda x:(x=='D').sum())).reset_index()
pc['ap']=round(pc['vitorias']/pc['jogos']*100,1)
ordem=['Paulistão','Brasileirão','Copa do Brasil','Sul-Americana','Supercopa']
cp=pc[pc['competicao'].isin(ordem)].set_index('competicao').reindex(ordem).dropna()

ax2=fig.add_subplot(gs[2,2:]); ax2.set_facecolor('#1a1a1a')
yp=np.arange(len(cp))
ax2.barh(yp,cp['vitorias'],color=COR_V,alpha=0.85,label='Wins',height=0.6)
ax2.barh(yp,cp['empates'],left=cp['vitorias'],color=COR_E,alpha=0.85,label='Draws',height=0.6)
ax2.barh(yp,cp['derrotas'],left=cp['vitorias']+cp['empates'],color=COR_D,alpha=0.85,label='Losses',height=0.6)
for i,(idx,row) in enumerate(cp.iterrows()):
    ax2.text(row['jogos']+0.3,i,f"{row['ap']}%  ({int(row['jogos'])} matches)",va='center',fontsize=8,color=COR_ST)
ax2.set_yticks(yp); ax2.set_yticklabels(cp.index,fontsize=9)
ax2.set_title('Results by Competition',fontsize=10,color=COR_TX,pad=8,fontweight='bold')
ax2.legend(fontsize=8,loc='lower right',facecolor='#111111',edgecolor=COR_GR,labelcolor=COR_TX)
ax2.set_xlim(0,cp['jogos'].max()+14)

fases_labels={'1_Crise':'Crisis\nH1/24','2_Transicao':'Transition\nMid/24','3_Virada':'Turnaround\nLate/24','4_Recuperacao':'Recovery\n2025','5_Campeao':'Champion\n2026'}
gf=df.groupby('fase').agg(marcados=('gols_cor','sum'),sofridos=('gols_adv','sum'),jogos=('resultado','count')).reindex(fases_labels.keys()).dropna()

ax3=fig.add_subplot(gs[3,:2]); ax3.set_facecolor('#1a1a1a')
xf=np.arange(len(gf)); w=0.35
ax3.bar(xf-w/2,gf['marcados'],width=w,color='#ffffff',alpha=0.85,label='Scored')
ax3.bar(xf+w/2,gf['sofridos'],width=w,color=COR_D,alpha=0.85,label='Conceded')
for i,(idx,row) in enumerate(gf.iterrows()):
    s=int(row['marcados']-row['sofridos']); ss=('+' if s>0 else '')+str(s)
    ax3.text(i,max(row['marcados'],row['sofridos'])+1.5,ss,ha='center',fontsize=9,color=COR_V if s>0 else COR_D,fontweight='bold')
ax3.set_xticks(xf); ax3.set_xticklabels([fases_labels[k] for k in gf.index],fontsize=8)
ax3.set_title('Goals Scored vs Conceded by Phase',fontsize=10,color=COR_TX,pad=8,fontweight='bold')
ax3.legend(fontsize=8,facecolor='#111111',edgecolor=COR_GR,labelcolor=COR_TX)

ax4=fig.add_subplot(gs[3,2:]); ax4.set_facecolor('#111111'); ax4.axis('off')
ax4.set_title('Key Milestones  ·  The Full Story',fontsize=10,color=COR_TX,pad=8,fontweight='bold',loc='left',x=0.03)
ax4.axvline(x=0.12,ymin=0.05,ymax=0.95,color=COR_GR,linewidth=1.5)
marcos=[
    ("Jan 2024",COR_D,"Mano Menezes demitido após 4 derrotas"),
    ("Jul 2024",COR_E,"Ramón Díaz assume. Time era 19º no Brasileirão"),
    ("Out 2024",COR_E,"Eliminado da Sul-Americana e Copa do Brasil"),
    ("Out 2024",'#4fc3f7',"Apenas 0.004% de chance → Copa do Brasil 2025"),
    ("Out 2024",COR_V,"Memphis Depay chega. Série histórica de 9 vitórias!"),
    ("Nov 2024",COR_V,"Yuri Alberto: 30 gols, artilheiro do Brasil em 2024"),
    ("Dez 2024",COR_V,"7º lugar no Brasileirão → Vaga na Libertadores 2025"),
    ("Dez 2025",'#ffd700',"TETRACAMPEÃO Copa do Brasil — vence Vasco 2x0"),
    ("Fev 2026",'#ffd700',"SUPERCOPA REI — Corinthians 2x0 Flamengo"),
]
for i,(data,cor,texto) in enumerate(marcos):
    ypm=0.92-i*(0.85/len(marcos))
    ax4.scatter(0.12,ypm,color=cor,s=60,zorder=5,transform=ax4.transAxes)
    ax4.text(0.01,ypm,data,transform=ax4.transAxes,fontsize=7,color=cor,va='center',fontweight='bold')
    ax4.text(0.16,ypm,texto,transform=ax4.transAxes,fontsize=8,color=COR_TX,va='center')

fig.text(0.5,0.02,'Data: Brasileirão · Copa do Brasil · Copa Sul-Americana · Paulistão · Supercopa Rei  ·  Built with Python & Matplotlib',
         ha='center',fontsize=7.5,color=COR_ST)

plt.savefig(str(__import__('pathlib').Path.home()/'Downloads'/'corinthians_dashboard_2024_2026.png'),
            dpi=150,bbox_inches='tight',facecolor=COR_BG)
print('Dashboard salvo em ~/Downloads/corinthians_dashboard_2024_2026.png')
plt.show()
