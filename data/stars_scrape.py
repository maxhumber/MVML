from gazpacho import get, Soup

def make_soup(url):
    html = get(url)
    soup = Soup(html)
    return soup

def get_next_url(soup):
    buttons = soup.find(
        "div",
        mode="all",
        attrs={"class": "BtnGroup", "data-test-selector": "pagination"},
    )
    button = buttons[-1].find("a", mode="all")[-1]
    if button.text == "Next":
        return button.attrs["href"]
    return None

def scrape_users(soup):
    users = soup.find("div", {"class": "follower-list-align-top d-inline-block ml-3"})
    users = [u.find("a", {"data-hovercard-type": "user"}) for u in users]
    users = [u.attrs["href"][1:] for u in users]
    return users



if __name__ == "__main__":

    # user list
    url = "https://github.com/maxhumber/gazpacho/stargazers"
    soup = make_soup(url)
    url = get_next_url(soup)
    users = scrape_users(soup)

    # one user
    url = 'https://github.com/garrrychan?page=2&tab=stars'
    soup = make_soup(url)
    divs = soup.find('div', {'class': 'd-inline-block mb-1'})
    repos = [d.find('a').attrs['href'] for d in divs]
