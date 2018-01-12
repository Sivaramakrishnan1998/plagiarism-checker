raw = get("https://www.google.com/search?q=%s"%(text),headers = headers,verify=False).text
    page = fromstring(raw)
    for result in page.cssselect(".r a"):
        url = result.get("href")
        if url.startswith("/url?"):
            url = parse_qs(urlparse(url).query)['q']
        print(url[0])

        urllist.append(url[0].strip('https://'))
    soup = BeautifulSoup(raw, "lxml")

    for s in soup.findAll('span', {'class': 'st'}):
        print(s.text)
        abstractlist.append(s.text)
    list3 = list(zip(urllist,abstractlist))
    result = dataextract(urllist,text)
    print(list3)
    print('\n\n\n\nscrapped from google')
