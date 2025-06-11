def solution(arr):
    answer = 0
    items = arr
    while True:
        back_items = items[:]
        for i, item in enumerate(items):
            if item >= 50 and not item % 2:
                items[i] = item / 2
            elif item <50 and item % 2:
                items[i] = item *2 + 1
        if items == back_items:
            break
        answer += 1
    return answer