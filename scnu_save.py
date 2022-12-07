import requests as re
from bs4 import BeautifulSoup as bs

LIMIT = 130
URL =f"https://www.scnu.ac.kr/SCNU/na/ntt/selectNttList.do?mi=1061&bbsId=1021"

def ext_something(html):
  #title = html.find("h2","jobTitle").find("a").find("span")["title"]
  title = html.find("a").string.strip()
  #company = html.find("span",{"class":"companyName"}).string
  href = html.find("a").attrs['href']
  link = f"https://www.scnu.ac.kr{href}"
  return {"title":title, "link": link}

def extract_indeed_pages():
  URL2 = f"{URL}&currPage={LIMIT}"
  result = re.get(URL2)
  soup = bs(result.text, "html.parser")
  pagination = soup.find("ul",{"class":"pagination"})
  links = pagination.find_all('a')
  pages=[]
  #2,-1
  for link in links[2:-1]:
    pages.append(int(link.string))
  max_page = pages[-1]
  return max_page

def extract_job(last_page):
  jobs =[]
  for page in range(1,last_page+1):
    print(f"Scrapping page {page}")
    result = re.get(f"{URL}&currPage={page}")
    soup = bs(result.text, "html.parser")
    results = soup.find_all("td", "ta_l")
    for result in results:
      job = ext_something(result)
      jobs.append(job)
  return jobs