import pandas as pd

from models.db_resource import DbResource
from models.resources import Content



class DataLakeResource(DbResource):
    resource_type: str

    list_query: str = """
        SELECT source_id, name, modified
        FROM data_lake
        WHERE type = :resource_type
    """

    get_query: str = """
        SELECT source_id, type, created, modified, access, name, content
        FROM data_lake
        WHERE id = :source_id
    """

    get_all_query: str = """
        SELECT source_id, type, created, modified, access, name, content
        FROM data_lake
        WHERE id IN :source_ids
    """

    def get_list(self) -> pd.DataFrame:
        with get_engine(self.engine_type).begin() as con:
            return pd.read_sql(text(self.list_query).bindparams(resource_type=self.resource_type), con)

    def update(self, i_df: pd.DataFrame) -> None:
        """
        Args:
            i_df: DataFrame[content, type, created, modified, access, source_id, name]
        """
        _SQL_QUERY = """
            DELETE FROM data_lake
            WHERE source_id = :source_id AND type = :type
        """
        i_df['content'] = i_df['content'].apply(json.dumps)
        indexes_to_delete = i_df[['source_id', 'type']].to_dict('records')
        with get_engine(self.engine_type).begin() as con:
            con.execute(text(_SQL_QUERY), indexes_to_delete)
            i_df.to_sql('data_lake', if_exists='append', con=con, index=False)

