



from hypothesis import given, strategies as st
from pet_boarding import parse_booking, stay_average, payable_fee


# Test 1: Test parse_booking with random inputs
@given(st.one_of(st.text(), st.none()))
def test_parse_booking_no_crash(s):
    try:
        parse_booking(s)
    except Exception as e:
        assert False, f"parse_booking crashed with: {e}"


# Test 2: Test stay_average with random inputs
@given(st.one_of(st.text(), st.none()))
def test_stay_average_no_crash(s):
    try:
        stay_average(s)
    except Exception as e:
        assert False, f"stay_average crashed with: {e}"


# Test 3: Test payable_fee with random inputs
@given(st.one_of(st.text(), st.none()))
def test_payable_fee_no_crash(s):
    try:
        payable_fee(s)
    except Exception as e:
        assert False, f"payable_fee crashed with: {e}"
