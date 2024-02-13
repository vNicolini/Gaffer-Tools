import imath
import IECore
import Gaffer
import MyTestExtension

Gaffer.Metadata.registerNode(

	MyTestExtension.Box,

	
	plugs = {
	
		"fileName" : [
			'nodule:type', '',
			'description', "The name of the file to be loaded. The file can be\nin any of the formats supported by Cortex's SceneInterfaces.",
			'plugValueWidget:type', 'GafferUI.FileSystemPathPlugValueWidget',
			'path:leaf', True,
			'path:valid', True,
			'path:bookmarks', 'sceneCache',
			'fileSystemPath:extensions', 'abc lscc scc usd usda usdc usdz vdb',
			'fileSystemPath:extensionsLabel', 'Show only cache files',
		],
		
		"tags" : [
			'nodule:type', '',
			'description', 'Limits the parts of the scene loaded to only those\nwith a specific set of tags.',
		],
		
	}
	

)
