def left_join(map1, map2):
    result = []

    for key, value in map1.items():
        inner = []
        inner.extend([key,value])

        if key in map2:
            inner.append(map2[key])
        else:
            inner.append(None)
        result.append(inner)

    return result
