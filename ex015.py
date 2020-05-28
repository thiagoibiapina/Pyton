k = float(input('Quantos Km foram percorridos?:'))
d = int(input('Quantos dias o carro foi utilizado?:'))
ct = (k * 0.15) + (d * 60)
print('O total a pagar por {} dias e {}km roddados é R$ {:.2f}'.format(d,k,ct))
