#conversor de moedas

real = float(100.00)
cotacao_dolar = float(5.20)
cotacao_euro = float(5.50)

dolar = real / cotacao_dolar
euro = real / cotacao_euro

print('O valor em dólares é: %.2f' % dolar)
print('O valor em euros é: %.2f' % euro)
