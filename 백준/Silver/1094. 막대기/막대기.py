x = int(input())
stick_list = [64]
stick = 0
while True:
    if sum(stick_list) > x:
        stick = int(stick_list.pop() / 2)
        stick_list.append(stick)
        if sum(stick_list) < x:
            stick_list.append(stick)
    if sum(stick_list) == x:
        print(len(stick_list))
        break