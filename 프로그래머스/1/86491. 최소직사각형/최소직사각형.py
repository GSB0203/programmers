def solution(sizes):
    width = 0
    height = 0

    for w, h in sizes:
        w, h = max(w, h), min(w, h)
        width = max(width, w)
        height = max(height, h)

    return width * height
