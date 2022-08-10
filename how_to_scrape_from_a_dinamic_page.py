url = ''
    browser = start_chrome(url, headless=True)
    soup= BeautifulSoup(browser.page_source, 'html.parser')
    
    quotes = soup.find_all('div', {'class':'quote'})
