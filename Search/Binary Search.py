# 1
def search(card, value):
    start, end = 0, len(card) - 1

    while start <= end:
        mid = (start + end) // 2

        if value < card[mid]:
            end = mid - 1
        elif value == card[mid]:
            return 1
        else:
            start = mid + 1
    return 0


# 2, start, end = 0, len() - 1
def search(card, value, start, end):
    mid = (start + end) // 2
    if start > end:
        return 0
    
    if value < card[mid]:
        return search(card, value, start, mid-1)
    elif value == card[mid]:
        return 1
    else:
        return search(card, value, mid+1, end)


# 시간 초과
def search(card, value):
    if not card:
        return 0

    start, end = 0, len(card)
    mid = (start + end) // 2

    if value < card[mid]:
        return search(card[:mid],value)
    elif value == card[mid]:
        return 1
    else:
        return search(card[mid+1:],value)   