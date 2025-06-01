import requests
from bs4 import BeautifulSoup
import urllib.robotparser
from urllib.parse import urljoin, urlparse
import time
import random
import json
from datetime import datetime
import sqlite3
import csv
import os
from concurrent.futures import ThreadPoolExecutor
import logging
from fake_useragent import UserAgent
import tldextract

# ethical scrapper foundation 

class EthicalScraper:
    def __init__(self, base_url, max_pages=100, delay=1, output_dir='scraped_data'):
        self.base_url = base_url
        self.max_pages = max_pages
        self.delay = delay
        self.output_dir = output_dir
        self.visited_urls = set()
        self.domain = tldextract.extract(base_url).registered_domain
        self.robots_parser = urllib.robotparser.RobotParser()
        self.robots_url = urljoin(base_url, '/robots.txt')
        self.user_agent = UserAgent().random
        self.session = requests.Session()
        self.setup_logging()
        self.setup_storage()
        
    def setup_logging(self):
        logging.basicConfig(
            filename='scraper.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
    def setup_storage(self):
        os.makedirs(self.output_dir, exist_ok=True)
        self.db_conn = sqlite3.connect(os.path.join(self.output_dir, 'scraped_data.db'))
        self.create_db_tables()
        
    def create_db_tables(self):
        cursor = self.db_conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT UNIQUE,
                title TEXT,
                content TEXT,
                links TEXT,
                timestamp DATETIME
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS resources (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                page_id INTEGER,
                resource_type TEXT,
                url TEXT,
                filename TEXT,
                FOREIGN KEY(page_id) REFERENCES pages(id)
            )
        ''')
        self.db_conn.commit()

# robots text compliance checker

def check_robots_txt(self):
    try:
        self.robots_parser.set_url(self.robots_url)
        self.robots_parser.read()
        return self.robots_parser.can_fetch(self.user_agent, self.base_url)
    except Exception as e:
        self.logger.warning(f"Could not parse robots.txt: {e}")
        return True  # Proceed with caution if robots.txt is unavailable

# advanced web page fetcher

def fetch_page(self, url):
    if not self.check_robots_txt():
        self.logger.info(f"Skipping {url} due to robots.txt restrictions")
        return None
        
    if url in self.visited_urls:
        return None
        
    try:
        headers = {
            'User-Agent': self.user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': self.base_url
        }
        
        time.sleep(self.delay * (0.5 + random.random()))  # Randomized delay
        
        response = self.session.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        if 'text/html' not in response.headers.get('Content-Type', ''):
            self.logger.info(f"Skipping non-HTML content at {url}")
            return None
            
        self.visited_urls.add(url)
        return response.text
        
    except requests.exceptions.RequestException as e:
        self.logger.error(f"Error fetching {url}: {e}")
        return None

# content extraction with beautiful soaps

def extract_content(self, html, url):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Remove unwanted elements
    for element in soup(['script', 'style', 'nav', 'footer', 'iframe']):
        element.decompose()
        
    data = {
        'url': url,
        'title': self.get_title(soup),
        'content': self.get_main_content(soup),
        'links': self.get_links(soup, url),
        'metadata': self.get_metadata(soup),
        'resources': self.extract_resources(soup, url)
    }
    
    return data
    
def get_title(self, soup):
    title = soup.find('title')
    return title.get_text().strip() if title else ''
    
def get_main_content(self, soup):
    # Try to find the main content using common semantic tags
    main_content = soup.find(['article', 'main']) or soup.find('div', class_=lambda x: x and 'content' in x.lower())
    if not main_content:
        # Fallback to body if no main content identified
        main_content = soup.find('body') or soup
        
    text = ' '.join(main_content.stripped_strings)
    return text
    
def get_links(self, soup, base_url):
    links = set()
    for link in soup.find_all('a', href=True):
        absolute_url = urljoin(base_url, link['href'])
        parsed_url = urlparse(absolute_url)
        if parsed_url.netloc.endswith(self.domain):  # Stay within same domain
            links.add(absolute_url)
    return list(links)
    
def get_metadata(self, soup):
    metadata = {}
    # Extract meta tags
    for meta in soup.find_all('meta'):
        if meta.get('name'):
            metadata[meta['name']] = meta.get('content', '')
        elif meta.get('property'):
            metadata[meta['property']] = meta.get('content', '')
            
    # Extract other useful metadata
    metadata['language'] = soup.find('html').get('lang', '')
    return metadata
    
def extract_resources(self, soup, base_url):
    resources = []
    # Images
    for img in soup.find_all('img', src=True):
        resources.append({
            'type': 'image',
            'url': urljoin(base_url, img['src']),
            'alt': img.get('alt', '')
        })
        
    # PDFs and documents
    for link in soup.find_all('a', href=True):
        href = link['href'].lower()
        if href.endswith(('.pdf', '.doc', '.docx', '.ppt', '.pptx')):
            resources.append({
                'type': 'document',
                'url': urljoin(base_url, link['href']),
                'text': link.get_text().strip()
            })
            
    # Videos
    for video in soup.find_all(['video', 'iframe']):
        src = video.get('src') or video.get('data-src')
        if src:
            resources.append({
                'type': 'video',
                'url': urljoin(base_url, src),
                'embed': True
            })
            
    return resources

# storage system 
def store_data(self, data):
    try:
        cursor = self.db_conn.cursor()
        
        # Store page data
        cursor.execute('''
            INSERT INTO pages (url, title, content, links, timestamp)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            data['url'],
            data['title'],
            data['content'],
            json.dumps(data['links']),
            datetime.now().isoformat()
        ))
        page_id = cursor.lastrowid
        
        # Store resources
        for resource in data['resources']:
            cursor.execute('''
                INSERT INTO resources (page_id, resource_type, url)
                VALUES (?, ?, ?)
            ''', (
                page_id,
                resource['type'],
                resource['url']
            ))
            
        self.db_conn.commit()
        
        # Also save as JSON for easy access
        json_path = os.path.join(self.output_dir, 'pages', f"{page_id}.json")
        os.makedirs(os.path.dirname(json_path), exist_ok=True)
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    except Exception as e:
        self.logger.error(f"Error storing data: {e}")
        self.db_conn.rollback()


