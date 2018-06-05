import logging
logging.basicConfig(level=logging.DEBUG,
	format="%(asctime)s-->>%(levelname)s==>%(message)s",
	filename="log.txt")
logging.info("information message")
logging.error("ERROR message")
logging.debug("DEBUG message")
logging.warn("WARNING nessage")