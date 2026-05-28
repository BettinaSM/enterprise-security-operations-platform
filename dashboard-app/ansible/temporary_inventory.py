from pathlib import Path

TEMP_DIR = (
    Path(__file__).resolve().parent /
    "temporary_inventory"
)

TEMP_DIR.mkdir(
    parents=True,
    exist_ok=True
)

# ---------------------------
# CREATE TEMP INVENTORY
# ---------------------------

def create_temp_inventory(
    hosts
):

    inventory_path = (
        TEMP_DIR /
        "temp_inventory.ini"
    )

    with open(
        inventory_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write("[temporary]\n")

        for host in hosts:

            file.write(f"{host}\n")

    return inventory_path
