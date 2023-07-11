# 贷款期限不变，降低月还款额

MAX_N = 12
MAX_X = 300000

for n in range(3, MAX_N + 1, 3):
    # 剩余期数
    RES_N = 300 - n
    # 剩余款项
    RES_X = 36200 * (100 - n // 3)
 
    # 提前还款额只能精确到 0.1 万
    for x in range(0, MAX_X + 1, 1000):
        if (RES_X - x) % RES_N == 0:
            y = (RES_X - x) // RES_N
            # 并且要求新的月还款额是整百
            if y % 100 == 0:
                print(f"{n}\t{x}\t{y}")

# 3       198000  11400
# 6       49000   11900
# 6       196000  11400
# 9       194000  11400
# 12      48000   11900
# 12      192000  11400