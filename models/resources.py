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
    def list(self) -> pd.DataFrame:
        """
        Lists all available documents in the resource
        Returns:
            DataFrame[id, name, modified]
        """
        pass

    def get(self, i_id: str) -> Content|None:
        """
        Returns a Content object for the specified id
        """
        pass