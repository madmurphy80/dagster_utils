import pandas as pd
from sqlalchemy import Engine, text, bindparam

from models.resources import DuResource, Content


class DbResource(DuResource):
    engine_type: str # SqlAlchemy engine to connect to the DB
    list_query: str # SQL query that returns the columns id, name and modified
    get_query: str  # SQL query that returns columns matching the Content dataclass, and has an :id parameter
    get_all_query: str # SQL query that returns columns matching the Content dataclass, and has an :id parameter
    def get_list(self) -> pd.DataFrame:
        with get_engine(self.engine_type).begin() as con:
            return pd.read_sql(text(self.list_query), con)

    def get(self, i_id: str) -> Content|None:
        with get_engine(self.engine_type).begin() as con:
            r = con.execute(text(self.get_query).bindparams(source_id=i_id)).first()
            if r:
                return Content(r.source_id, r.type, r.created, r.modified, r.access, r.name, r.content)

    def get_all(self, i_source_ids: list[str]) -> pd.DataFrame:
        with get_engine(self.engine_type).begin() as con:
            df = pd.read_sql(text(self.get_all_query).bindparams(bindparam('source_ids', value=i_source_ids, expanding=True)),
                             con=con)
            return df