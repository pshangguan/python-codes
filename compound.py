def solution(R,E):
    ## use generator
    while True:
        R = R * (1 + E)
        yield R
      
cnt=0
for n in solution(100,0.15):
    cnt+=1
    print("%d: %.2f" % (cnt,n))
    if (cnt > 30):
        break

