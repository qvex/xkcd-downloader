import requests, os, bs4

url = 'http://xkcd.com'
try:
    os.makedirs('C:\\Users\\localhost\\Desktop\\xkcd\\', exist_ok=True)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

while not url.endswith('#'):

    # TODO : Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # TODO: Find the url of the page.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')

    # TODO: Download the image.
    print('Downloading image %s...' % (comicUrl))
    res = requests.get(comicUrl)
    res.raise_for_status()

    # TODO: Save the image to ./xkcd.
    imageFile = open(os.path.join('C:\\Users\\localhost\\Desktop\\xkcd\\', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(10000):
        imageFile.write(chunk)
    imageFile.close()

    # TODO: Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')
