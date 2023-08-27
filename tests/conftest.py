import pytest
from task_flows.database.core import create_missing_tables


@pytest.fixture
def tables():
    try:
        create_missing_tables()
    except SystemExit:
        # command line tool will exit with exit(0)
        pass
