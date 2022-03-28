import json

with open("Quake.txt", "r") as file:
    linesarray = file.readlines()
    game = 1
    games = []
    for line in range(len(linesarray)):
        if "InitGame:" in linesarray[line]:
            g = {"game": game, "status": []}
            s = {"total_kills": 0, "players": []}
            ids = []

        if "ClientUserinfoChanged:" in linesarray[line]:
            id = int(linesarray[line][30]) - 1
            nome = linesarray[line].split('n\\')[1].split('\\t')[0]

            if id not in ids:
                s['players'].append(
                    {"id": id, "nome": nome, "kills": 0, "old_names": []})
                ids.append(id)

            for player in s['players']:
                if (player['id'] == id) and (player['nome'] != nome) and (nome not in player['old_names']):
                    player['old_names'].append(nome)

        if "Kill:" in linesarray[line]:
            s['total_kills'] += 1
            if "Kill: 1022" in linesarray[line]:
                id = int(linesarray[line][18])-1
                for player in s['players']:
                    if (player['id'] == id):
                        player['kills'] -= 1
            elif linesarray[line][13] != linesarray[line][15]:
                id = int(linesarray[line][13]) - 1
                for player in s['players']:
                    if (player['id'] == id):
                        player['kills'] += 1

        if "ShutdownGame:" in linesarray[line]:
            g['status'] = s
            games.append(g)
            game += 1

    with open("final.json", "w") as final:
        json.dump(games, final, indent=2)
