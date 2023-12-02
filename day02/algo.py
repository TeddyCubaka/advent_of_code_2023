import json

with open("input.txt") as f:
    data = f.read().strip()

data = data.split('\n')
games = []

for game in data:
    steps_brut = game.split(':')[1].split(';')
    steps = []
    for step in steps_brut:
        step = step.replace(',', '')
        step = step.split(' ')

        index_blue = (step.index('blue') - 1) if 'blue' in step else None
        index_green = (step.index('green') - 1) if 'green' in step else None
        index_red = (step.index('red') - 1) if 'red' in step else None

        steps.append({
            "blue": int(step[index_blue]) if index_blue is not None else 0,
            "green": int(step[index_green]) if index_green is not None else 0,
            "red": int(step[index_red]) if index_red is not None else 0
        })

    games.append({
        "ID": int(game.split(':')[0].split('Game ')[1]),
        "steps": steps
    })

# first part


def is_possible(step):
    if step["red"] > 12:
        return False
    elif step["blue"] > 14:
        return False
    elif step["green"] > 13:  # debugging my code for one hour because this condition was 'blue' incase of 'green' 😃
        return False
    else:
        return True


valid_IDs = []

for game in games:
    is_pass = [is_possible(i) for i in game['steps']]
    if False not in is_pass:
        valid_IDs.append(game['ID'])


print(sum(valid_IDs))  # first part of the challenge

# second part


def get_max_values(step):
    max_value_db = {"blue": 0, "green": 0, "red": 0}
    for i in step:
        if i['blue'] > max_value_db['blue']:
            max_value_db['blue'] = i['blue']
        if i['green'] > max_value_db['green']:
            max_value_db['green'] = i['green']
        if i['red'] > max_value_db['red']:
            max_value_db['red'] = i['red']
    return max_value_db['blue'] * max_value_db['green'] * max_value_db['red']


sum = 0

for game in games:
    sum += get_max_values(game["steps"])


print(sum)


# print(json.dumps(games))
