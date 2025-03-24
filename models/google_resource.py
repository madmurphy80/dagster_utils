import pandas as pd

from models.resources import DuResource, ContentAccess, ContentType, Content


class GoogleResource(DuResource):
    api_key: str
    content_access: ContentAccess
    document_type: ContentType

    def list(self) -> pd.DataFrame:
        """
        TODO: Implement
        """
        pass

    def get(self, i_id: str) -> Content|None:
        """
        TODO: Implement
        """
        pass