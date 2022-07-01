from App import app
import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.addHandler(AzureLogHandler(
    connection_string='InstrumentationKey=00000000-0000-0000-0000-000000000000')
)
    logger.warning("Sucesss")
   

    app.run(host='0.0.0.0', port=8000, debug=True)

