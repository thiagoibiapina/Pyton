p = float(input('Qual o preço do produto? R$'))
pcd = p - (p * 0.05)
print('O produto que custava R$ {:.2f}\nNa promoção com 5% de desconto custa R${:.2f}'.format(p,pcd))
