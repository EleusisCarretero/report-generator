from bs4 import BeautifulSoup

def read_html(path:str):
    with open(path, "r", encoding="utf-8") as f:
        html_value = f.read()
    soup = BeautifulSoup(html_value, "html.parser")
    return soup

def define_teble(path:str, extension:str='.js'):
    soap = read_html(path)
    table = soap.find("table")
    headers = [th.get_text(strip=True) for th in table.find_all("th") if th.get_text(strip=True) != '']
    rows = []
    for tr in table.find_all("tr"):
       if tr.find_all("td"):
        file = tr.find_all("td")[0].get_text(strip=True).replace(extension, "")
        row_data = [td.get_text(strip=True) for td in tr.find_all("td")[1:] if 'pct' in td['class']]
        if row_data:
            rows.append({file:dict(zip(headers, row_data))})
    print(rows)
    return rows
      

define_teble("/home/eleusis/Documents/remote_repos/report-generator/src/jest/test_index.html")