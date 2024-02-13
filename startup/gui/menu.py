import os
import re
import traceback

import IECore

import Gaffer
import GafferScene
import GafferUI
import GafferDispatchUI
import GafferSceneUI

import Prism

## Node creation menu
###########################################################################

moduleSearchPath = IECore.SearchPath( os.environ["PYTHONPATH"] )

nodeMenu = GafferUI.NodeMenu.acquire( application )


# Define Turntable
def __turntable() :

    return Gaffer.Reference( "Turntable" )
def __turntablePostCreator( node, menu ) :

    node.load("Turntable.grf")

# Define YetiProcedural
def __YetiProcedural() :

    return Gaffer.Reference( "YetiProcedural" )
def __YetiProceduralPostCreator( node, menu ) :

    node.load("YetiProcedural.grf")

# Define GafferThree
def __GafferThree() :

    return Gaffer.Reference( "GafferThree" )
def __GafferThreePostCreator( node, menu ) :

    node.load("GafferThree.grf")



# Gaffer Tools nodes

nodeMenu.append(path = "/GafferTools/Turntable", nodeCreator = __turntable, postCreator = __turntablePostCreator, searchText = "Turntable")
nodeMenu.append(path = "/GafferTools/YetiProcedural", nodeCreator = __YetiProcedural, postCreator = __YetiProceduralPostCreator, searchText = "YetiProcedural")
nodeMenu.append(path = "/GafferTools/GafferThree", nodeCreator = __GafferThree, postCreator = __GafferThreePostCreator, searchText = "GafferThree")


# Prism nodes

nodeMenu.append( "/Prism/Importer", Prism.PrismAssetImporter, searchText = "PrismAssetImporter" )

# TEST NODES 
import MyTestExtension
import MyTestExtensionUI
nodeMenu.append( "/MyTestExtension/Box", MyTestExtension.Box )