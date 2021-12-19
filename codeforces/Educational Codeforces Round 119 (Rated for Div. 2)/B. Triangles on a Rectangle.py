for _ in range(int(input())):
    w, h = map(int, input().split())
    w1 = list(map(int, input().split()))[1:]
    w2 = list(map(int, input().split()))[1:]
    h1 = list(map(int, input().split()))[1:]
    h2 = list(map(int, input().split()))[1:]
    w1.sort()
    w2.sort()
    h1.sort()
    h2.sort()
    max_w1 = w1[-1] - w1[0]
    max_w2 = w2[-1] - w2[0]
    max_h1 = h1[-1] - h1[0]
    max_h2 = h2[-1] - h2[0]
    print(max(max_w1 * h, max_w2 * h, max_h1 * w, max_h2 * w))
    