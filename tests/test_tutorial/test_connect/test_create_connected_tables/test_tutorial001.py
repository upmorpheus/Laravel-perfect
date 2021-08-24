from typing import Any, Dict, List, Union
from unittest.mock import patch

from sqlalchemy import inspect
from sqlalchemy.engine.reflection import Inspector
from sqlmodel import create_engine
from sqlmodel.pool import StaticPool

from ....conftest import get_testing_print_function


def test_tutorial001(clear_sqlmodel):
    from docs_src.tutorial.connect.create_tables import tutorial001 as mod

    mod.sqlite_url = "sqlite://"
    mod.engine = create_engine(mod.sqlite_url)
    mod.main()
    insp: Inspector = inspect(mod.engine)
    assert insp.has_table(str(mod.Hero.__tablename__))
    assert insp.has_table(str(mod.Team.__tablename__))
