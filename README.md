# CS 1XA3 Project01 - <nasirn4>
## Usage
Execute this script from project root with:
chmod +x CS1XA3/Project01/project_analyze.sh
./CS1XA3/Project01/project_analyze feature1 feature2 feature3
With arguments
	feature1: File Size List
	feature2: File Type Count
	feature3: FIXME log

....
## Feature 01
Description: List all files in the repo and their sizes in integer format in descending order.
Execution: Run the script ./project_analyze.sh feature1 . .
Reference: some code was taken from [[https://stackoverflow.com/questions/18193392/how-to-sort-a-file-in-unix-both-alphabetically-and-numerically-on-different-fiel]]

## Feature 02
Description: Using the read command, the user is prompted for an extension such as txt, pdf, py.
Make sure to just type in the extension without the '.' before it.
Execution: Run the script ./project_analyze.sh . feature2 .
Reference: some code was taken from [[https://tecadmin.net/prompt-user-input-in-linux-shell-script/]]

## Feature 03
Description: Find every file in the repo that has the word merge in the commit message and then
automatically checkout that commit. 
Execution: Run the script ./project_analyze.sh . . feature3
Reference: some code was taken from [[https://unix.stackexchange.com/questions/107067/tail-multiple-files-and-output-as-additional-column-with-find-results]]
...

## Custom Feature 
