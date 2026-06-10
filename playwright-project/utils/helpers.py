import random

def generate_random_email():
    number = random.randint(1000, 9999)
    return f"test{number}@gmail.com"



# def print_current_url(page):
#     print("current url:", page.url)
def print_current_url(page):
    print(f"Current URL: {page.url}")


def take_screenshot(
    page,
    filename
):

    page.screenshot(
        path=f"screenshots/{filename}.png"
    )


from datetime import datetime

def current_timestamp():

    return datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )