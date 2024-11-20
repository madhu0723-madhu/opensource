# Read the input values
A, B, C, X = map(int, input().strip().split())

# Check the sums of all pairs
if (A + B >= X) or (A + C >= X) or (B + C >= X):
    print("YES")
else:
    print("NO")
