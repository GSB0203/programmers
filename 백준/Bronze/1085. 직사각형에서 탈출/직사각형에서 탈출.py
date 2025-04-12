x, y, w, h = map(int, input().split())

min_w = min(x, (w - x))
min_h = min(y, (h - y))
print(min(min_w, min_h))