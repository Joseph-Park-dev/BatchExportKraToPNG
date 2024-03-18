# Batch save folder to png

This plugin gets the list of .kra files in the folder, exports them into .png files. 

## How to install

* In Krita go to Settings > Manage Resourcs > Open Resource Folder
* Copy `BatchSaveFolderPNG.desktop` into the pykrita folder
* Copy the `BatchSaveFolderPNG` folder into that `pykrita` folder

Restart Krita and make sure the plugin is enabled, which means ``Settings > Configure Krita > Python Plugin manager > Batch Save Folder to .png`` should be checked.

## How to use

You can find the script under ``Tools > Scripts > Batch Save Folder to .png``.
Browse the source folder, where you keep the .kra files to export,
and the destinatoin folder, where you will store the exported .png files.
Click the save button to start the process.

## Plugin's life
### 2024.03.07
Basic plugin with src_folder, dest_folder path button was made & uploaded to forum, gitHub.

### 2024.03.19
Improved plugin with better UI, enabling modification of .png export parameters.