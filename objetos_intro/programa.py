from banco.cuentas import CuentaBancaria

cuenta1 = CuentaBancaria("105-356-643", "Benito Bodoque", 25000)
cuenta1.generar_balance()
cuenta1.depositar(5000)
cuenta1.generar_balance()