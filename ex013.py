s = float(input('Qual o salário do funcionário? R$'))
a = float(input('Qual o aumento percentual? %'))
sca = s + (s * (a/100))
print('O valor do salário após o aumento de {}% será de R${}'.format(a,sca))
