import GafferUI
import Gaffer
import os
import pathlib
from pathlib import Path
import functools


def set_prism_project( menu, version_up=False):
	CG_PROJECTS = os.environ['CG_PROJECTS_DIR']
	if CG_PROJECTS:
		scriptWindow = menu.ancestor( GafferUI.ScriptWindow )
		script = scriptWindow.scriptNode()
		
		filename = script["fileName"].getValue()
		print(filename)

		path = Path(filename)

		GAFFER_PROJECT_ROOT_DIR= path.parent.as_posix()
		PROJECT_NAME = path.parts[3]  # PROJECT_NAME values is at index 3
		SEQ, SHOT = path.parts[6], path.parts[7]  # SEQ and SHOT values are at index 6 and 7 in parts of the path
		VERSION = path.stem.split('_')[-1][1:]  # location of the VERSION in the filename

		projectName = script["variables"]["projectName"]["value"].setValue(PROJECT_NAME)
		print('PROJECT_NAME:', script["variables"]["projectName"]["value"].getValue())
		
		projectSEQ = script["variables"]["projectSeq"]["value"].setValue(SEQ)
		print('SEQ:', script["variables"]["projectSeq"]["value"].getValue())
				
		seqSHOT = script["variables"]["seqShot"]["value"].setValue(SHOT)
		print('SHOT:', script["variables"]["seqShot"]["value"].getValue())
		
		shotVERSION = script["variables"]["shotVersion"]["value"].setValue(VERSION)
		print('VERSION:', script["variables"]["shotVersion"]["value"].getValue())
		
		gafferProjectRootDir = script["variables"]["projectRootDirectory"]["value"].setValue(GAFFER_PROJECT_ROOT_DIR)
		print('projectRootDirectory:', script["variables"]["projectRootDirectory"]["value"].getValue())

	else:
		print("The 'CG_PROJECTS_DIR' environment variable is not set.")
		return

GafferUI.ScriptWindow.menuDefinition(application).append(
"/Prism/" + "Set Project",
	{
		"command" : functools.partial( set_prism_project ),
		"label" : "Set Project",
		"shortCut" : ""
	}
)
