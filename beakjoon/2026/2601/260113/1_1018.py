# import sys

# n, m = map(int, sys.stdin.readline().split())
# board = []
# cnt = 0

# bCnt = 0
# wCnt = 0
# for _ in range(n):
#     line = list(sys.stdin.readline().rstrip())
#     for i in range(len(line)):
#         if line[i] == "B":
#             bCnt += 1
#         else:
#             wCnt += 1
#     board.append(line)

# color = ""

# for i in range(n):
#     for j in range(m):
#         if i == 0 and j == 0:
#             color = board[0][0]
#         elif i != 0 and j == 0:
#             if board[i - 1][0] == board[i][0]:
#                 cnt += 1
#                 if board[i][0] == "W":
#                     board[i][0] = "B"
#                 else:
#                     board[i][0] = "W"
#         else:
#             if board[i][j - 1] == board[i][j]:
#                 cnt += 1
#                 if board[i][j] == "W":
#                     board[i][j] = "B"
#                 else:
#                     board[i][j] = "W"
# print(cnt)

# helped by gemini

import sys

# 1. Read Input
n, m = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append(sys.stdin.readline().rstrip())

min_repaints = 64  # Max possible error is 64 (8x8)

# 2. Slide the 8x8 window
# Range is (n - 7) because if n=8, range(1) gives index 0 only.
for i in range(n - 7):
    for j in range(m - 7):

        count_w_start = 0  # Cost if top-left is 'W'
        count_b_start = 0  # Cost if top-left is 'B'

        # 3. Check the 8x8 square starting at (i, j)
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                # Even sum means it should match the top-left color
                # Odd sum means it should be the opposite color
                is_even = (a + b) % 2 == 0

                if is_even:
                    # If (row+col) is even, it should match the start color
                    if board[a][b] != "W":
                        count_w_start += 1
                    if board[a][b] != "B":
                        count_b_start += 1
                else:
                    # If (row+col) is odd, it should act opposite
                    if board[a][b] != "B":
                        count_w_start += 1
                    if board[a][b] != "W":
                        count_b_start += 1

        # 4. Find the minimum cost for this specific 8x8 block
        current_min = min(count_w_start, count_b_start)

        # 5. Update the global minimum
        if current_min < min_repaints:
            min_repaints = current_min

print(min_repaints)
