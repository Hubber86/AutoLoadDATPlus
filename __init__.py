# __init__.py

def classFactory(iface):
    """
    Load AutoLoadDATPlusPlugin class from file and return an instance to QGIS.

    :param iface: A QGIS interface instance (QgisInterface)
    :return: An instance of the plugin
    """
    from .AutoLoadDATPlus import AutoLoadDATPlusPlugin
    return AutoLoadDATPlusPlugin(iface)
