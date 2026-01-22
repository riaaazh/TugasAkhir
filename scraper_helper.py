# file ini kunci utama pada proses scraping

import os
import csv
import time
import re  # buat bersihin teks dari spasi berlebih
from datetime import datetime  # buat nentuin tanggal awal dan akhir scraping

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


# --- FUNGSI 1: Ekstraksi Data Tweet ---
def extract_tweets(driver, soup):
    """
    Ambil data tweet (teks, waktu, username) dari halaman X (Twitter).
    """
    tweet_elements = soup.find_all("div", {"data-testid": "tweetText"})
    extracted_data = []

    for element in tweet_elements:
        # Bersihin teks dari spasi dan newline berlebih
        tweet_text = re.sub(r'\s+', ' ', element.text)
        tweet_text = tweet_text.strip()

        tweet_timestamp = "N/A"
        tweet_username = "N/A"

        try:
            # Ambil waktu tweet
            time_tag = element.find_previous("time")
            if time_tag and "datetime" in time_tag.attrs:
                tweet_timestamp = time_tag["datetime"]
        except:
            pass

        try:
            # Ambil username dari tweet
            user_container = element.find_previous("div", {"data-testid": "User-Name"})
            if user_container:
                username_link = user_container.find("a", href=True)
                if username_link:
                    handle = username_link['href'].split('/')[-1]
                    if handle:
                        tweet_username = "@" + handle
        except:
            pass

        # Simpan data tweet jika teksnya cukup panjang
        if tweet_text and len(tweet_text) > 10:
            extracted_data.append({
                "timestamp": tweet_timestamp,
                "username": tweet_username,
                "text": tweet_text,
                "url_pencarian": driver.current_url
            })
    return extracted_data


# --- FUNGSI 2: Fungsi Utama Scraping ---
def scrape_year_data(year, driver, max_scrolls=1000):
    """
    Ambil data tweet DPR dari X (Twitter) untuk satu tahun penuh.
    """

    TAHUN_AWAL_STR = str(year)
    TANGGAL_AWAL = f"{TAHUN_AWAL_STR}-01-01"

    # Tentuin tanggal akhir (kalo tahun sekarang, ambil sampe hari ini)
    tahun_sekarang = datetime.now().year
    if int(year) == tahun_sekarang:
        TANGGAL_AKHIR = datetime.now().strftime("%Y-%m-%d")
        print(f"Tahun target ({year}) adalah tahun berjalan. Data akan diambil sampai {TANGGAL_AKHIR}.")
    else:
        TANGGAL_AKHIR = f"{TAHUN_AWAL_STR}-12-31"


    # --- Buat query pencarian ---
    # Query utama: tentang DPR RI
    target_query = "(%22DPR%20RI%22%20OR%20%22Dewan%20Perwakilan%20Rakyat%22%20OR%20%22anggota%20DPR%22%20OR%20%22wakil%20rakyat%22%20OR%20%22Komisi%20DPR%22%20OR%20%22Gedung%20DPR%22)"

    # Query tambahan: topik terkait DPR
    keywords_query = "(%22RUU%22%20OR%20%22undang-undang%22%20OR%20%22kebijakan%22%20OR%20%22pengesahan%22%20OR%20%22reses%22%20OR%20%22rapat%20paripurna%22%20OR%20%22aspirasi%20rakyat%22)"

    # Gabungin query utama dan tambahan #bentuk 
    query = f"{target_query}%20{keywords_query}%20since%3A{TANGGAL_AWAL}%20until%3A{TANGGAL_AKHIR}"


    # Target URL untuk scraping
    target_url = f"https://x.com/search?q={query}&src=typed_query&f=live"

    print(f"\n--- Memulai Scraping Tahun {year}. Target URL: {target_url} ---")
    driver.get(target_url)
    time.sleep(20) # tunggu halaman selesai load

    data_scraped_count = 0
    filename = f"aspirasi_dpr_{TAHUN_AWAL_STR}.csv"
    existing_texts = set()

    # Cek file lama, kalau ada ambil teksnya buat hindari duplikasi
    if os.path.isfile(filename):
        try:
            with open(filename, 'r', newline='', encoding='utf-8') as f_read:
                reader = csv.DictReader(f_read)
                for row in reader:
                    if "text" in row:
                        existing_texts.add(row["text"])
            print(f"File {filename} ditemukan. {len(existing_texts)} data sebelumnya dimuat untuk menghindari duplikasi.")
        except Exception as e:
            print(f"Error membaca file {filename}: {e}. Memulai sebagai file baru.")
            existing_texts = set()

    # Loop scroll buat ambil data baru
    for i in range(max_scrolls):
        print(f"Tahun {year} | Scroll ke-{i+1} | Data unik terkumpul: {data_scraped_count}")

        # Ambil HTML halaman dan parse pake BeautifulSoup
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Ekstrak data dari halaman
        new_tweets = extract_tweets(driver, soup)

        # Filter data yang belum pernah disimpan
        unique_new_tweets = []
        for t in new_tweets:
            if t["text"] not in existing_texts:
                unique_new_tweets.append(t)
                existing_texts.add(t["text"])

        # Simpan data baru ke file CSV
        if unique_new_tweets:
            # Cek apakah file baru (buat header)
            is_new_file = not os.path.isfile(filename) or os.path.getsize(filename) == 0

            with open(filename, 'a', newline='', encoding='utf-8') as f:
                fieldnames = ["timestamp", "username", "text", "url_pencarian"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)

                if is_new_file:
                    writer.writeheader() # tulis header cuma di file baru

                # tulis data baru
                writer.writerows(unique_new_tweets)
                data_scraped_count += len(unique_new_tweets)

        # Scroll ke bawah dan cek apakah masih ada konten baru
        last_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(20) # jeda buat nunggu data baru muncul

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            print(f"Menghentikan scraping tahun {year}. Tidak ada konten baru (dasar halaman tercapai).")
            break

    print(f"Scraping tahun {year} selesai. Total data unik baru terkumpul: {data_scraped_count}")


### # Query utama: tentang DPR RI
query = ['"DPR RI"',
         '"Dewan Perwakilan Rakyat"', 
         '"anggota DPR"', 
         '"wakil rakyat"', 
         '"Komisi DPR"', 
         '"Gedung DPR"',]
# %22 = '"'
# %20 = ' '
target_query0 = "(" + " OR ".join(query).replace(" ", "%20").replace('"', '%22') + ")"
print(target_query0)