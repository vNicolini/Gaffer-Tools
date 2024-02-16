import imath
import pathlib
from pathlib import Path
import IECore
import Gaffer
import GafferUI
import GafferScene
import PrismAssetImporter_Lite

# Function to get the asset exportPath from script.
def get_asset_exportPath(script):
    filename = script['fileName'].getValue()   # Get file path from script
    filename = Path(filename)                  # Convert string to Path object    
    asset_exportPath = filename.parents[3] / "Export"   # Define export path
    return asset_exportPath                       # Return the export path

# Function to get departments and their values
def get_departments(asset_exportPath): 
    dept_folders = [item for item in asset_exportPath.glob('*') if item.is_dir()]  
    dept_names = [dept_folder.name for dept_folder in dept_folders]    
    dept_values = [str(dept_folder) for dept_folder in dept_folders]    
    return IECore.StringVectorData(dept_names), IECore.StringVectorData(dept_values) 

# Function to get versions and their values for a specified department
def get_versions(asset_exportPath, dept_name): 
    versions_folders = [item for item in (asset_exportPath / dept_name).glob('*') if item.is_dir()]  
    version_names = [version_folder.name for version_folder in versions_folders]    
    version_values = [str(version_folder) for version_folder in versions_folders]     
    return IECore.StringVectorData(version_names), IECore.StringVectorData(version_values) 


Gaffer.Metadata.registerNode(

	PrismAssetImporter_Lite.PrismAssetImporter_Lite,

	'uiEditor:emptySections', IECore.StringVectorData( [  ] ),
	'uiEditor:emptySectionIndices', IECore.IntVectorData( [  ] ),
	plugs = {
	
		"out" : [
			'nodule:type', 'GafferUI::StandardNodule',
			'description', 'The output scene.',
			'layout:section', 'Settings',
			'layout:index', 0,
		],
		
		"tags" : [
			'nodule:type', '',
			'description', 'Limits the parts of the scene loaded to only those\nwith a specific set of tags.',
			'divider', True,
			'layout:section', 'Settings',
			'layout:index', 2,
		],
			
		"prismDept" : [
			'nodule:type', '',
			'layout:section', 'Settings',
			'plugValueWidget:type', 'GafferUI.PresetsPlugValueWidget',
			'label', 'Department',
			'layout:index', 4,
			'presetsPlugValueWidget:allowCustom', False,
			'presetNames', lambda plug : get_departments( get_asset_exportPath( plug.node().scriptNode() ) )[0],  
			'presetValues', lambda plug : get_departments( get_asset_exportPath( plug.node().scriptNode() ) )[1], 
		],
		
		"fileName" : [
			'nodule:type', '',
			'description', "The name of the file to be loaded. The file can be\nin any of the formats supported by Cortex's SceneInterfaces.",
			'plugValueWidget:type', 'GafferUI.FileSystemPathPlugValueWidget',
			'path:leaf', True,
			'path:valid', True,
			'path:bookmarks', 'sceneCache',
			'fileSystemPath:extensions', 'abc lscc scc usd usda usdc usdz vdb',
			'fileSystemPath:extensionsLabel', 'Show only cache files',
			'layout:section', 'Settings',
			'layout:index', 1,
		],
		
	}
	
)
