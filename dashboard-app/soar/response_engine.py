import subprocess

# ---------------------------
# BLOCK USER
# ---------------------------

def block_linux_user(
    username
):

    command = [

        "sudo",
        "usermod",
        "-L",
        username
    ]

    try:

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        return {

            "success": True,
            "output": result.stdout
        }

    except Exception as error:

        return {

            "success": False,
            "error": str(error)
        }
