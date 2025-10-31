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
                Verify the login sucessfully
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