from playwright.sync_api import Page


def test_user_can_open_google(page: Page) -> None:
    page.context.tracing.start(screenshots=True, snapshots=True)

    page.goto("https://google.com")
    assert page.title() == "Google"

    page.context.tracing.stop(path="trace.zip")