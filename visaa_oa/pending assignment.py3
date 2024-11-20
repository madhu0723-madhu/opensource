X, Y, Z = map(int, input().strip().split())
total_time_required = X * Y
available_time = Z * 24 * 60
if total_time_required <= available_time:
    print("YES")
else:
    print("NO")
