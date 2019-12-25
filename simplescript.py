"""Example of a very basic script"""

import logging


logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s",
                    level=logging.INFO)
logging.info("simplescript.py is running")
