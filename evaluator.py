import random
import turingarena as ta

def test_case(A, B, C):
    perm = range(len(C))
    random.shuffle(perm)
    with ta.run_algorithm(ta.submission.source) as p:
        p.functions.get_two_sorted_lists_and_store_their_merge(len(A), A, len(B), B)
    except ta.AlgorithmError as e:
        print(f" error: {e}")
        ta.goals.setdefault("correct", False)
        ta.goals.setdefault("linear_merge", False)
        ta.goals.setdefault("correct_YES_certificate", False)

    for pi in perm:
        with ta.run_algorithm(ta.submission.source) as p:
            res = p.functions.tell_element_in_pos(pos)
        except ta.AlgorithmError as e:
            print(f" error: {e}")
            ta.goals.setdefault("correct", False)
            ta.goals.setdefault("linear_merge", False)
            ta.goals.setdefault("correct_YES_certificate", False)
        if res != C[pi]:
            ta.goals.setdefault("correct", False)
            ta.goals.setdefault("linear_merge", False)
            ta.goals.setdefault("correct_YES_certificate", False)
            print("Il numero che avevo in mente era %d, non %d come da tè affermato." % (N,res) )


def run_all_test_cases():
    C = range(1,1000000,1000)
    A = []
    B = []
    for c in C:
        if random.randint(0,1) == 1:
            A.append(c)
        else:
            B.append(c)
        test_case(A, B, C)
        
run_all_test_cases()        

ta.goals.setdefault("correct", True)
ta.goals.setdefault("linear_merge", True)
ta.goals.setdefault("direct_access", True)
print(ta.goals)
