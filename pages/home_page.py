from playwright.sync_api import Page
from constants.urls import ING_HOME_PAGE

class HomePage():
    def __init__(self, page: Page):
        """Initialize locators."""
        self.page = page
        self.context = self.page.context
        self.adjust_cookies_button = page.get_by_role("button", name="Dostosuj")
        self.analytics_cookie_switch = page.get_by_role("switch", name="Cookies analityczne").locator("span").first
        self.analytics_cookie_state = page.locator("div:nth-child(2) > .cookie-policy-switch > .cookie-policy-toggle-button")
        self.accept_selected_cookies_button = page.get_by_role("button", name="Zaakceptuj zaznaczone")
        self.marketing_cookie_state = page.locator("div:nth-child(3) > .cookie-policy-switch > .cookie-policy-toggle-button")

    def goto(self) -> "HomePage":
        """Navigate to page."""
        self.page.goto(ING_HOME_PAGE)
        return self
    
    def click_adjust_cookies(self) -> "HomePage":
        """Clicks button that allows to select which cookies are allowed."""
        self.adjust_cookies_button.click()
        return self
    
    def click_analytics_cookies(self) -> "HomePage":
        """Click switch that turns analytics cookies on/off."""
        self.analytics_cookie_switch.click()
        return self
    
    def click_accept_selected(self) -> "HomePage":
        """Clicks button that accepts currently selected cookies."""
        self.accept_selected_cookies_button.click()
        return self
    
    def get_gdpr_cookie_value(self) -> str:
        """Get value of the GDPR cookie that indicates which cookies were enabled."""
        cookies = self.page.context.cookies()
        return ''.join([cookie['value'] for cookie in cookies if cookie["name"] == 'cookiePolicyGDPR'])
