import Gaffer
import GafferScene
import IECore
import imath

class PrismAssetImporter_Lite( Gaffer.SubGraph ) :

	def __init__( self, name = "PrismAssetImporter_Lite" ) :

		Gaffer.SubGraph.__init__( self, name )

		self["SceneReader"] = GafferScene.SceneReader( "SceneReader" )
		self["out"] = GafferScene.ScenePlug( "out", direction = Gaffer.Plug.Direction.Out, flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, )
		self["BoxOut"] = Gaffer.BoxOut( "BoxOut" )
		self["BoxOut"].setup( GafferScene.ScenePlug( "in", ) )
		self["tags"] = Gaffer.StringPlug( "tags", defaultValue = '', flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, )
		self["prismDept"] = Gaffer.StringPlug( "prismDept", defaultValue = '', flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, )
		self["fileName"] = Gaffer.StringPlug( "fileName", defaultValue = '', flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, )
		self["SceneReader"]["tags"].setInput( self["tags"] )
		self["out"].setInput( self["BoxOut"]["__out"] )
		self["BoxOut"]["in"].setInput( self["SceneReader"]["out"] )
		Gaffer.Metadata.registerValue( self["BoxOut"]["__out"], 'nodule:type', 'GafferUI::StandardNodule' )
		Gaffer.Metadata.registerValue( self["BoxOut"]["__out"], 'description', 'The output scene.' )
		self["fileName"].setInput( self["SceneReader"]["fileName"] )

		self["Expression"] = Gaffer.Expression()
		self["Expression"].setExpression('''import pathlib
from pathlib import Path

prismDeptValue = parent["__in"]["PrismAssetImporter_Lite"]

parts = prismDeptValue.split('/')

asset_name = parts[-3]
department_name = parts[-1]
file_format = ".abc"

masterPath = str(prismDeptValue + "/" + "master")
								   
parent["SceneReader"]["fileName"] = masterPath + "/" + asset_name + "_" + department_name + "_" + "master" + file_format
'''
		)
 
		self.__removeDynamicFlags()

	# Remove dynamic flags using the same logic used by the Reference node.
	## 	odo : Create the plugs without the flags in the first place.
	def __removeDynamicFlags( self ) :

		for plug in Gaffer.Plug.Range( self ) :
			plug.setFlags( Gaffer.Plug.Flags.Dynamic, False )
			if not isinstance( plug, ( Gaffer.SplineffPlug, Gaffer.SplinefColor3fPlug, Gaffer.SplinefColor4fPlug ) ) :
				for plug in Gaffer.Plug.RecursiveRange( plug ) :
					plug.setFlags( Gaffer.Plug.Flags.Dynamic, False )

IECore.registerRunTimeTyped( PrismAssetImporter_Lite, typeName = "PrismAssetImporter_Lite::PrismAssetImporter_Lite" )
