def solution(wallet, bill):
    fold_count = 0
    while True:
        if min(bill) > min(wallet):
            if bill[0] > bill[1]:
                bill[0] = int(bill[0] / 2)
                fold_count +=1
            else:
                bill[1] = bill[1] / 2
                fold_count +=1
        elif max(bill) > max(wallet):
            if bill[0] > bill[1]:
                bill[0] = int(bill[0] / 2)
                fold_count +=1
            else:
                bill[1] = bill[1] / 2
                fold_count +=1
        else:
            return fold_count
            break