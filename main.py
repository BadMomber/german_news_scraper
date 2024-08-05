import newspaper_scraper as nps

with nps.Spiegel(db_file='spiegel.db') as news:
    news.index_articles_by_date_range('2023-03-01', '2023-06-15')
    news.scrape_public_articles()
    news.nlp()

# with nps.Welt(db_file='welt.db') as news:
#     news.index_articles_by_date_range('2022-11-01', '2024-06-15')
#     news.scrape_public_articles()
#     news.nlp()

# with nps.Zeit(db_file='zeit.db') as news:
#     news.index_articles_by_date_range('2022-11-01', '2024-06-15')
#     news.scrape_public_articles()
#     news.nlp()
#
# with nps.Handelsblatt(db_file='handelsblatt.db') as news:
#     news.index_articles_by_date_range('2022-11-01', '2024-06-15')
#     news.scrape_public_articles()
#     news.nlp()