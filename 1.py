#set 3 6 10 15 21 28
# 1x3 2x3 3x3+1 4x3+3 5x3+6 6x3+10
# (3) 3+3 3+3+4 3+3+4+5
while True:
    x = int(input())

    x = x+2
    x = (((x)*(x+1))/2)-x
    print(int(x))