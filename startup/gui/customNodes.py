import Gaffer
import GafferUI
import os

def __turntable() :

    return Gaffer.Reference( "Turntable" )

def __turntablePostCreator( node, menu ) :

    node.load("${library:references}/turntable.grf")

nodeMenu = GafferUI.NodeMenu.acquire( application )
nodeMenu.append(
    path = "/GafferTools/Turntable",
    nodeCreator = __turntable,
    postCreator = __turntablePostCreator,
    searchText = "Turntable"
)


def __YetiProcedural() :

    return Gaffer.Reference( "YetiProcedural" )

def __YetiProceduralPostCreator( node, menu ) :

    node.load("${library:references}/YetiProcedural.grf")

nodeMenu = GafferUI.NodeMenu.acquire( application )
nodeMenu.append(
    path = "/GafferTools/YetiProcedural",
    nodeCreator = __YetiProcedural,
    postCreator = __YetiProceduralPostCreator,
    searchText = "YetiProcedural"
)


def __GafferThree() :

    return Gaffer.Reference( "GafferThree" )

def __GafferThreePostCreator( node, menu ) :

    node.load("${library:references}/GafferThree.grf")

nodeMenu = GafferUI.NodeMenu.acquire( application )
nodeMenu.append(
    path = "/GafferTools/GafferThree",
    nodeCreator = __GafferThree,
    postCreator = __GafferThreePostCreator,
    searchText = "GafferThree"
)