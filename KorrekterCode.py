import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests

# Pfad zum ChromeDriver (passen Sie diesen Pfad an Ihre Systemkonfiguration an)
chromedriver_path = '/Users/kamillalauter/Downloads/chromedriver_mac64 (1)/chromedriver'

# Konfigurieren des Chrome-Browsers für Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialisieren des ChromeDriver-Dienstes
webdriver_service = Service(chromedriver_path)
try:
    browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)
except Exception as e:
    print(f"Error initializing ChromeDriver: {e}")
    exit()

# Funktion zum Extrahieren von Daten aus BeautifulSoup-Objekt
def extract_data(soup, selector):
    elements = soup.select(selector)
    return [element.text.strip() for element in elements]

# Funktion zum Extrahieren von Kontaktdetails, Adresse und Startdatum von der zweiten Seite
def extract_details_from_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Jobtitel extrahieren
    job_title_element = soup.find('h1', class_='title title--section title--left')
    job_title = job_title_element.text.strip() if job_title_element else 'Kein Jobtitel gefunden'

    # Adresse extrahieren
    address_section = soup.find('div', class_='address')
    address_info = address_section.get_text(strip=True) if address_section else 'Keine Adresse gefunden'

    # Kontaktperson extrahieren
    contact_section = soup.find('div', class_='job-posting-contact-person__name')
    contact_info = contact_section.text.strip() if contact_section else 'Keine Kontaktperson gefunden'

    # Startdatum extrahieren
    start_date_label = soup.find('span', class_='label', text='Frühester Beginn')
    start_date_info = start_date_label.find_next('span', class_='value').text.strip() if start_date_label else 'Kein Startdatum gefunden'

    return job_title, address_info, contact_info, start_date_info

# Funktion zum Extrahieren der freien Plätze
def extract_vacancies(soup):
    vacancies = []
    fact_items = soup.select('li.job-posting-cluster-cards__list-item')
    for item in fact_items:
        if item.select_one('i.icon-users'):
            value = item.select_one('span.job-posting-cluster-cards__fact-value').text.strip()
            vacancies.append(value)
    return vacancies

# Funktion zum Speichern der Daten in einer CSV-Datei
def save_to_csv(data, filename, header):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Header der CSV-Datei
        writer.writerows(data)

# Liste zum Speichern der Jobdaten
job_data = []

# Schleife über Seiten 1 bis 2 (für Testzwecke, später auf 101 erhöhen)
for page_num in range(1, 2):
    # URL für jede Seite
    url = f"https://www.ausbildung.de/suche/?form_main_search[what]=&form_main_search[where]=Hannover&t_search_type=root&t_what=&t_where=&page={page_num}"
    browser.get(url)
    # Warten, bis die Seite vollständig geladen ist
    time.sleep(5)

    # Abrufen des HTML-Inhalts der Seite
    html_content = browser.page_source

    # Verwenden von BeautifulSoup, um die Jobtitel und Anzahl der Plätze zu extrahieren
    soup = BeautifulSoup(html_content, 'html.parser')

    job_titles = extract_data(soup, 'h3.job-posting-cluster-cards__title')

    # Für jede Stelle Kontaktdetails, Adresse und Startdatum extrahieren
    for i in range(len(job_titles)):
        job_title_element = soup.find_all('h3', class_='job-posting-cluster-cards__title')[i]
        job_url = job_title_element.find_parent('a')['href'] if job_title_element.find_parent('a') else None
        if job_url:
            full_job_url = f"https://www.ausbildung.de{job_url}"
            print(full_job_url)

            job_title, address, contact_person, start_date = extract_details_from_page(full_job_url)
            vacancies = extract_vacancies(soup)
            job_data.append([job_title, address, vacancies[i] if i < len(vacancies) else 'Keine Angabe', start_date, contact_person, full_job_url])

# Speichern der Jobdaten in einer CSV-Datei
save_to_csv(job_data, 'job_data.csv', ['Job Title', 'Address', 'Vacancies', 'Start Date', 'Contact Person', 'Link'])

print(f"{len(job_data)} job entries have been saved to job_data.csv")

# Browser schließen
browser.quit()
