import IECore
import Gaffer

def __scriptAdded( container, script ) :

    variables = script["variables"]

    # Add "project:directory" variable if not already present
    if "projectDirectory" not in variables :
        projectDirectory = variables.addMember(
            "project:directory",
            IECore.StringData( "${CG_PROJECTS_DIR}/${project:name}" ),
            "projectDirectory"
        )
        Gaffer.MetadataAlgo.setReadOnly( variables["projectDirectory"]["name"], True )
        Gaffer.MetadataAlgo.setReadOnly( variables["projectDirectory"]["value"], True )

    # Add "project:seq" variable if not already present
    if "projectSeq" not in variables :
        projectSeq = variables.addMember(
            "project:seq",
            IECore.StringData( "" ),
            "projectSeq"
        )
        Gaffer.MetadataAlgo.setReadOnly( variables["projectSeq"]["name"], True )
        Gaffer.MetadataAlgo.setReadOnly( variables["projectSeq"]["value"], True )

    # Add "seq:shot" variable if not already present
    if "seqShot" not in variables :
        seqShot = variables.addMember(
            "seq:shot",
            IECore.StringData( "" ),
            "seqShot"
        )
        Gaffer.MetadataAlgo.setReadOnly( variables["seqShot"]["name"], True )
        Gaffer.MetadataAlgo.setReadOnly( variables["seqShot"]["value"], True )

    # Add "shot:version" variable if not already present
    if "shotVersion" not in variables :
        shotVersion = variables.addMember(
            "shot:version",
            IECore.StringData ( "" ),
            "shotVersion"
        )
        Gaffer.MetadataAlgo.setReadOnly( variables["shotVersion"]["name"], True )
        Gaffer.MetadataAlgo.setReadOnly( variables["shotVersion"]["value"], True )

    # Add "shot:renderDirectory" variable if not already present
    if "shotRenderDirectory" not in variables :
        shotRenderDirectory = variables.addMember(
            "shot:renderDirectory",
            IECore.StringData( "${project:directory}/03_Production/Shots/${project:seq}/${seq:shot}/Renders/3dRender/${renderPass}/v${shot:version}" ),
            "shotRenderDirectory"
        )
        Gaffer.MetadataAlgo.setReadOnly( variables["shotRenderDirectory"]["name"], True )
        Gaffer.MetadataAlgo.setReadOnly( variables["shotRenderDirectory"]["value"], True )

application.root()["scripts"].childAddedSignal().connect( __scriptAdded, scoped = False )