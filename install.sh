
###### Execute all ###############################################################################
#### source install.sh


pip install -r py36_docfull.txt 
pip install imodels ipython
pip install -e . 



####Only show current directory
 PS1="[\W]\\$ "

pwd
which python 





################################################################################################
#### Auto Batch



#The $0 variable is reserved for the function’s name.
#The $# variable holds the number of positional parameters/arguments passed to the function.