data = input().strip().split(" ")
T = int(data[0])
N = int(data[1])
nums = input().strip().split(" ")
nums = list(map(int, nums))

seen = {}
for num in nums:
    complement = T - num
    if complement in seen:
        pair = sorted((num, complement))
        print(f"{pair[0]} {pair[1]}")
        exit()
    seen[num] = True
