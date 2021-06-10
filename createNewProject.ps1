# A PowerShell script to automatically create a new project folder with .gitignore, .env and README.md for Windows

$folderName = Read-Host -Prompt 'Input the folder name'
$USERNAME = Read-Host -Prompt 'Input your name'

$ScriptDir = Split-Path $script:MyInvocation.MyCommand.Path # get current directory path
$time = (Get-Date).ToString("dddd MM/dd/yyyy HH:mm K")
$Path = 'C:\Users\User\Desktop\' + $folderName 

if (!(Test-Path $Path))
{
New-Item -itemType Directory -Path C:\Users\User\Desktop\ -Name $FolderName
}
else
{
write-host "Folder already exists"
}

Set-Location -Path $Path
New-Item README.md
Set-Content README.md "# $folderName
Created on $time by $USERNAME"
New-Item .env
New-Item .gitignore
Set-Content .gitignore '# Virtual Environment
myenv

#Environment variables
.env

#Jupyter Notebooks
*.ipynb

# Others
*.txt
*.png
*.jpg
__pychache__
'
Write-Host ' '
Write-Host "Current path  directory is $ScriptDir"