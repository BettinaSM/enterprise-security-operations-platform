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

class AuthorizationException(SOCPlatformException):
    pass


class ThreatIntelException(SOCPlatformException):
    pass


class DetectionException(SOCPlatformException):
    pass


class RiskEngineException(SOCPlatformException):
    pass


class VulnerabilityException(SOCPlatformException):
    pass


class CloudIntegrationException(SOCPlatformException):
    pass


class DatabaseException(SOCPlatformException):
    pass


class SOARException(SOCPlatformException):
    pass
