import os
import inspect
import functools

import IECore

import Gaffer
import GafferUI


def prism_publish_box( menu ):

	scriptWindow = menu.ancestor( GafferUI.ScriptWindow )
	script = scriptWindow.scriptNode()

	selection = script.selection()
	print( selection[0].getName() )





GafferUI.ScriptWindow.menuDefinition(application).append(
"/Prism/" + "Publish Box",
	{
		"command" : functools.partial( prism_publish_box ),
		"label" : "Publish Box",
		"shortCut" : ""
	}
)
