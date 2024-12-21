from main import fmt_price

if __name__ == '__main__':
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
