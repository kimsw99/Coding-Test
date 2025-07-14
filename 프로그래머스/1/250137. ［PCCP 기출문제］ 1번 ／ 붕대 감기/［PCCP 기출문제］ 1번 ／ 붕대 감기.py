def solution(bandage, health, attacks):
    band_time, x, y = bandage
    sucess_count = 0 
    time = 0
    max_health = health
    times = [i[0] for i in attacks]
    while time <= attacks[-1][0]:
        if time in times:
            health -= attacks[times.index(time)][1]
            sucess_count = 0
        elif health < max_health:
            health += x
            sucess_count += 1
            if sucess_count == band_time and health < max_health:
                health += y
                sucess_count = 0
            if health > max_health:
                health = max_health

        if health <= 0:
            return -1
        time +=1
    return health