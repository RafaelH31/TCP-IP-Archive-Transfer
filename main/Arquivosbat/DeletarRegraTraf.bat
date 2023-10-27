@echo Excluindo regra que perSitia o tráfico
netsh advfirewall firewall delete rule name="Permit Porta 8080"
echo Regra excluida
pause
