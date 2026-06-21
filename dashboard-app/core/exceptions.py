class SOCPlatformException(Exception):
    pass


class CMDBException(SOCPlatformException):
    pass


class IntegrationException(SOCPlatformException):
    pass


class AuthenticationException(SOCPlatformException):
    pass


class InventoryException(SOCPlatformException):
    pass


class BaselineException(SOCPlatformException):
    pass
