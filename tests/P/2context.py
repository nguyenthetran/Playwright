# 2context.py  (async, chạy 2 cửa sổ)
import asyncio
from playwright.async_api import async_playwright, TimeoutError as PWTimeout

DATA = [
    {"username": "Phuongtest123",  "password": "oTSDDMsdl3A1eKv"},
    {"username": "Phuongtest1234", "password": "oTSDDMsdl3A1eKv."},  # user sai để thấy toast lỗi
]

# ---- helper: lấy thông điệp hiển thị trên UI (toast/alert/notification)
async def get_ui_message(page, timeout: int = 3000) -> str:
    selectors = [
        ".ant-notification-notice-message",  # Ant Design notification
        ".ant-message-notice-content",       # Ant Design message
        "[role='alert']",
        "div[class*='toast']",
        "div[class*='notification']",
        "text=Can't login with your information",  # thông điệp cụ thể bạn thấy
    ]
    # thử lần lượt, chờ nhanh
    for sel in selectors:
        try:
            el = await page.wait_for_selector(sel, timeout=timeout)
            if el:
                txt = await el.text_content()
                if txt and txt.strip():
                    return txt.strip()
        except Exception:
            pass
    # fallback: quét tất cả
    try:
        texts = await page.locator(", ".join(selectors)).all_text_contents()
        for t in texts:
            if t and t.strip():
                return t.strip()
    except Exception:
        pass
    return ""

# ---- flow chính cho mỗi cửa sổ
async def perform_flow(page, data):
    print(">>> Truy cập trang đăng nhập")
    try:
        await page.goto("https://predev-seller-center.amaze-x.com/auth/sign-in")
        # đổi ngôn ngữ nếu muốn:
        await page.get_by_text("TH", exact=True).click()
        await page.get_by_text("EN", exact=True).click()

        await page.get_by_role("textbox", name="Email/Phone Number/Username").fill(data["username"])
        await page.get_by_role("textbox", name="Password").fill(data["password"])
        await page.get_by_role("button", name="Sign In").click()

        # 🔍 Kiểm tra message UI (toast)
        ui_msg = await get_ui_message(page, timeout=2000)
        if ui_msg:
            lower_msg = ui_msg.lower()
            if any(k in lower_msg for k in ["success", "logged in", "login success"]):
                print(f"✅ PASS UI: {data['username']} -> {ui_msg}")
                return {"user": data["username"], "status": "ok", "message": ui_msg}

            # các từ khoá báo lỗi
            if any(k in lower_msg for k in ["can't", "fail", "error", "invalid", "wrong", "not", "unable"]):
                await page.screenshot(path=f"fail_ui_{data['username']}.png")
                print(f"❌ FAIL UI: {data['username']} -> {ui_msg}")
                return {"user": data["username"], "status": "fail_ui", "message": ui_msg}

        # 🔄 nếu không có toast → tiếp tục check dashboard
        await page.wait_for_load_state("networkidle")
        await page.wait_for_selector("text=Dashboard", timeout=15000)

        print(f"✅ PASS: {data['username']} đăng nhập thành công")
        return {"user": data["username"], "status": "ok", "message": "Logged in"}

    except PWTimeout:
        ui_msg = await get_ui_message(page, timeout=2000)
        await page.screenshot(path=f"fail_timeout_{data['username']}.png")
        msg = ui_msg or "Timeout — Có thể sai selector hoặc đăng nhập thất bại"
        print(f"❌ FAIL TIMEOUT: {data['username']} -> {msg}")
        return {"user": data["username"], "status": "timeout", "message": msg}

    except Exception as e:
        ui_msg = await get_ui_message(page, timeout=2000)
        await page.screenshot(path=f"fail_error_{data['username']}.png")
        msg = ui_msg or f"Exception: {e}"
        print(f"❌ FAIL EXC: {data['username']} -> {msg}")
        return {"user": data["username"], "status": "error", "message": msg}
# ---- runner
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        contexts, tasks = [], []

        for data in DATA:
            ctx = await browser.new_context()
            contexts.append(ctx)
            page = await ctx.new_page()
            tasks.append(perform_flow(page, data))

        results = await asyncio.gather(*tasks, return_exceptions=False)

        print("\n== Summary ==")
        for r in results:
            print(r)

        for c in contexts:
            await c.close()
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
