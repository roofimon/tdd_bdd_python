from next_lib import *
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)


@scenario('cucumber.feature', 'Arguments for given, when, thens')
def test_arguments_for_given_when_thens():
    """Arguments for given, when, thens."""

@given(parsers.parse("there are {start:d} cucumbers"), target_fixture="there_are_5_cucumbers")
def there_are_5_cucumbers(start):
    """there are 5 cucumbers."""
    return cucumber(start)


@when(parsers.parse("I eat {eat:d} cucumbers"))
def i_eat_2_cucumbers(there_are_5_cucumbers, eat):
    """I eat 2 cucumbers."""
    there_are_5_cucumbers['eat'] += eat


@then(parsers.parse("I should have {left:d} cucumbers"))
def i_should_have_0_cucumbers(there_are_5_cucumbers, start, left):
    """I should have 0 cucumbers."""
    assert there_are_5_cucumbers['start'] == start
    assert start - there_are_5_cucumbers['eat'] == left