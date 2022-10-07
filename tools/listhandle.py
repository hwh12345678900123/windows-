def halflist(lst: list) -> str:
    result = []
    for i in range(len(lst)):
        if i <= len(lst) / 2:
            result.append(lst[i])
        else:
            break
    result2 = ""
    for i in result:
        result2 += i
    return result2
