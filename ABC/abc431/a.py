import sys

input = sys.stdin.readline

h, b = map(int, input().split())

print(max(0, h-b))