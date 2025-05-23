from typing import Any, Mapping
from dify_plugin.interfaces.datasource import DatasourceProvider


class NotionDatasourceProvider(DatasourceProvider):
    def _validate_credentials(self, credentials: Mapping[str, Any]):
        """
        Validate the credentials for the Notion datasource provider.
        """
        pass
