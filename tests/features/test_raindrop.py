from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('raindrops.feature', 'Outlined given, when, thens')
def test_outlined_given_when_thens():
    """Outlined given, when, thens."""


@given('there are <start> cucumbers')
def there_are_start_cucumbers():
    """there are <start> cucumbers."""
    pass


@when('I eat <eat> cucumbers')
def i_eat_eat_cucumbers():
    """I eat <eat> cucumbers."""
    pass


@then('I should have <left> cucumbers')
def i_should_have_left_cucumbers():
    """I should have <left> cucumbers."""
    pass