import random
import turingarena as ta

def test_case(A, B, C):
    print(f"testing case len(A) = {len(A)}, len(B) = {len(B)}\t", end="")
    with ta.run_algorithm(ta.submission.source) as p:
        try:
            p.procedures.merge(len(A), A, len(B), B, len(C))
            
            res = [p.functions.getElement(i) for i in range(len(C))]
            
            for i in range(len(C)):
                
                if res[i] != C[i]:
                    print(f"\nWrong merge at element {i}: expected {C[i]}, found {res[i]}")
                    if len(C) <= 20:
                        print(f"A array = {A}")
                        print(f"B array = {B}")
                        print(f"Your merge = {res}")
                        print(f"Correct merge = {C}")
                    return False

        except ta.AlgorithmError as e:
            print(f"\nError: {e}")
            return False
    print("CORRECT")
    return True
       
def run_all_test_cases():
    cases = (10, 20, 50, 100, 1000, 10000)
    for c in cases:
        C = sorted([random.randint(0, 1000) for _ in range(c)])
        A = []
        B = []
        for x in C:
            if random.randint(0,1) == 1:
                A.append(x)
            else:
                B.append(x)
        ta.goals.check("correct", test_case, A, B, C)
        
run_all_test_cases()        

ta.goals.setdefault("correct", True)
