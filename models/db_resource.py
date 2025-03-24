import pandas as pd
from sqlalchemy import Engine, text

from models.resources import DuResource, Content


class DbResource(DuResource):
    engine: Engine # SqlAlchemy engine to connect to the DB
    list_query: text # SQL query that returns the columns id, name and modified
    get_query: text  # SQL query that returns columns matching the Content dataclass, and has an :id parameter

    def list(self) -> pd.DataFrame:
        with self.engine.begin() as con:
            return pd.read_sql(self.list_query, con)

    def get(self, i_id: str) -> Content|None:
        with self.engine.begin() as con:
            r = con.execute(self.get_query.bindparams(i_id)).first()
            if r:
                return Content(r.source_id, r.type, r.created, r.modified, r.access, r.name, r.content)