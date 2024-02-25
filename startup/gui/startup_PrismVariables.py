import IECore
import Gaffer
import GafferUI

import os
import pathlib
from pathlib import Path

def prismVariables( scriptContainer, script ):
    variables = script["variables"]
    
    CG_PROJECTS = os.environ['CG_PROJECTS_DIR']
    if CG_PROJECTS:
        filename = script["fileName"].getValue()
        
        # Checking if the file name is not null or empty
        if filename and len(filename) > 0:
            print("Loaded", filename ) 
            path = Path(filename)
            
            # PROJECT WIDE VARIABLES VALUES
            GAFFER_PROJECT_ROOT_DIR = path.parent.as_posix()
            PROJECT_NAME = path.parts[3]   # PROJECT_NAME values is at index 3
            DEPARTMENT = path.stem.split('_')[-2] # Define the context of the file (surfacing or lighting)
            VERSION = path.stem.split('_')[-1][1:]  # location of the VERSION in the filename

            #VARIABLES VALUES FOR LIGHTING
            SEQ, SHOT = path.parts[6], path.parts[7]   # SEQ and SHOT values are at index 6 and 7 in parts of the path

            #VARIABLES VALUES FOR SURFACING/LOOKDEV
            ASSET = path.parts[-5] # Grab the asset name regardless of how many subfolder/group it's part of
            LD_VERSION= "0001"

        else:
            print("!!! Unnamed file detected! !!!")
            return
    else:
        print("The 'CG_PROJECTS_DIR' environment variable is not set.")
        return


# PROJECT WIDE GLOBAL CONTEXT VARIABLES TO EDIT
    variables["projectName"]["value"].setValue(PROJECT_NAME)
    Gaffer.MetadataAlgo.setReadOnly( variables["projectName"]["name"], True )
    Gaffer.MetadataAlgo.setReadOnly( variables["projectName"]["value"], True )

    variables["projectRootDirectory"]["value"].setValue(GAFFER_PROJECT_ROOT_DIR)
    Gaffer.MetadataAlgo.setReadOnly( variables["projectRootDirectory"]["name"], True )
    Gaffer.MetadataAlgo.setReadOnly( variables["projectRootDirectory"]["value"], True )

# PROJECT WIDE GLOBAL CONTEXT VARIABLES TO CREATE
    if "projectDepartment" not in variables:
        projectDepartment = variables.addMember( "project:department", IECore.StringData(DEPARTMENT), "projectDepartment" )
    Gaffer.MetadataAlgo.setReadOnly( variables["projectDepartment"]["name"], True )
    Gaffer.MetadataAlgo.setReadOnly( variables["projectDepartment"]["value"], True )       

    if "projectDirectory" not in variables :
        projectDirectory = variables.addMember( "project:directory", IECore.StringData( "${CG_PROJECTS_DIR}/${project:name}" ), "projectDirectory" )
    Gaffer.MetadataAlgo.setReadOnly( variables["projectDirectory"]["name"], True )
    Gaffer.MetadataAlgo.setReadOnly( variables["projectDirectory"]["value"], True )


# GLOBAL CONTEXT VARIABLES FOR LIGHTING TO CREATE
    if DEPARTMENT == "Lighting":
        if "projectSeq" not in variables :
            projectSeq = variables.addMember( "project:seq", IECore.StringData(SEQ), "projectSeq" )
        Gaffer.MetadataAlgo.setReadOnly( script["variables"]["projectSeq"]["name"], True )
        Gaffer.MetadataAlgo.setReadOnly( script["variables"]["projectSeq"]["value"], True )

        if "seqShot" not in variables :
            seqShot = variables.addMember( "seq:shot", IECore.StringData(SHOT), "seqShot")
        Gaffer.MetadataAlgo.setReadOnly( variables["seqShot"]["name"], True )
        Gaffer.MetadataAlgo.setReadOnly( variables["seqShot"]["value"], True )

        if "shotVersion" not in variables :
            shotVersion = variables.addMember( "shot:version", IECore.StringData (VERSION), "shotVersion" )
        Gaffer.MetadataAlgo.setReadOnly( variables["shotVersion"]["name"], True )
        Gaffer.MetadataAlgo.setReadOnly( variables["shotVersion"]["value"], True )

        if "shotRenderDirectory" not in variables :
            shotRenderDirectory = variables.addMember( "shot:renderDirectory", IECore.StringData( "${project:directory}/03_Production/Shots/${project:seq}/${seq:shot}/Renders/3dRender/${renderPass}/v${shot:version}" ), "shotRenderDirectory" )
        Gaffer.MetadataAlgo.setReadOnly( variables["shotRenderDirectory"]["name"], True )
        Gaffer.MetadataAlgo.setReadOnly( variables["shotRenderDirectory"]["value"], True )



# GLOBAL CONTEXT VARIABLES FOR SURFACING/LOOKDEV TO CREATE
    if DEPARTMENT == "Surfacing":
        if "assetName" not in variables :
            assetName = variables.addMember( "asset:name", IECore.StringData (ASSET), "assetName" )
        Gaffer.MetadataAlgo.setReadOnly( variables["assetName"]["name"], True )
        Gaffer.MetadataAlgo.setReadOnly( variables["assetName"]["value"], True )

        if "lookdevVersion" not in variables :
            lookdevVersion = variables.addMember( "lookdev:version", IECore.StringData (LD_VERSION), "lookdevVersion" )
        Gaffer.MetadataAlgo.setReadOnly( variables["lookdevVersion"]["name"], True )
        Gaffer.MetadataAlgo.setReadOnly( variables["lookdevVersion"]["value"], True )

        if "assetRenderDirectory" not in variables :
            assetRenderDirectory = variables.addMember( "asset:renderDirectory", IECore.StringData( "${project:directory}/03_Production/Assets/${asset:name}/Renders/3dRender/${project:department}/v${lookdev:version}" ), "assetRenderDirectory" )
        Gaffer.MetadataAlgo.setReadOnly( variables["assetRenderDirectory"]["name"], True )
        Gaffer.MetadataAlgo.setReadOnly( variables["assetRenderDirectory"]["value"], True )



callbackHandle = application.root()["scripts"].childAddedSignal().connect( prismVariables, scoped = True )