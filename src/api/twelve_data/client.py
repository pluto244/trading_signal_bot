import pandas as pd
from twelvedata import TDClient
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent.parent))

from utils.logger import logger
from config import TWELVEDATA_API_KEY



class TwelveDataClient:    
    def __init__(self):
        """
        Инициализация клиента.

        """
        self.api_key = TWELVEDATA_API_KEY
        if not self.api_key:
            raise ValueError("API key is required. Set TWELVEDATA_API_KEY in .env")
        
        self.td = TDClient(apikey=self.api_key)
        logger.info("TwelveData client initialized")

    def get_data(
        self,
        symbol: str = 'AAPL,',
        interval: str = "5min",
        output_size: int = 100,
        timezone: str = "America/New_York",
    ) -> pd.DataFrame:
        """
        Получение данных с возможностью добавления индикаторов.
        
        :param symbol: Тикер (например "AAPL")
        :param interval: Размер свечи ("1min", "5min", "1day" и т.д.)
        :param output_size: Количество свеч
        :param timezone: Часовой пояс
        :return: pd.DataFrame с данными
        """
        try:
            ts = self.td.time_series(
                symbol=symbol,
                interval=interval,
                outputsize=output_size,
                timezone=timezone
            ).with_ema(time_period=output_size*2).with_rsi(time_period=output_size*2).as_pandas()
            
            if ts.empty:
                logger.warning(f"No data returned for {symbol}")
                return ts

            return ts
            
        except Exception as e:
            logger.error(f"Failed to get data: {str(e)}")
            raise

if __name__=="__main__":
    client = TwelveDataClient()
    df = client.get_data()
    print(df)
