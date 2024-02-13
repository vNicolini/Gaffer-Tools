import Gaffer
import GafferScene
import IECore
import imath

class Box( Gaffer.SubGraph ) :

	def __init__( self, name = "Box" ) :

		Gaffer.SubGraph.__init__( self, name )

		self["SceneReader"] = GafferScene.SceneReader( "SceneReader" )
		self["SceneReader"].addChild( Gaffer.V2fPlug( "__uiPosition", defaultValue = imath.V2f( 0, 0 ), flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, ) )
		self["fileName"] = Gaffer.StringPlug( "fileName", defaultValue = '', flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, )
		self["tags"] = Gaffer.StringPlug( "tags", defaultValue = '', flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, )
		self["SceneReader"]["fileName"].setInput( self["fileName"] )
		self["SceneReader"]["tags"].setInput( self["tags"] )
		self["SceneReader"]["__uiPosition"].setValue( imath.V2f( -5.0999999, -2.20000005 ) )
		

		self.__removeDynamicFlags()

	# Remove dynamic flags using the same logic used by the Reference node.
	## 	odo : Create the plugs without the flags in the first place.
	def __removeDynamicFlags( self ) :

		for plug in Gaffer.Plug.Range( self ) :
			plug.setFlags( Gaffer.Plug.Flags.Dynamic, False )
			if not isinstance( plug, ( Gaffer.SplineffPlug, Gaffer.SplinefColor3fPlug, Gaffer.SplinefColor4fPlug ) ) :
				for plug in Gaffer.Plug.RecursiveRange( plug ) :
					plug.setFlags( Gaffer.Plug.Flags.Dynamic, False )

IECore.registerRunTimeTyped( Box, typeName = "MyTestExtension::Box" )
