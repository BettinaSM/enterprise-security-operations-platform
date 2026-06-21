from parsers.baseline_engine import (

    save_baseline,

    compare_baseline

)


def create_baseline(name, content):

    save_baseline(

        name,

        content
    )


def validate_baseline(name, content):

    return compare_baseline(

        name,

        content
    )
