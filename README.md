# debian_stats

Command line tool for downloading compressed Content files associated with a Debian mirror, and parsing the file to return the top 10 most common packages.

Design process:
Can break the project into 4 distinct steps: get command line input from user, download specified architecture, parse file, print statistics.
Functions for the last 3 steps were completed first, and then invoked in main() alongside user command line input.

1. file_download(): used requests library to download the file locally
2. file_parse(): used the gzip library to unzip file and read line by line. used the .split function to isolate package names and store quantities inside a dictionary
3. print_stats(): formatted printout of the top 10 most common packages inside the dictionary using itemgetter
4. main(): used argparse to get user input

Entire project took ~3 hours. Most challenging part was learning the gzip library to propelry decode the downloaded files. Was running into UnicodeDecode errors prior to learning the full functionalities of the gzip.open function.
