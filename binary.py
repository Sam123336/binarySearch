while True:
    try:
        while True:
            cards=list(map(lambda x:int(x),input().split(" ")))
            quer=int(input())
            def locatecard(card,quer):
               
                lo,hi=0,len(card)
                while lo <=hi:
                    mid = (lo+hi)//2
                    #print(mid)
                    mid_numm=card[mid]
                    s=0
                    p=1
                    while card[s]==card[p]:
                        s+=1
                        p+=1
                    while card[s]>=card[p]:
                        
                        if mid_numm==quer:
                            return mid
                        you=mid-1
                        while mid_numm<quer:
                            if card[you]==quer:
                                return you
                            you-=1
                        you=mid+1  
                        while mid_numm>quer:
                            if card[you]==quer:
                                return you
                            you+=1
                        return you
                    while card[s]<=card[p]:
                        if mid_numm==quer:
                            return mid
                        you=mid+1
                        while mid_numm<quer:
                            if card[you]==quer:
                                return you
                            you+=1
                        you=mid-1
                        while mid_numm>quer:
                            if card[you]==quer:
                                return you
                            you-=1
                        return-1
            result=locatecard(cards,quer)
            print(result)
            a=str(input("you wantto recheck(y/n)"))
            if a!="y":
                break
    except ValueError:
        print("input some intiger for creating a list")
    a=str(input("you wantto recheck(y/n)"))
    if a!="y":
        break
