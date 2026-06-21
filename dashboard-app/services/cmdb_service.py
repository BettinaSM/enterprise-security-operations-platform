from parsers.cmdb_engine import (

    load_cmdb,

    search_asset

)


def get_all_assets():

    return load_cmdb()


def find_asset(keyword):

    return search_asset(keyword)
