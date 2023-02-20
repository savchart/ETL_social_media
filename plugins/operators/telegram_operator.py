import logging
from airflow.models import BaseOperator
from airflow.providers.telegram.hooks.telegram import TelegramHook
from airflow.utils.decorators import apply_defaults


class TelegramOperator(BaseOperator):
    """
    Operator to extract data from Telegram API.

    :param telegram_conn_id: The connection ID to use when fetching Telegram API credentials
    :type telegram_conn_id: str
    :param telegram_method: The Telegram API method to use
    :type telegram_method: str
    :param telegram_method_args: The arguments to the Telegram API method
    :type telegram_method_args: dict
    :param output_file_path: The path to the output file where data will be written
    :type output_file_path: str
    """

    @apply_defaults
    def __init__(self,
                 telegram_conn_id,
                 telegram_method,
                 telegram_method_args,
                 output_file_path,
                 *args, **kwargs):
        super(TelegramOperator, self).__init__(*args, **kwargs)
        self.telegram_conn_id = telegram_conn_id
        self.telegram_method = telegram_method
        self.telegram_method_args = telegram_method_args
        self.output_file_path = output_file_path

    def execute(self, context):
        logging.info("Executing TelegramOperator")

        telegram_hook = TelegramHook(telegram_conn_id=self.telegram_conn_id)
        response = telegram_hook.run_method(self.telegram_method, self.telegram_method_args)

        with open(self.output_file_path, "w") as file:
            file.write(response)
