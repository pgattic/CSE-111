from address import extract_city, extract_state, extract_zipcode
import pytest

my_address = "18097 Cavnasback Dr., Clinton Twp., Michigan 48038"

def test_extract_city():
	assert extract_city(my_address) == "Clinton Twp."

def test_extract_state():
	assert extract_state(my_address) == "Michigan"

def test_extract_zipcode():
	assert extract_zipcode(my_address) == "48038"



pytest.main(["-v", "--tb=line", "-rN", __file__])
