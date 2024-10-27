from loguru import logger # type: ignore

logger.debug("Um aviso para o Dev.")
logger.info("Aviso de algum processo importante.")
logger.warning("Aviso que algo pode falhar no futuro.")
logger.error("Ocorreu uma falha no sistema.")
logger.critical("Aplicação abortada!")
 