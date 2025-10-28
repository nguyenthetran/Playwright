def base_product_payload():
    return{
        "status": "reviewing",
        "name": "TestAPIwithPlaywright3",
        "name_th": "TestAPIwithPlaywright3",
        "description": "<p><b>Lorem Ipsum</b>&nbsp;is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p><p><br></p>",
        "description_th": "<p><b>Lorem Ipsum</b>&nbsp;is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p><p><br></p>",
        "image_url": [
            {
                "id": "a44a00e5-5d2d-4692-8cb7-d04480479807",
                "name": "a97b00d1-b2df-11f0-bd00-f21b952ab4a5-0.png",
                "url": "https://ms-resource.amaze-x.com/0caf140e-143f-4c2b-a262-dc3386e68ef9/image/a97b00d1-b2df-11f0-bd00-f21b952ab4a5-0.png",
                "type": "image"
            }
        ],
        "category_group_id": "3417a7f1-bd2d-4dc1-b6ed-c947e20f83db",
        "category_path": [
            "959ad173-2d78-42f1-8ab9-73e8aad420d7",
            "fa276e1e-0d17-4eec-a8c5-0faf4dbe8e29",
            "3417a7f1-bd2d-4dc1-b6ed-c947e20f83db"
        ],
        "brand_id": "3d754880-7120-480e-a8c9-e2ef7ee6fe16",
        "attributes": [],
        "inventory": [
            {
                "shop_address_id": "3e478aae-53f5-4085-af62-73e2100ee31f",
                "warehouse_name": "test",
                "stock": 10
            }
        ],
        "price": 10,
        "selling_price_start_time": "",
        "selling_price_end_time": "",
        "model_list": [],
        "tier_variations": [],
        "tier_variations_multi_lang": [],
        "whole_sale": [],
        "weight": 10,
        "parcel_size": {
            "width": 10,
            "length": 10,
            "height": 10
        },
        "shipping": [
            {
                "shop_shipping_method_id": "48d67aa3-1f8d-44c8-948d-87e60697cbc4",
                "enable": False,
                "shipping_fee": 0,
                "shipping_channel_id": "63389eae-b05f-48a1-a9dd-062395dfef4b",
                "shop_id": "0caf140e-143f-4c2b-a262-dc3386e68ef9",
                "shipping_channel": {
                    "id": "63389eae-b05f-48a1-a9dd-062395dfef4b",
                    "is_default": True,
                    "name": "Amaze Standard Delivery",
                    "seller_editable": False,
                    "code_name": "ali_express",
                    "shipping_fee_editable": False
                }
            },
            {
                "shop_shipping_method_id": "d1c4b207-09aa-447d-931f-32182a6e16a4",
                "enable": True,
                "shipping_fee": 0,
                "shipping_channel_id": "a95df682-5a30-4555-880b-323a68f73f75",
                "shop_id": "0caf140e-143f-4c2b-a262-dc3386e68ef9",
                "shipping_channel": {
                    "id": "a95df682-5a30-4555-880b-323a68f73f75",
                    "is_default": False,
                    "name": "Seller Own Fleet",
                    "seller_editable": True,
                    "code_name": "3p_own_fleet",
                    "shipping_fee_editable": True
                }
            }
        ],
        "pre_order": False,
        "pre_order_days": 0,
        "condition": "new",
        "parent_sku": "",
        "payment_configs": [
            {
                "shop_payment_channel_config_id": "a662459e-37c3-49a5-881b-bf481938af8d",
                "is_active": True
            }
        ],
        "installment_configuration": {
            "is_active": False
        },
        "update_flag": [
            "attributes",
            "variant",
            "variant_option"
        ]
    }