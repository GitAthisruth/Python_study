n, k = map(int, input().split())
scores = list(map(int, input().split()))

print("kth score is :",scores[k-1])
num = 0
for score in scores:
    if score>=scores[k] and score>0:
        num+=1
print(f"number of contestants who advance to the next round is {num}")

