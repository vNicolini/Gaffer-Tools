import GafferUI
import os
import functools


def custom_save_scrip( menu, version_up=False):
	proj = os.environ['PROJ']
	if proj:
		scriptWindow = menu.ancestor( GafferUI.ScriptWindow )
		script = scriptWindow.scriptNode()
		
		level_dir = os.environ['LEVEL_DIR']
		shot = os.environ['SHOT']
		task = os.environ['TASK']
		
		gaffer_dir = os.path.join(level_dir, task, 'gaffer')
		if not os.path.exists(gaffer_dir):
			os.mkdir(gaffer_dir)

		scene_name = script['variables']['projectName']['value'].getValue()
		script_version = int(script["variables"]["projectVersion"]['value'].getValue())

		if version_up:
			script_version = script_version+1

		else:
			scene_name_diag = GafferUI.TextInputDialogue( initialText = scene_name, title="Scene Name", confirmLabel="Set" )
			scene_name = scene_name_diag.waitForText( parentWindow = scriptWindow )

		if scene_name:
			script['variables']['projectName']['value'].setValue(scene_name)
			script_name = "%s.%s.v%02d.gfr" % (shot, scene_name, script_version)
			script_filename = os.path.join(gaffer_dir, script_name)

			dialogue = GafferUI.BackgroundTaskDialogue( "Saving File" )
			result = dialogue.waitForBackgroundTask( functools.partial( script.serialiseToFile, script_filename ), parentWindow = scriptWindow )
			if not isinstance( result, Exception ) :
				print(script_name)
				script["fileName"].setValue( script_filename )
				script["variables"]["projectVersion"]['value'].setValue(f"{script_version:02d}")
				script["unsavedChanges"].setValue( False )
	else:
		return

GafferUI.ScriptWindow.menuDefinition(application).append(
"/CUSTOM_MENU/" + "Save Script",
	{
		"command" : functools.partial( custom_save_scrip ),
		"label" : "Save Script",
		"shortCut" : "Shift+S"
	}
)
GafferUI.ScriptWindow.menuDefinition(application).append(
"/CUSTOM_MENU/" + "Version Up",
	{
		"command" : functools.partial( custom_save_scrip, version_up=True ),
		"label" : "Version Up",
		"shortCut" : "Shift+Alt+S"
	}
	
)

