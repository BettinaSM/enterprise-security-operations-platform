import platform

IS_WINDOWS = platform.system().lower() == "windows"

if IS_WINDOWS:
    try:
        import win32net
        import win32security
    except:
        pass
