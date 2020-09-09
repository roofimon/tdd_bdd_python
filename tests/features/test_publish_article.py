from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)



@scenario('publish_article.feature', 'Publishing the article')
def test_publishing_the_article():
    """Publishing the article."""
    pass


@given('I have an article')
def i_have_an_article():
    """I have an article."""
    pass


@given('I\'m an author user')
def im_an_author_user():
    """I'm an author user."""
    pass


@when('I go to the article page')
def i_go_to_the_article_page():
    """I go to the article page."""
    pass


@when('I press the publish button')
def i_press_the_publish_button():
    """I press the publish button."""
    pass


@then('I should not see the error message')
def i_should_not_see_the_error_message():
    """I should not see the error message."""
    pass


@then('the article should be published')
def the_article_should_be_published():
    """the article should be published."""
    pass