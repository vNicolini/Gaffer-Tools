import IECore
import Gaffer

def __scriptAdded( container, script ) :

    variables = script["variables"]

    # Add "library:references" variable if not already present
    if "libraryReferences" not in variables :
        libraryReferences = variables.addMember(
            "library:references",
            IECore.StringData( "${GAFFER_TOOLS}/resources/references" ),
            "libraryReferences"
        )
        Gaffer.MetadataAlgo.setReadOnly( variables["libraryReferences"]["name"], True )
        Gaffer.MetadataAlgo.setReadOnly( variables["libraryReferences"]["value"], True )

    # Add "library:assets" variable if not already present
    if "libraryAssets" not in variables :
        libraryAssets = variables.addMember(
            "library:assets",
            IECore.StringData( "${GAFFER_TOOLS}/resources/assets" ),
            "libraryAssets"
        )
        Gaffer.MetadataAlgo.setReadOnly( variables["libraryAssets"]["name"], True )
        Gaffer.MetadataAlgo.setReadOnly( variables["libraryAssets"]["value"], True )


application.root()["scripts"].childAddedSignal().connect( __scriptAdded, scoped = False )
