import IECore
import Gaffer

def __scriptAdded( container, script ) :

    variables = script["variables"]

    if "libraryResources" not in variables :
            projectResources = variables.addMember(
                    "library:resources",
                    IECore.StringData( "$HOME/gaffer/resources" ),
                    "libraryResources"
            )

    Gaffer.MetadataAlgo.setReadOnly( variables["libraryResources"]["name"], True )

application.root()["scripts"].childAddedSignal().connect( __scriptAdded, scoped = False )