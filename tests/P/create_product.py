import os
import asyncio
from playwright.async_api import async_playwright, Playwright, expect

URL = "https://uat-seller-center.amaze-x.com/auth/sign-in"

async def run(playwright: Playwright) -> None:
    # Tạo thư mục lưu video
    os.makedirs("video01", exist_ok=True)

    browser = await playwright.chromium.launch(headless=False)

    # Bật ghi video vào thư mục video01 (lưu khi context đóng)
    context = await browser.new_context(
        record_video_dir="videos",
        record_video_size={"width": 1280, "height": 720},
    )

    page = await context.new_page()

    try:
        await page.goto(URL)

        await page.locator("span").filter(has_text="ThaiLanTH").click()
        await page.get_by_text("United StatesEN").click()

        await page.get_by_role("textbox", name="Email/Phone Number/Username").click()
        await page.get_by_role("textbox", name="Email/Phone Number/Username").fill("Accountuat44")

        await page.get_by_role("textbox", name="Password").click()
        await page.get_by_role("textbox", name="Password").fill("xlNuHa031f0BIQL")

        await page.get_by_role("button", name="Sign In").click()

        await page.get_by_text("Create Products").click()

        # (Giữ nguyên locator gốc của bạn)
    

        await page.locator(
            'input[type="file"][accept*=".jpeg"], input[type="file"][accept*=".jpg"], input[type="file"][accept*=".png"]'
        ).set_input_files("./5783930.jpg")

        await page.get_by_role("textbox", name="* Product Name", exact=True).click()
        await page.get_by_role("textbox", name="* Product Name", exact=True).fill("Testing automation 1 ")

        await page.get_by_role("textbox", name="* Product Name -TH").click()
        await page.get_by_role("textbox", name="* Product Name -TH").fill("Testing automation")

        await page.get_by_role("textbox", name="Please set category").click()
        await page.get_by_role("menuitem", name="Fashion right").locator("div").first.click()
        await page.get_by_role("menuitem", name="Men Bags right", exact=True).locator("div").nth(1).click()
        await page.get_by_role("menuitem", name="Men's Sling Bag").locator("div").nth(1).click()
        await page.get_by_role("button", name="OK").click()

        await page.locator('[id="form-item-basicInfo.descriptionEn"]').get_by_role("textbox").fill(
            "Testing automation 1 Testing automation 1Testing automation 1Testing automation 1Testing automation 1Testing automation 1Testing automation 1 "
        )
        await page.locator('[id="form-item-basicInfo.descriptionTh"]').get_by_role("textbox").fill(
            "Testing automation 1 Testing automation 1Testing automation 1Testing automation 1Testing automation 1Testing automation 1Testing automation 1 "
        )

        await page.locator("#rc_select_1").click()
        await page.get_by_title("Aisikadan (อซิกาเด้น)").click()

        await page.locator('input[name="saleInfo.price"]').click()
        await page.locator('input[name="saleInfo.price"]').fill("0230")

        await page.locator("#stock").click()
        await page.locator("#stock").fill("033")

        await page.locator("#product-form-sale-info").click()

        await page.locator("#rc_select_2").click()
        await page.get_by_text("Phuong Nguyen").click()

        await page.locator('input[name="shippingInfo.weight"]').click()
        await page.locator('input[name="shippingInfo.weight"]').fill("12")

        await page.get_by_role("spinbutton", name="W (Integer)").click()
        await page.get_by_role("spinbutton", name="W (Integer)").fill("0223")

        await page.get_by_role("spinbutton", name="L (Integer)").click()
        await page.get_by_role("spinbutton", name="L (Integer)").fill("02233")

        await page.get_by_text("cm").nth(1).click()
        await page.get_by_text("cm").nth(1).click()

        await page.get_by_role("spinbutton", name="W (Integer)").click()
        await page.get_by_role("spinbutton", name="W (Integer)").fill("2")

        await page.get_by_role("spinbutton", name="L (Integer)").click()
        await page.get_by_role("spinbutton", name="L (Integer)").fill("22")

        await page.get_by_role("spinbutton", name="H (Integer)").click()
        await page.get_by_role("spinbutton", name="H (Integer)").fill("02")

        await page.get_by_role("button", name="Submit").click()

        # Chờ thông báo thành công
        await page.wait_for_url("**/portal/product/list?status=all", timeout=20000)

        print("✅ Product created successfully, returning to product list page.")
       

        # Thêm chút thời gian để video bắt kịp khung hình cuối (tùy chọn)
        await page.wait_for_timeout(500)

    finally:
        # Đóng context để video được ghi ra file trong thư mục video01
        await context.close()
        await browser.close()


async def main():
    async with async_playwright() as p:
        await run(p)

if __name__ == "__main__":
    asyncio.run(main())
