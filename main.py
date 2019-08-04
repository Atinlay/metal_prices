import pandas as pd
from datetime import datetime

from config import Configuration
from helpers import get_metals_and_prices_from_table, soup_url, get_database_engine

if __name__ == '__main__':
    config = Configuration()
    soup = soup_url(config.url)
    metal_table = soup.find("div", {"class": "c_mp_price_table"})
    metals, prices = get_metals_and_prices_from_table(metal_table)

    metal_and_prices_df = pd.DataFrame()
    metal_and_prices_df["metal"] = metals
    metal_and_prices_df["price"] = prices
    metal_and_prices_df["date"] = datetime.today().strftime("%Y-%m-%d")

    connection = get_database_engine()

    metal_and_prices_df.to_sql(name=config.sql_table,
                               con=connection,
                               schema="projects",
                               if_exists="append",
                               index=False)