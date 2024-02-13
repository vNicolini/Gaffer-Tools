__import__("IECore")
__import__("Gaffer")
__import__("GafferScene")

from .AssetImporter import PrismAssetImporter

__import__( "IECore" ).loadConfig( "GAFFER_STARTUP_PATHS", subdirectory = "Prism" )
