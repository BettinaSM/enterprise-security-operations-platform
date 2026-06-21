from parsers.cmdb_engine import (
    load_cmdb
)

def test_load_cmdb():

    assets = load_cmdb()

    assert isinstance(
        assets,
        list
    )
