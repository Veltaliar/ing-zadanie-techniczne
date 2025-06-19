from playwright.sync_api import expect
from constants.cookies import COOKIE_STATE_ENABLED_ANALYTICS


def test_analytics_cookies_enabled(home_page):
    """Test checks if GDPR cookie have correct value after enabling analytics cookies."""
    home_page.goto() \
             .click_adjust_cookies()
             
    expect(home_page.analytics_cookie_state).to_have_attribute("aria-checked", "false")
    expect(home_page.marketing_cookie_state).to_have_attribute("aria-checked", "false")

    home_page.click_analytics_cookies() \
             .click_accept_selected()

    assert home_page.get_gdpr_cookie_value() == COOKIE_STATE_ENABLED_ANALYTICS

