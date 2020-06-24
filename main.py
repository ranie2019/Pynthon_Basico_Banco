from cliente import Cliente
from conta import Conta

cliente1 = Cliente('Ranie', '123.456.789-10', 27)


conta_rani = Conta(cliente1, 0, 1000)

print(conta_rani.cliente.nome, conta_rani.consulta_saldo())

conta_rani.depositar(1000)

print(conta_rani.consulta_saldo())

conta_rani.sacar(500)

print(conta_rani.consulta_saldo())

conta_rani.sacar(1000)

print(conta_rani.consulta_saldo())