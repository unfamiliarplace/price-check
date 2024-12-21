from main import fmt_price, get_matching_combos

def test_fmt_price() -> None:
    assert fmt_price(1) == '$0.01'
    assert fmt_price(20) == '$0.20'
    assert fmt_price(3_00) == '$3.00'
    assert fmt_price(4_01) == '$4.01'
    assert fmt_price(50_00) == '$50.00'
    assert fmt_price(600_00) == '$600.00'
    assert fmt_price(7_000_00) == '$7,000.00'
    assert fmt_price(80_000_00) == '$80,000.00'
    assert fmt_price(900_000_00) == '$900,000.00'
    assert fmt_price(1_000_000_00) == '$1,000,000.00'

def test_combos() -> None:
    t1 = 3423
    p1 = [1042,1042,4894,2625,2317,2545,2469,2497,2469,3018,599,599,799,399,399,2548,2095,1917,2619,2548]
    c1 = {frozenset((2625,399,399))}

    r1 = set(frozenset(c) for c in get_matching_combos(t1, p1))
    assert r1 == c1

def run() -> None:
    test_fmt_price()
    test_combos()

if __name__ == '__main__':
    run()
