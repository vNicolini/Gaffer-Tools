# How to install

## Setup on Windows
```
1- Download the repo.
2- Extract (if downloaded as Zip else just move) the repo in the desired location
3- Run gafferTools_setup.bat
```

## Setup on Linux
```
1- Download the repo.
2- Extract (if downloaded as Zip else just move) the repo in the desired location
3- Run gafferTools_setup.sh
```
>[!WARNING]
>The bash script currently is untested as I don't have a running linux system at the moment, it's expected to work but you've been warned in case it doesn't.

## How the setup works

The script will create (or append to if they already are set/existing) the following user environment variables:
```
GAFFER_TOOLS = parent directory of the bat/sh script(s) and tools
GAFFER_STARTUP_PATHS = allows the nodes to show up in the node creation menu in the nodegraph and will create a custom Global Context Variable point to ${GAFFER_TOOLS/assets}
GAFFER_REFERENCE_PATHS = location of the nodes files
```

# Content

## Yeti Procedural

https://github.com/vNicolini/Gaffer-Tools/assets/57097563/e1386b50-22df-4325-b06d-26a47c760550

Custom box that aleviates any potential user error(s) when loading and setting up Yeti Procedurals within Gaffer while keeping exposed important parameters as well as a debug tab.

>[!IMPORTANT]
>**This requires to have your Yeti/installationPath/bin to be set in your PATH variable for the bbox to be calculated and displayed accordingly**

---

## Turntable Tool (WIP)

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


#### Batch Render Support (WIP)

- **Batch Render Toggle:**  Allows to have the various HDRIs to be dispatched and rendered through a wedge node.  

> [!IMPORTANT]
> #### Prerequisites
> Requires a wedge node using the value set in the Selector plug of the Spreadsheet tab as Variable and the Index Variable plug set accordingly.
>
> Mode set to String List.
>
>**The Strings plug requires the enabledRowNames of the Spreadsheet as input.**
![Gaffer_BatchRenderWedge](https://github.com/vNicolini/Gaffer-Tools/assets/57097563/871fa3a8-690f-4dc3-b222-0930fa267ba2)

## GafferThree (WIP)
