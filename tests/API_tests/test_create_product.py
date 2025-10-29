from itertools import product
import pytest
import json
import time
import requests
from tests.API_tests.api_utils import create_product
from tests.API_tests.api_utils import get_product_list, get_product_by_id
from tests.API_tests.payloads import base_product_payload


@pytest.fixture
def product_payload():
    """Fixture trả về payload cơ bản"""
    return base_product_payload()

def test_create_product_and_verify_product(product_payload):
    product_name = "Product name test ne"
    product_payload["name"] = product_name

    # Step 1️⃣ - Tạo product
    create_resp = create_product(product_payload)

    # 🌟 ĐO TIME LƯỜNG TẠO SẢN PHẨM Ở ĐÂY
    creation_duration = create_resp.elapsed.total_seconds() 
    print(f"⏱️ Creation API Load Time: {creation_duration:.3f} seconds")


    assert create_resp.status_code in [200, 201], f"❌ Product creation failed: {create_resp.text}"
    created_data = create_resp.json().get("data", {})
    created_id = created_data.get("id")
    assert created_id, "❌ No product ID returned from create API"

    print(f"✅ Product created successfully: {product_name} (ID: {created_id})")

    # Step 2️⃣ - Polling verify product
    time.sleep(10)
    found = False

    start_time_polling = time.time() # BẮT ĐẦU ĐO TỔNG THỜI GIAN POLLING

    for i in range(10):
        time.sleep(3)
        get_resp = get_product_by_id(created_id)

        # 🌟 THÊM ĐO LƯỜNG TẢI TRÊN MỖI LẦN GET
        get_duration = get_resp.elapsed.total_seconds()
        print(f"   -> [Attempt {i+1}] GET Load Time: {get_duration:.3f}s")

        if get_resp.status_code == 200:
            data = get_resp.json().get("data", {})
            if data.get("id") == created_id:
                found = True
                end_time_polling = time.time() # KẾT THÚC ĐO TỔNG THỜI GIAN
                total_polling_duration = end_time_polling - start_time_polling

                print(f"✅ Product verified successfully in system (ID: {created_id})")
                print(f"⏱️ Total Verification Duration: {total_polling_duration:.3f} seconds")
                break

    assert found, f"❌ Product '{product_name}' (ID: {created_id}) not found after retries."

def test_create_product_missing_name(product_payload):
    product_payload.pop("name", None)
    response = create_product(product_payload)
    assert response.status_code == 400
    print("✅ Validation works for missing name")

def test_create_product_invalid_price(product_payload):
    product_payload["price"] = -5
    response = create_product(product_payload)
    assert response.status_code == 400
    print("✅ Validation works for invalid price")

def test_create_product_missing_category(product_payload):
    product_payload.pop("category_group_id", None)
    response = create_product(product_payload)
    assert response.status_code == 400
    print("✅ Validation works for missing category_group_id")

def test_create_product_no_image(product_payload):
    product_payload["image_url"] = []
    response = create_product(product_payload)
    assert response.status_code == 400
    print("✅ Validation works for missing image")

def test_create_product_zero_price(product_payload):
    product_payload["price"] = 0
    response = create_product(product_payload)
    if response.status_code in [200, 201]:
        print("✅ Product allowed with zero price")
    else:
        print("❌ Zero price rejected as expected")

def test_create_product_duplicate_name(product_payload):
    product_payload["name"] = "Product name test ne"  # giống case đầu tiên
    response = create_product(product_payload)
    if response.status_code == 409:
        print("✅ Duplicate product name rejected")
    else:
        print("⚠️ API allowed duplicate product name")