# crawler engine 

def crawl(self, start_url=None):
    if not start_url:
        start_url = self.base_url
        
    if not self.check_robots_txt():
        self.logger.warning(f"Cannot crawl {self.base_url} due to robots.txt restrictions")
        return
        
    queue = [start_url]
    crawled_pages = 0
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        while queue and crawled_pages < self.max_pages:
            current_url = queue.pop(0)
            
            self.logger.info(f"Crawling: {current_url}")
            html = self.fetch_page(current_url)
            if not html:
                continue
                
            data = self.extract_content(html, current_url)
            self.store_data(data)
            crawled_pages += 1
            
            # Add new links to queue
            for link in data['links']:
                if link not in self.visited_urls and link not in queue:
                    queue.append(link)
                    
            # Submit resource downloads to thread pool
            for resource in data['resources']:
                executor.submit(self.download_resource, resource, crawled_pages)
                
def download_resource(self, resource, page_id):
    try:
        resource_dir = os.path.join(self.output_dir, 'resources', resource['type'])
        os.makedirs(resource_dir, exist_ok=True)
        
        filename = os.path.basename(urlparse(resource['url']).path)
        if not filename:
            filename = f"resource_{int(time.time())}"
            
        filepath = os.path.join(resource_dir, filename)
        
        headers = {'User-Agent': self.user_agent}
        response = self.session.get(resource['url'], headers=headers, stream=True, timeout=10)
        response.raise_for_status()
        
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                
        self.logger.info(f"Downloaded {resource['type']}: {filename}")
        
        # Update database with filename
        cursor = self.db_conn.cursor()
        cursor.execute('''
            UPDATE resources SET filename = ? 
            WHERE page_id = ? AND url = ?
        ''', (filename, page_id, resource['url']))
        self.db_conn.commit()
        
    except Exception as e:
        self.logger.error(f"Error downloading resource {resource['url']}: {e}")

# analysis and reporting 

def generate_report(self):
    report = {
        'domain': self.domain,
        'total_pages': len(self.visited_urls),
        'start_time': min(self.visited_urls.values()) if self.visited_urls else None,
        'end_time': datetime.now().isoformat(),
        'stats_by_type': self.get_resource_stats()
    }
    
    report_path = os.path.join(self.output_dir, 'report.json')
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)
        
    return report
    
def get_resource_stats(self):
    cursor = self.db_conn.cursor()
    cursor.execute('''
        SELECT resource_type, COUNT(*) as count 
        FROM resources 
        GROUP BY resource_type
    ''')
    rows = cursor.fetchall()
    return {row[0]: row[1] for row in rows}

# usage example 

if __name__ == "__main__":
    # Example usage for educational purposes
    university_url = "https://ocw.mit.edu"  # MIT OpenCourseWare as an example
    
    scraper = EthicalScraper(
        base_url=university_url,
        max_pages=50,  # Limit for demonstration
        delay=2,       # Be polite with requests
        output_dir='mit_ocw_data'
    )
    
    try:
        scraper.crawl()
        report = scraper.generate_report()
        print(f"Scraping complete. Report:\n{json.dumps(report, indent=2)}")
    except KeyboardInterrupt:
        print("\nScraping interrupted by user. Saving progress...")
    finally:
        scraper.db_conn.close()