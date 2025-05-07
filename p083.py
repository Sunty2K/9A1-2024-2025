def can_transform(subarray, pattern):
    subarray.sort()
    pattern.sort()
    
    # Kiểm tra phép dịch chuyển đồng đều
    shift = subarray[0] - pattern[0]
    if all(subarray[i] - pattern[i] == shift for i in range(len(pattern))):
        return True
    
    return False

n = int(input())  # Số phần tử của dãy a
arr = [int(input()) for _ in range(n)]

c = int(input())  # Số phần tử của dãy mẫu
pattern = [int(input()) for _ in range(c)]

result = []
for i in range(n - c + 1):
    if can_transform(arr[i:i + c], pattern):
        result.append(i + 1)  # Vị trí bắt đầu (1-based index)

# Xuất kết quả
print(len(result))
for pos in result:
    print(pos)
