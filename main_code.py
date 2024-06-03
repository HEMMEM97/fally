def trending_topics():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time
    import requests
    from webdriver_manager.chrome import ChromeDriverManager

    # List of proxies to choose from
    proxies_list = [
        '189.240.60.168:9090',
        '20.24.43.214:80'
        # Add more proxies here
    ]

    proxies_list = proxies_list[::-1]

    # Function to test if a proxy works
    def test_proxy(proxy):
        proxies = {
            'http': f'http://{proxy}',
            'https': f'http://{proxy}',
        }
        try:
            response = requests.get('https://httpbin.org/ip', proxies=proxies, timeout=10)
            if response.status_code == 200:
                return True
        except Exception as e:
            print(f"Proxy {proxy} failed: {e}")
        return False

    # Choose a working proxy randomly from the list
    working_proxy = None
    for proxy in proxies_list:
        if test_proxy(proxy):
            working_proxy = proxy
            break

    if not working_proxy:
        print("No working proxy found")
        exit(1)

    print(f"Using proxy: {working_proxy}")

    chrome_options = webdriver.ChromeOptions()
    '''chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--remote-debugging-port=9222")'''
    chrome_options.add_argument(f'--proxy-server={working_proxy}')
     
    
    # Initialize the WebDriver
    driver = webdriver.Chrome()

    # Wait object
    wait = WebDriverWait(driver, 20)  # Increased the wait time to 20 seconds
    try:
        
        # Open Twitter login page
        driver.get('https://twitter.com/login')
        print("yahuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
        
        time.sleep(8)  # Give some time for the login page to fully load
        print('yahan hu')
        # Find the username input field and enter the username
        username_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="text"]')))
        username_input.send_keys('TestLaksha15220')

        # Find the "Next" button and click it
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Next"]/..')))
        next_button.click()

        # Wait for the password input field to appear and enter the password
        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
        password_input.send_keys('patlamayadevam')

        # Submit the login form
        password_input.send_keys(Keys.RETURN)

        # Wait for the home page to fully load
        wait.until(EC.presence_of_element_located((By.XPATH, '//nav')))

        # Navigate to Twitter home page (if not redirected automatically)
        driver.get('https://twitter.com/home')
        time.sleep(10)  # Wait for the home page to fully load

        # Locate the "What’s Happening" section
        whats_happening_section = wait.until(EC.presence_of_element_located((By.XPATH, '//section[@aria-labelledby="accessible-list-0"]')))

        # Fetch the top 5 trending topics
        trending_topics = whats_happening_section.find_elements(By.XPATH, './/div[@data-testid="trend"]')[:5]

        L=[working_proxy]
        # Print the trending topics
        for index, topic in enumerate(trending_topics, start=1):
            topic_text = topic.text
            L.append(topic_text)
        print("main code - - ")
        print(L)
        return L

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the browser
        driver.quit()
