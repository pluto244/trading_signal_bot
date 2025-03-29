import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path

def setup_logger(name: str = 'trading_bot') -> logging.Logger:
    """
    Настройка логгера с ротацией файлов
    
    Параметры:
        name: имя логгера (по умолчанию 'trading_bot')
    
    Возвращает:
        Настроенный экземпляр логгера
    """
    log_dir = Path('logs')
    log_dir.mkdir(exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    file_handler = RotatingFileHandler(
        filename=log_dir / 'trading_bot.log',
        maxBytes=500 * 1024 * 1024,  # 500 МБ
        backupCount=3,
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

logger = setup_logger()