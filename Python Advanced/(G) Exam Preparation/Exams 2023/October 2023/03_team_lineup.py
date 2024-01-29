def team_lineup(*args):
    data = {}
    for name, country in args:
        if country not in data:
            data[country] = [name]

        data[country].append(name)

    sorted_data = dict(sorted(data.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

    result = ''
    for key, value in sorted_data.items():
        result += f'{key}:\n'

        for el in value:
            result += f'  -{el}\n'

    return result


'''TESTS'''

print(team_lineup(
   ("Harry Kane", "England"), 
   ("Manuel Neuer", "Germany"), 
   ("Raheem Sterling", "England"), 
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))

print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))

