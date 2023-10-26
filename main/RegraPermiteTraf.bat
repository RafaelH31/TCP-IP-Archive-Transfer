@echo off
echo Permitindo tráfico para a porta 8080
netsh advfirewall firewall add rule name="Permit Porta 8080" dir=in action=allow protocol=TCP localport=8080
echo Regra Criada.
pause
