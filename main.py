from loguru import logger # type: ignore
from sys import stderr

logger.add(
                sink=stderr,
                format="{time} <r>{level}</r> <g>{message}</g> {file}",
                level="INFO"
            )

logger.add(
                "main_logs.log",
                format="{time} {level} {message} {file}",
                level="CRITICAL"
            )

def soma(x, y):
    try:
        soma = x + y
        logger.info(f"Valores corretos {soma}")
        return x + y
    except:
        logger.critical("Valores incorretos!")

soma(2,3)
soma(2,"3")