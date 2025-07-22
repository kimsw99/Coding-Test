def solution(n, w, num):
    # num의 층(row)과 열(col) 계산
    row = (num - 1) // w
    pos = (num - 1) % w
    col = pos if row % 2 == 0 else w - 1 - pos

    # 꺼내야 하는 상자 수 (num 포함)
    count = 1

    # 위층들 확인
    for r in range(row + 1, (n - 1) // w + 1 + 1):
        start = r * w + 1
        end = min((r + 1) * w, n)
        length = end - start + 1  # 위층 상자 개수

        # 층의 실제 인덱스 (0 ~ length-1)
        if r % 2 == 0:
            # 왼 -> 오른
            if col < length:
                count += 1
        else:
            # 오른 -> 왼
            if (w - 1 - col) < length:
                count += 1

    return count
