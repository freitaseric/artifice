[Setup]
AppName=Artífice
AppVersion=1.0
DefaultDirName={autopf64}\Artifice
DefaultGroupName=Artifice
OutputBaseFilename=Artifice-Setup-1.0
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
UninstallDisplayIcon={app}\Artifice.exe

[Files]
Source: "dist\Artifice.exe"; DestDir: "{app}"

[Icons]
Name: "{group}\Artifice"; Filename: "{app}\Artifice.exe"
Name: "{autodesktop}\Artifice"; Filename: "{app}\Artifice.exe"