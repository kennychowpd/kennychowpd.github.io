import math


def snail(smp):

    # OMG elegent, found on SOF
    unfldd = sum(smp, [])
    l = len(unfldd)
    if l == 0:
        return []
    sctn_l = int(math.sqrt(l))
    crrct_arr = list(chunker(unfldd, sctn_l))
    # [1,2,3,4,5]
    # [6,7,8,9,a]
    # [b,c,d,e,f]
    # [g,h,i,j,k]
    # [l,m,n,o,p]
    # 1,2,3,4,5|6,7,8,9,a|b,c,d,e,f|g,h,i,j,k|l,m,n,o,p
    # -------->|------> 2|7---> 9 3|6 <---- 4|<--------
    # ---1-----|---8-----|--11-----|----10---|----5----
    # 1) *pop lst[0]
    # 2) loop(pop lst[from 1 to n every 1][n])
    # 3) if i = lst[n] : pop reversed lst[n]
    # 4) and loop (pop lst[from n to 1][0])
    # 5) if i = lst[0] : *pop lst[0]
    # 6) loop from *
    answer = []
    while True:
        if sctn_l == 0:
            return sum(answer, [])
        if sctn_l != 0:
            answer.append(crrct_arr.pop(0))
            sctn_l -= 1
            if sctn_l > 1:
                for i in range(sctn_l - 1):
                    answer.append([crrct_arr[i].pop(-1)])
        if sctn_l != 0:
            answer.append(list(reversed(crrct_arr.pop(-1))))
            sctn_l -= 1
            if sctn_l != 1:
                for i in range(sctn_l - 1):
                    answer.append([crrct_arr[i * -1 - 1].pop(0)])
            else:
                pass

    # lovely generator! found on SOF
def chunker(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]