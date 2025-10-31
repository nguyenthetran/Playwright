from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)
    context = browser.new_context(record_video_dir="videos/")
    context.tracing.start(screenshots=True, snapshots=True)
    page = context.new_page()

    print("🧭 Navigating to sign-in page")
    page = context.new_page()
    page.goto("https://uat-seller-center.amaze-x.com/auth/sign-in")
    page.get_by_text("TH", exact=True).click()
    page.get_by_text("EN", exact=True).click()
    page.get_by_role("textbox", name="Email/Phone Number/Username").click()
    page.get_by_role("textbox", name="Email/Phone Number/Username").fill("Phuongtest123")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("oTSDDMsdl3A1eKv")
    page.get_by_role("button", name="Sign In").click()

    # ---------------------
    context.close()
    browser.close()
