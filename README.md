# desafio-PRAGMA - TESTE DE TI/LÓGICA

Construa um Parser para o arquivo de log. 
O arquivo "Quake.txt" é gerado pelo servidor de Quake 3 Arena. Nele está registrado informações sobre as partidas, informações como: Quando começa, quando termina, quem matou quem, quem "se matou" (caiu no vazio, explodiu a si próprio), entre outros. O Parser deve ser capaz de ler o arquivo, agrupar os dados de cada partida, e organizar as suas informações.
 
Exemplo:
21:42 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT
* O player "Isgalamido" morreu por que estava ferido e caiu de uma altura que o matou.
 2:22 Kill: 3 2 10: Isgalamido killed Dono da Bola by MOD_RAILGUN
* O player "Isgalamido" matou o player "Dono da Bola" usando a arma "Railgun".
Para cada jogo o Parser deve gerar algo como: 
[{<br/>
  "game": 1,<br/>
  "status": {<br/>
     "total_kills": 45,<br/>
     "players": [<br/>
		{<br/>
			"id": 1,<br/>
			"nome": "Mocinha",<br/>
			"kills": 5,<br/>
			"old_names": ["Dono da bola"]<br/>
		},<br/>
		{<br/>
			"id": 2,<br/>
			"nome": "Isgalamido",<br/>
			"kills": 18,<br/>
			"old_names": []<br/>
		},<br/>
		{<br/>
			"id": 3,<br/>
			"nome": "Zeh",<br/>
			"kills": 20,<br/>
			"old_names": []<br/>
		}<br/>
	]<br/>
  }<br/>
}]<br/>
Observação1: Quando o <world> mata o player ele perde -1 kill. <world> não é um player e não deve aparecer na lista de players e nem no dicionário de kills. total_kills são os kills dos games, isso inclui mortes do <world>.
O Comando ClientUserinfoChanged indica a definição do nome do jogador.
  
Observação2: Não foi dito nada a respeito de quando o jogador se mata. Na primeira versão, o programa contabilizava um kill para quem se matava. Contudo, não faz sentido um jogador ganhar um ponto por ter se matado. Logo, quando o jogador se mata não ganha nenhum kill.
  
Observação3: O programa foi feito em Python e o arquivo chamado final.json é o arquivo que é gerado após a leitura do arquivo de log Quake.txt.
