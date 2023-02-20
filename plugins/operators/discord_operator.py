from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class DiscordOperator(BaseOperator):

    @apply_defaults
    def __init__(
            self,
            discord_api_key,
            discord_server_id,
            discord_channel_id,
            *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.discord_api_key = discord_api_key
        self.discord_server_id = discord_server_id
        self.discord_channel_id = discord_channel_id

    def execute(self, context):
        # Retrieve data from Discord using API
        # Store data in database or CSV file
        pass
