import asyncio

from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext, BrowserContextConfig
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from pydantic import SecretStr
import os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Get the API key from the environment
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash', api_key=SecretStr(os.getenv('GEMINI_API_KEY'))) # type: ignore

# Create BrowserConfig of Browser Use provided
browser_config = BrowserConfig(
    headless=False,
    disable_security=True
)

# Create browser instance with the BrowserConfig
browser = Browser(config=browser_config)

# Ensure project_root is a string
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
recording_path = os.path.join(project_root, 'exports', 'recordings')
trace_path = os.path.join(project_root, 'exports', 'traces')

# Create the directory if it does not exist
if not os.path.exists(recording_path):
    os.makedirs(recording_path)
if not os.path.exists(trace_path):
    os.makedirs(trace_path)

# Create BrowserContextConfig of Browser Use provided
browser_context_config = BrowserContextConfig(
    wait_for_network_idle_page_load_time=3.0,
    browser_window_size={'width': 1600, 'height': 900}, # type: ignore
    locale='vi-VN',
    highlight_elements=True,
    viewport_expansion=-1,
    save_recording_path=os.path.join(project_root, 'exports', 'recordings'),
    trace_path=os.path.join(project_root, 'exports', 'traces')
)

# Create browser context with the BrowserContextConfig
browser_context = BrowserContext(
    browser=browser,
    config=browser_context_config
)

# Create agent with the model and browser context
agent = Agent( task=''' 
                Go to https://uat-seller-center.amaze-x.com/auth/sign-in 
                Click the language dropdown icon showing 'TH'. 
                Click the 'EN' option. 
                Login with username and password: 'qc_tester' and 'Test@1234' 
                Click the 'Sign In' button. 
                Wait for the 'Welcome to Amaze Seller Center' text to appear.
                Click the gear icon (Settings) immediately to the right of the search box.
                Wait for the 'Use Media Center' toggle switch to be visible.
                Click the toggle switch next to 'Use Media Center' to turn it ON.
                Verify that the toggle switch next to 'Use Media Center' is ON.
                Wait for 1 seconds.
                Click the close icon (X) to dismiss the settings panel.
                Click Create Products.
                Click the 'Add Image (0/9)' button.
                Click the 'From Media Center' button.
                Await for the "Upload from Media Center" text to apppear.
                Search the 'Amaze.png' on 'Name' field.
                Click the 'Apply' button.
                Click the checkbox above the image named 'Amaze.png'.
                Click the 'Confirm' button.
                Type 'Test auto with Playwright' into the 'Product Name' input field.
                Type 'Test auto with Playwright' into the 'Product Name -TH' input field.
                Click the "Category" field.
                Await for the "Edit Category" text to apppear.
                Click the 'Fashion' category item in the first column.
                Click the 'Watches' category item in the second column.
                Click the 'Men Watches' category item in the third column.
                Click the 'OK' button to confirm the selection.
                Scroll down the panel containing the 'Product Description -TH' fields until the bottom is visible.
                Type 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.' into the 'Product Description' input field.
                Type 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.' into the 'Product Description -TH' input field.
                Scroll down the page until the 'Specification' field is visible.
                Click the 'Brand' input field.
                Click the 'Alba (อัลบา)' brand option.
                Click the 'Watch style' input field.
                Click the 'work' Watch style option.
                Scroll down the page until the 'Sales information' field is visible.
                Type '10' into the 'Original Price' input field.
                Type '10' into the 'Stock' input field.
                Click the "Warehouse" field.
                Click 'test' Warehouse option.
                Scroll down the page until the 'Shipping' field is visible.
                Type '50' into the 'Weight' input field.
                Type '20' into the 'W (Integer)' parcel size field.
                Type '30' into the 'L (Integer)' parcel size field.
                Type '15' into the 'H (Integer)' parcel size field.
                Click 'Submit' button.
                Await create product successfully.
            ''',
    llm=llm,
    browser_context=browser_context
)


async def main():
    await agent.run()

    # Close the browser context and browser
    await browser_context.close()
    await browser.close()


asyncio.run(main())