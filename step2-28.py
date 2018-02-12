count = int(input())

GAME_COUNT = 0
WIN_COUNT = 1
ADRAW_COUNT = 2
FAIL_COUNT = 3
SCORE_COUNT = 4

results = {}

for i in range(count):
    game = input().split(';')
    t1_name = game[0]
    results.setdefault(t1_name, [0, 0, 0, 0, 0])
    results[t1_name][GAME_COUNT] += 1
    t1_score = int(game[1])

    t2_name = game[2]
    results.setdefault(t2_name, [0, 0, 0, 0, 0])
    results[t2_name][GAME_COUNT] += 1
    t2_score = int(game[3])

    if t1_score > t2_score:
        results[t1_name][WIN_COUNT] += 1
        results[t1_name][SCORE_COUNT] += 3
        results[t2_name][FAIL_COUNT] += 1
    elif t1_score < t2_score:
        results[t1_name][FAIL_COUNT] += 1
        results[t2_name][WIN_COUNT] += 1
        results[t2_name][SCORE_COUNT] += 3
    else:
        results[t1_name][ADRAW_COUNT] += 1
        results[t2_name][ADRAW_COUNT] += 1
        results[t1_name][SCORE_COUNT] += 1
        results[t2_name][SCORE_COUNT] += 1

for k, v in results.items():
    print(k, end=':')
    print(*v)

