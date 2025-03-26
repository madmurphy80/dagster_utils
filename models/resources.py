from dataclasses import dataclass
from datetime import datetime

import dagster as dg
import pandas as pd

ContentType: str
ContentAccess: str

@dataclass
class Content:
    source_id: str
    type: ContentType
    created: datetime
    modified: datetime
    access: ContentAccess
    name: str
    content: str

class DuResource(dg.ConfigurableResource):
    def get_list(self) -> pd.DataFrame:
        """
        Lists all available documents in the resource
        Returns:
            DataFrame[source_id, name, modified]
        """
        pass

    def get(self, i_source_id: str) -> Content|None:
        """
        Returns a Content object for the specified id
        """
        pass

    def get_all(self, i_source_ids: list[str]) -> pd.DataFrame:
        """
        Returns:
            DataFrame[source_id, type, content, created, modified, access, name]
        """
        pass