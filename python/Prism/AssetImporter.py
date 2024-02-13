import IECore

import Gaffer
import GafferScene
import GafferImage

class PrismAssetImporter (GafferImage.ImageProcessor) :

    def __init__ (self, name= "PrismAssetImporter") :
        GafferImage.ImageProcessor.__init__( self, name )
        self['__deepState'] = GafferImage.DeepState()
        self['__deepState']['in'].setInput( self['in'] )
        self['__deepState']['enabled'].setInput( self['enabled'] )
        self['out'].setInput( self['__deepState']['out'] )
        self['out'].setFlags( Gaffer.Plug.Flags.Serialisable, False )

        self['__deepState']['deepState'].setValue( GafferImage.DeepState.TargetState.Tidy )
        Gaffer.PlugAlgo.promote( self['__deepState']['pruneTransparent'] )
        Gaffer.PlugAlgo.promote( self['__deepState']['pruneOccluded'] )
        Gaffer.PlugAlgo.promote( self['__deepState']['occludedThreshold'] )

IECore.registerRunTimeTyped( PrismAssetImporter, typeName = "Prism::PrismAssetImporter" )
