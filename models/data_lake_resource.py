import pandas as pd

from models.db_resource import DbResource
from models.resources import Content


class DataLakeResource(DbResource):
    def list(self) -> pd.DataFrame:
        """
        Lists all available documents in the resource
        Returns:
            DataFrame[id, name, modified]
        """
        pass

    def get(self, i_id: str) -> Content | None:
        """
        Returns a Content object for the specified id
        """
        pass