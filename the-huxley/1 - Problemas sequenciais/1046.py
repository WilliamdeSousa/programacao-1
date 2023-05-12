tot_video = float(input())
tot_audio = float(input())
tot_dados = float(input())
cap = float(input())
dados_max = (tot_video * 5.2 + tot_audio * 3.4 + tot_dados * 1.5) / cap # QDmax = (TVideo*5.2 + TAudio*3.4 + TDados*1.5) / Capacidade
print(f'{dados_max:.2f}')
