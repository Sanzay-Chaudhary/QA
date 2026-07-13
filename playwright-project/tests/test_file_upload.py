from playwright.sync_api import sync_playwright

def test_file_upload():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/upload")
        page.set_input_files("#file-upload",
            "testdata/sample.txt")
        page.click("#file-submit")
        upload_file = page.locator("#uploaded-files").inner_text()
        print("Uploaded file:", upload_file)
        page.screenshot(path= "screenshots/file_upload.png")
        assert upload_file == "sample.txt"
        wait_for_timeout = 5000
        browser.close()
