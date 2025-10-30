import asyncio
import os
import re
from pathlib import Path
from playwright.async_api import async_playwright, TimeoutError as PWTimeoutError

# === CẤU HÌNH CƠ BẢN ===
HEADLESS = False
SLOW_MO = 0  # ms (tăng nếu muốn xem chậm)
VIDEO_DIR = Path("videos")          # thư mục lưu video
VIDEO_SIZE = {"width": 1280, "height": 720}  # kích thước video
UPLOAD_FILE = Path(r"massupload_basic_product_template (17).xlsx")  # đổi sang đường dẫn thật nếu cần

async def main():
    # Đảm bảo thư mục video tồn tại
    VIDEO_DIR.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=HEADLESS, slow_mo=SLOW_MO)

        # record_video được bật ở mức context => mỗi page sẽ có 1 file .webm
        context = await browser.new_context(
            record_video_dir=str(VIDEO_DIR),
            record_video_size=VIDEO_SIZE,
            viewport={"width": 1366, "height": 768},
        )

        page = await context.new_page()

        try:
            # === LOGIN ===
            await page.goto("https://predev-seller-center.amaze-x.com/auth/sign-in")
            await page.locator("span").filter(has_text="ThaiLanTH").click()
            await page.get_by_text("United StatesEN").click()
            await page.get_by_role("textbox", name="Email/Phone Number/Username").fill("Adgjl123")
            await page.get_by_role("textbox", name="Password").fill("Adgjl123")
            await page.get_by_role("button", name="Sign In").click()
            await page.wait_for_load_state("networkidle")

            # === OPEN MASS UPLOAD PAGE ===
            await page.get_by_text(re.compile(r"^My Products")).click()
            await page.get_by_role("button", name="Batch Update").click()

            async with page.expect_popup() as popup_info:
                await page.get_by_role("link", name="Mass Upload Product").click()
            page1 = await popup_info.value
            await page1.wait_for_load_state("domcontentloaded")

            # === UPLOAD FILE ===
            await page1.get_by_role("tab", name="Upload File").click()

            # Nếu file ở cùng thư mục script, chuyển sang absolute path để chắc chắn
            file_path = str(UPLOAD_FILE.resolve())
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Không tìm thấy file upload: {file_path}")

            async with page1.expect_file_chooser() as fc_info:
                await page1.get_by_role("button", name="Select File", exact=True).click()
            file_chooser = await fc_info.value
            await file_chooser.set_files(file_path)

            # Nhấn Upload
            await page1.get_by_role("button", name=re.compile(r"^Upload(s)?$", re.I)).click()

            # === LẤY POPUP THÔNG BÁO ===
            try:
                toast = page1.locator('[role="alert"], .ant-notification-notice').first
                await toast.wait_for(state="visible", timeout=10_000)
                msg = (await toast.inner_text()).strip()

                print("\n==========================")
                print("📢 POPUP MESSAGE:")
                print(msg)
                print("==========================")

                if re.search(r"success", msg, re.I):
                    print("✅ RESULT: PASS — File uploaded successfully.")
                elif re.search(r"only xlsx|csv", msg, re.I):
                    print("❌ RESULT: FAIL — Wrong file type.")
                else:
                    print("⚠️ RESULT: UNKNOWN — Popup message không khớp điều kiện.")
            except PWTimeoutError:
                print("❌ FAIL — Không thấy popup thông báo trong 10 giây.")

        finally:
            # Đóng page trước để đảm bảo video được flush
            try:
                await page.close()
            except Exception:
                pass

            # Lấy đường dẫn video của page (sau khi page đã đóng)
            try:
                video_path = await page.video.path()  # type: ignore[attr-defined]
                print(f"\n🎬 Video đã lưu: {video_path}")
            except Exception as e:
                print(f"\n⚠️ Không lấy được đường dẫn video: {e}")

            await context.close()
            await browser.close()
            print("\n🎯 DONE. Browser closed.")

if __name__ == "__main__":
    asyncio.run(main())
