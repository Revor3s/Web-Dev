def sol(cntu,cntc):
    if cntu<cntc:
        print(cntu)
        return 0
    print(cntc)

if __name__ == '__main__':
    s=input()
    cntc,cntu=0,0
    l=len(s)
    vol=['u','i','e','y','o','a']
    for i in range(l):
        if s[i] in vol: 
            for j in range(i+1,l+1):
                subst=s[i:j]
                for z in range(0,l,j-i):
                    if s[z:j-i]==subst:
                        cntu+=1
        else: 
            for j in range(i+1,l+1):
                subst=s[i:j]
                for z in range(0,l,j-i):
                    if s[z:j-i]==subst:
                        cntu+=1
    sol(cntu,cntc)