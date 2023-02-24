<h3>Ping e desligamento automático de servidor</h3>
Esse código Python tem a função de verificar se um determinado equipamento está ativo na rede, enviando um e-mail de alerta caso ele esteja inativo e desligando automaticamente o servidor caso não haja resposta ao ping.

<h4>Como usar</h4>
Antes de executar o código, é necessário definir o IP do equipamento que será verificado. Isso pode ser feito na linha 38 do código, na chamada da função <b>check_ping()</b>.

Também é necessário preencher as informações de remetente, destinatário e senha na função <b>enviar_email()</b>, nas linhas 17, 18 e 20, respectivamente.

<h4>Funcionamento</h4>
O código usa o comando <b>ping</b> para verificar se o equipamento definido está ativo na rede. O resultado do ping é verificado na função <b>check_ping(hostname, silent=True)</b>, que retorna <b>True</b> se o equipamento está ativo e <b>False</b> caso contrário.

Se o equipamento estiver inativo, o código chama a função <b>enviar_email()</b> para enviar um e-mail de alerta para o destinatário definido. Além disso, é chamada a função <b>desligandoServidor()</b> para desligar automaticamente o servidor.

<h4>Módulos utilizados</h4>
O código utiliza os seguintes módulos do Python:

<b>os</b>: para executar o comando de desligamento do sistema na função desligandoServidor(). <br>
<b>platform</b>: para determinar o sistema operacional em uso e escolher o argumento correto para o comando ping. <br>
<b>subprocess</b>: para executar o comando ping e redirecionar a saída para o fluxo padrão ou para o dispositivo nulo, dependendo do valor do parâmetro silent. <br>
<b>smtplib</b>: para enviar um e-mail informando sobre a ativação do Nobreak. <br>
