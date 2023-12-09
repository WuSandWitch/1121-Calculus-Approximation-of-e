from decimal import Decimal,getcontext

def approximation1(n:int,prec:int = 100) -> Decimal:
    n = int(n)
    getcontext().prec = prec

    def riemann_sum(e:Decimal) -> Decimal:
        delta_x = Decimal(e - 1) / Decimal(n)

        d_dot_5 = Decimal(0.5)

        s = Decimal(0)
        for i in range(1,n + 1):
            s +=  Decimal(1)/Decimal(1+Decimal(i-d_dot_5)*delta_x)
        return s * delta_x
    
    lower = Decimal("2")
    upper = Decimal("3")

    step = 0

    old_s = 0

    while (step < n):
        
        middle = Decimal((lower+upper)/2)
        s = riemann_sum(middle)

        if old_s == s:
            break
        old_s = s
        
        if s > 1:
            upper = middle
        else:
            lower = middle

        step += 1
        print(f"step {step:4} : e value {middle}")
    return Decimal((lower+upper)/2)

def approximation2(n:int,prec:int = 100) -> Decimal:
    getcontext().prec = prec

    s = Decimal(1) + Decimal(1) / Decimal(n)
    s = s**Decimal(n)

    return s

def approximation3(n:int,prec:int = 100) -> Decimal:

    getcontext().prec = prec


    tmp = Decimal(1)
    s = Decimal(1)

    old_s = 0

    for i in range(1,n + 1):
        s += tmp / Decimal(i)
        tmp /= Decimal(i)

        if old_s == s:
            break
        old_s = s
    return s

if __name__ == '__main__':
    print(approximation1(1))
    print(approximation2(1e20))
    print(approximation3(100000000))
    print("2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274")