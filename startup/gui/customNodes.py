import Gaffer
import GafferUI
import os

def __turntable() :

    return Gaffer.Reference( "Turntable" )

def __turntablePostCreator( node, menu ) :

    node.load("C:\\Users\\Admin\\gaffer\\projects\\RND\\customNodes\\turntable.grf")

nodeMenu = GafferUI.NodeMenu.acquire( application )
nodeMenu.append(
    path = "/Custom/Turntable",
    nodeCreator = __turntable,
    postCreator = __turntablePostCreator,
    searchText = "Turntable"
)


def __YetiProcedural() :

    return Gaffer.Reference( "YetiProcedural" )

def __YetiProceduralPostCreator( node, menu ) :

    node.load("C:\\Users\\Admin\\gaffer\\projects\\RND\\customNodes\\YetiProcedural.grf")

nodeMenu = GafferUI.NodeMenu.acquire( application )
nodeMenu.append(
    path = "/Custom/YetiProcedural",
    nodeCreator = __YetiProcedural,
    postCreator = __YetiProceduralPostCreator,
    searchText = "YetiProcedural"
)


def __GafferThree() :

    return Gaffer.Reference( "GafferThree" )

def __GafferThreePostCreator( node, menu ) :

    node.load("C:\\Users\\Admin\\gaffer\\projects\\RND\\customNodes\\GafferThree.grf")

nodeMenu = GafferUI.NodeMenu.acquire( application )
nodeMenu.append(
    path = "/Custom/GafferThree",
    nodeCreator = __GafferThree,
    postCreator = __GafferThreePostCreator,
    searchText = "GafferThree"
)