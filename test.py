import solve
import time
from decimal import Decimal,getcontext

def test(tail:int=10,prec:int=15) -> list[dict]:

    getcontext().prec = prec
    real_e = "2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274"

    data = []

    for precision in range(3,tail+1):

        n = 1
        start = time.time()
        test_e = solve.approximation1(n,prec=prec)
        time_delta = time.time() - start
        while str(test_e)[:precision] != real_e[:precision]:
            
            start = time.time()
            n *= 2
            test_e = solve.approximation1(n,prec=prec) 
            time_delta = time.time()-start
        data.append({
            "precision" : precision,
            "Approximation" : "Approximation1",
            "time": time_delta,
            "e_value" : str(test_e),
            "n" : n
        })

        n = 1
        start = time.time()
        test_e = solve.approximation2(n,prec=prec)
        time_delta = time.time() - start
        while str(test_e)[:precision] != real_e[:precision]:
            
            start = time.time()
            n *= 2
            test_e = solve.approximation2(n,prec=prec) 
            time_delta = time.time()-start
        data.append({
            "precision" : precision,
            "Approximation" : "Approximation2",
            "time": time_delta,
            "e_value" : str(test_e),
            "n" : n
        })

        n = 1
        start = time.time()
        test_e = solve.approximation3(n,prec=prec)
        time_delta = time.time() - start
        while str(test_e)[:precision] != real_e[:precision]:
            
            start = time.time()
            n += 1
            test_e = solve.approximation3(n,prec=prec) 
            time_delta = time.time()-start
        data.append({
            "precision" : precision,
            "Approximation" : "Approximation3",
            "time": time_delta,
            "e_value" : str(test_e),
            "n" : n
        })


    return data


def save_json(filename="data.json",tail:int=10,prec:int=100):
    data = test(tail=tail,prec=prec)
    import json
    with open(filename, 'w') as f:
        json.dump({"data":data}, f, indent=4)
        
if __name__ == "__main__":
    save_json(tail=15,prec=100)



