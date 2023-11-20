var saldo = 0

        function atualizarSaldo() 
        {
            document.getElementById("saldo").innerText = saldo
        }

        function depositarDinheiro() 
        {
            let valor = parseFloat(document.getElementById("valor").value)
            if (!isNaN(valor) && valor > 0) {
                saldo += valor
                atualizarSaldo()
            } else {
                alert("Por favor, digite um valor válido.")
            }
        }

        function retirarDinheiro() 
        {
            let valor = parseFloat(document.getElementById("valor").value)
            if (!isNaN(valor) && valor > 0 && valor <= saldo) {
                saldo -= valor
                atualizarSaldo()
            } else {
                alert("Valor inválido ou insuficiente para retirada.")
            }
        }