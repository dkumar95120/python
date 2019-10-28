def largestRectangle(h):
    if len(h) == 1:
        return h[0]
    min_height = min(h)
    area = min_height * len(h)
    i = h.index(min_height)
    if i == 0:
        max_area = max(area, largestRectangle(h[1:]))
    elif i == len(h) - 1:
        max_area = max(area, largestRectangle(h[:i]))
    else:
        max_area = max(area, largestRectangle(h[:i]), largestRectangle(h[i+1:]))
    return max_area

