'''from my_project.weather import *


def test_check_weather1():
    assert check_weather(22.00) == "hot"

def test_check_weather2():
    assert check_weather(5.00) == "average"

def test_check_weather3():
    assert check_weather(5.00) == "cold"

def test_check_weather4():
    assert check_weather(11.00) == "average"

def test_check_weather5():
    assert check_weather(30)=="hot"
    assert check_weather(11)=="cold" '''
#versione da stupidi


#versione giusta
from my_project.weather import check_weather
import pytest
@pytest.mark.parametrize("temperature, expected", [
(21.00, "hot"),
(13.00, "average"),
(0.00, "cold"),
(15.00, "cold")
])
def test_check_weather(temperature, expected):
    assert check_weather(temperature) == expected

