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
### Feature 01
*Description:* List all files in the repo and their sizes in integer format in descending order
using the flag -rn.
*Execution:* Run the script ./project_analyze.sh feature1 . .
*Reference:* some code was taken from [[https://stackoverflow.com/questions/18193392/how-to-sort-a-file-in-unix-both-alphabetically-and-numerically-on-different-fiel]]

### Feature 02
*Description:* Using the read command, the user is prompted for an extension such as txt, pdf, py.
In order to get rid of the absolute path, a variable parent_path was created that gets the
absolute path of the script and then uses that to get the parent directory by cd-ing into it.
*Execution:* Run the script ./project_analyze.sh . feature2 .
Make sure to just type in the extension without the '.' before it.
*Reference:* some code was taken from [[https://tecadmin.net/prompt-user-input-in-linux-shell-script/]]
				    [[https://stackoverflow.com/questions/24112727/relative-paths-based-on-file-location-instead-of-current-working-directory/24113238]]

### Feature 03
*Description:* Find every file in the repo that has the word #FIXME in the last line using find for
the file, tail -1 for the last line and grep for the word. It then puts list of the file names in
CS1XA3/Project01/fixme.log with each gile seperated by a newline. 
*Execution:* Run the script ./project_analyze.sh . . feature3
Then type in ls and you will find the file fixme.log. Type in less fixme.log and you will be able
to view the contents of this file.
*Reference:* some code was taken from [[https://unix.stackexchange.com/questions/107067/tail-multiple-files-and-output-as-additional-column-with-find-results]]
...

### Custom Feature 01
*Description:* This feature creates a file CS1XA3/Project01/sortedprocesses.log if it doesn't exist,
if it does exist overwrite it.
This file will contain a list of all the process identification numbers sorted in descending order.

### Custom Feature 02
*Description:* This feature removes duplicate lines from all files.
It creates a file CS1XA3/Project01/removedlines.log where a list of all removed lines is stored in
ascending order. 
