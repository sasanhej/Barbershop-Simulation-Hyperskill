import numpy as np
s, a, b, k1 = input().split()
s = int(s)
a = int(a)
b = int(b)
k1 = int(k1)
iterations=5000
results=list([])
for k in  [k1-1,k1]:
    mwtm = list([])
    cdm = list([])
    mnplm = list([])
    close = 7 * 60

    for t in range(iterations):
        o = list([])
        p = list([])
        arrival = 0
        service = 0
        while True:
            arrival += np.random.exponential(scale=s)
            if arrival > close:
                break
            service = np.random.uniform(low=a, high=b)
            o.append([arrival, service, 0])
        q = list([])
        f = list([])
        mwt = 0
        cd = 0
        mnpl = 0
        i = 0
        while q or i < close:
            if o:
                if o[0][0] <= i:
                    q.append(o.pop(0))
            for j in range(k):
                for l in p:
                    if i >= l:
                        p.remove(l)
            while q and k - len(p):
                mwt = max(i-q[0][0], mwt)
                q[0][2] = i-q[0][0]
                cd = max((i+q[0][1]), cd)
                p.append(i + q[0][1])
                f.append(q.pop(0))
            mnpl = max(len(q), mnpl)
            i += 1
        mwtm.append(mwt)
        cdm.append(max(0, cd-close))
        mnplm.append(mnpl>5)

    mwtf = sorted(mwtm)[int(iterations * 0.95)]
    cdf = sum(cdm)/len(cdm)
    mnplf = sum(mnplm)/len(mnplm)

    results.append([mwtf, cdf, mnplf])

print(results[0][0]-results[1][0], results[0][1]-results[1][1], results[0][2]-results[1][2], sep='\n')
