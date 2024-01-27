# How to install
 

## As user environment variables
### On windows:
```
1- Download the repo.
2- Extract (if downloaded as Zip else just move) the repo in the desired location
3- Run gafferTools_setup.bat
```

### On linux:
```
1- Download the repo.
2- Extract (if downloaded as Zip else just move) the repo in the desired location
3- Run gafferTools_setup.sh
```
>[!WARNING]
>The bash script currently is untested as I don't have a running linux system at the moment, it's expected to work but you've been warned in case it doesn't.


## In a wrapper
### On windows:
```
1- Download the repo.
2- Extract (if downloaded as Zip else just move) the repo in the desired location
3- If you already have a custom wrapper to start `gaffer.cmd` call gafferTools.bat prior to it (see example below)
```
### On linux:
```
1- Download the repo.
2- Extract (if downloaded as Zip else just move) the repo in the desired location
3- If you already have a custom wrapper to start `gaffer.cmd` call gafferTools.sh prior to it (see example below)
```

## How the setup works

The script will create (or append to if they already are set/existing) the following environment variables at user or wrapper/session level (depending on the setup you've chosen):
```
GAFFER_TOOLS = parent directory of the bat/sh script(s) and tools
GAFFER_STARTUP_PATHS = allows the nodes to show up in the node creation menu in the nodegraph and will create a custom Global Context Variable point to ${GAFFER_TOOLS/assets}
GAFFER_REFERENCE_PATHS = location of the nodes files
```  

### Example of a wrapper on windows:
```
@echo off

:: Define Arnold's SDK location
set "ARNOLD_ROOT=G:/pipeline/renderers/Arnold/Arnold-7.2.5.1-windows"

:: Define Yeti's Procedural location
set "ARNOLD_PLUGIN_PATH=G:/pipeline/Plugins/Maya/Yeti/2024/4.2.12/bin;%ARNOLD_PLUGIN_PATH%"

:: Load GafferTools
call "G:/pipeline/Utilities/Tools/Gaffer/Gaffer-Tools/gafferTools.bat"

:: Start Gaffer
"G:/pipeline/DCCs/gaffer-1.3.10.0-windows/bin/gaffer.cmd"
```

# Content

## Yeti Procedural

https://github.com/vNicolini/Gaffer-Tools/assets/57097563/e1386b50-22df-4325-b06d-26a47c760550

Custom box that aleviates any potential user error(s) when loading and setting up Yeti Procedurals within Gaffer while keeping exposed important parameters as well as a debug tab.

>[!IMPORTANT]
>**This requires to have your Yeti/installationPath/bin to be set in your PATH variable for the bbox to be calculated and displayed accordingly**

---

## Turntable Tool

### Overview

This Turntable Tool is designed to provide a streamlined way to create turntable animations with ease.  
  
This tool streamlines the process of setting up a turntable animation by automating asset and skydome rotation based on the timeline duration (split 50/50 by default). 
   
It also includes features such as rotation offset fields, inversion toggles, automatic camera framing based on the asset bounding box, normalized scaling of the cyclo and HDRI in viewport, HDRI support, and visibility toggles for enhanced control over your turntable renders.

https://github.com/vNicolini/Gaffer-Tools/assets/57097563/05370399-24fc-4d3b-8c94-ae904a8098c8

### Features  

#### Adaptive and Automatic Rotation  

- **Timeline Duration Control:** The tool automatically adapts asset and skydome rotation based on the timeline duration, ensuring a smooth and consistent turntable animation.  


#### Rotation Controls

- **Rotation Offset Fields:** Fine-tune your turntable animation with customizable rotation offset fields for both the skydome and asset, allowing precise control over the rotation angles.  

- **Inversion Toggles:** Toggle inversion of skydome and/or asset rotation independently, providing flexibility in achieving desired turntable effects.  


#### Camera Framing  

- **Automatic Asset Framing:** Enable automatic camera framing to adjust the camera based on the asset bounds. Optional padding further enhance control over the framing.  

#### Scaling and Visibility  

- **Normalized Ground and Viewport Skydome Scale:** Maintain visual coherence with normalized ground and viewport skydome scaling, ensuring consistency across different scenes.  

- **Skydome Camera Rays Visibility Toggle:** Easily toggle the visibility of skydome camera rays for a cleaner presentation.  

- **Cyclo Camera Rays Visibility Toggle:** Toggle the visibility of cyclo camera rays to customize the appearance of your turntable render.  

- **Reference Spheres Toggle:** Enable or disable reference spheres as needed for visual guidance in your turntable setup.  


#### HDRI Support  

- **HDRI Repository Loader:** Load HDRI environments from a repository to enhance the visual quality of your turntable renders.  

- **HDRI Dropdown Menu:** Conveniently select HDRI environments from a dropdown menu, providing a user-friendly interface for quick and easy HDRI adjustments.  


#### Batch Render Support (WIP Feature)

- **Batch Render Toggle:**  Allows to have the various HDRIs to be dispatched and rendered through a wedge node.  

> [!IMPORTANT]
> #### Prerequisites
> Requires a wedge node using the value set in the Selector plug of the Spreadsheet tab as Variable and the Index Variable plug set accordingly.
>
> Mode set to String List.
>
>**The Strings plug requires the enabledRowNames of the Spreadsheet as input.**
![Gaffer_BatchRenderWedge](https://github.com/vNicolini/Gaffer-Tools/assets/57097563/871fa3a8-690f-4dc3-b222-0930fa267ba2)

## GafferThree 

### Overview

Inspired by Ezequiel Mastrasso's LightCreator, part of the [LDTGaffer](https://github.com/ezequielmastrasso/LDTGaffer/tree/master "LDTGaffer's Repo") toolsuite he's developped.  
As well as Katana's GafferThree node, used for lighting (hence this name)  
  
It includes all you can expect from a lighting utility, creating lights, naming them, set AOV names, and more...  

https://github.com/vNicolini/Gaffer-Tools/assets/57097563/dc0e5cfc-392d-4a5e-babf-a303ad470440



### Features  

#### Light Types
GafferThree supports the creation of the following light types:  

- Quad Lights
- Skydome Lights
- Distant Lights
- Spot Lights
- Disk Lights
- Cylinder Lights  

#### Per-Light Type Parameters
Each light type comes with a set of specific parameters that can be adjusted to customize the lighting effect. These parameters include but are not limited to:

- Intensity/Exposure
- Color
- Size
- Cone Angle (for spot lights)
- Spread Angle
- Contribution
- etc ...  

#### HDRI Textures Support
GafferThree provides support for High Dynamic Range Imaging (HDRI) textures for Skydome and Quad lights. Users can easily load HDRI textures for the Skydome and Quad lights as well as color correct them if needed.  

#### Texture Resolution
For Quad and Skydome lights with textures, GafferThree allows users to set the resolution of the textures independtly between the viewport and the render output. This enables fine-tuning of the texture quality based on project requirements.  

#### Viewport Scale
Adjust the viewport scale of the lights visualiser. This feature helps users visualize and finetune more easily the lights orientation.  

#### Drawing Mode
GafferThree supports different drawing modes for lights in the viewport. Users can choose between wireframe, color, or textured representations to facilitate a more efficient and intuitive lighting workflow.

> [!NOTE]
> At the time of writting i haven't found a way to have the quad light display its color in the viewport **but** if/when you have an HDRI assigned to it it'll display, and the color correction also are displayed in the viewport. 
> It is **not** impacting the render output whatsoever, only the viewport visualization