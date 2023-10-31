@echo off

echo Permitindo trafico para a porta 8080
netsh advfirewall firewall add rule name="Permit Porta 8080" dir=in action=allow protocol=TCP localport=8080
echo Regra Criada.

echo pressione qualquer tecla para iniciar o progama
pause > nul

echo Iniciando o arquivo localhost.py
py localhost.py

echo agora que fechou o progama aperte qualquer tecla para fechar a porta 
pause > nul

@echo Excluindo regra que permite o tráfico
netsh advfirewall firewall delete rule name="Permit Porta 8080"
echo Regra excluída.

pause 