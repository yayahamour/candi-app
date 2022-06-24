from App import app
import sentry_sdk
import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.addHandler(AzureLogHandler(
    connection_string='InstrumentationKey=00000000-0000-0000-0000-000000000000')
)
    logger.warning("Sucescs")
    sentry_sdk.init(
        dsn="https://432bbda901094e48b34d4c6a51c6a28b@o1298037.ingest.sentry.io/6527720",

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0
    )

    app.run(host='0.0.0.0', port=8000, debug=True)

