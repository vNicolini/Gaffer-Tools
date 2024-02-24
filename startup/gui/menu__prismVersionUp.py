import GafferUI
import GafferSceneUI

import os
import functools
import json
from pathlib import Path

def prism_save_script(menu):
    proj = os.environ['CG_PROJECTS_DIR']
    
    if proj:
        scriptWindow = menu.ancestor(GafferUI.ScriptWindow)
        script = scriptWindow.scriptNode()
        variables = script["variables"]
        
        filename = script["fileName"].getValue()
        path = Path(filename)
        GAFFER_PROJECT_ROOT_DIR = path.parent.as_posix()
                
        scene_name, shotVersion = path.stem.split('_v')
        
        shotVersion = int(shotVersion) + 1
        
        script_name = "_".join([scene_name, f"v{shotVersion:04d}"]) + path.suffix 
        
        script_filename = os.path.join(GAFFER_PROJECT_ROOT_DIR, script_name)
        
        dialogue = GafferUI.BackgroundTaskDialogue("Saving File")
        result = dialogue.waitForBackgroundTask(functools.partial(script.serialiseToFile, script_filename), parentWindow=scriptWindow)
        
        if not isinstance(result, Exception):
            print("New version saved:",script_filename)
            script["fileName"].setValue(script_filename)
            script["unsavedChanges"].setValue(False)
            versioninfo = {
                "project_path": GAFFER_PROJECT_ROOT_DIR,
                "sequence": scene_name.split('-')[0],
                "shot": scene_name.split('-')[-1].split('_')[0],
                "department": script_filename.split('/')[-2],
                "task": script_filename.split('/')[-1].split('.')[0],
                "version": f"v{shotVersion:04d}",
                "type": "shot",
                "user": os.getlogin(),  
                "comment": "",    # add comments if needed
                "username": os.getlogin()  # get current logged in username
            }

            with open(os.path.join(GAFFER_PROJECT_ROOT_DIR, f"{script_name.split('.')[0]}versioninfo.json"), 'w') as jsonfile:
                jsonfile.write(json.dumps(versioninfo, indent=4))
                
            variables["shotVersion"]["value"].setValue(f"{shotVersion:04d}")  
          
            # Grab a screenshot of the first Viewer found in the current ScriptWindow
            scriptWindow = GafferUI.ScriptWindow.acquire( script )
            viewer = scriptWindow.getLayout().editors( GafferUI.Viewer )[0]
            GafferUI.WidgetAlgo.grab( widget = viewer, imagePath = os.path.join(GAFFER_PROJECT_ROOT_DIR, f"{script_name.split('.')[0]}preview.jpg") )
            
        
		


            
GafferUI.ScriptWindow.menuDefinition(application).append(
"/Prism/" + "Version Up",
{
    "command": functools.partial(prism_save_script),
    "label": "Version Up",
    "shortCut": ""
}
)