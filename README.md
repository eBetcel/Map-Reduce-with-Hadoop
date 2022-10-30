# Map/Reduce with Hadoop

This practice is about programming map/reduce functions in some datasets to be processed at a Hadoop cluster using Yarn.

## Requirements:
. Installing Apache Hadoop with at least 2 nodes
. Complete the tasks below developing the provided scripts
## Tasks
1. Get the 10 highest incomes
* Download file salarios.csv (incoming) avaliable at this [link](https://goo.gl/A3MhFS). 
* Modify the files mapper.py and reducer.py to create mapping and reducing functions to output a list with the 10 highiest incomes, returning the name and income.
2. Extract file names with less than 5 characters
* Download the [weblog file](https://goo.gl/A3MhFS) (weblog_entries.txt)
* Make the necessary changes to mapper.py and reducer.py to generate a list with the name of the files .html having the number of characters lesser or equal than 5
3. Calculate stats from users that accessed the e-mail service
* Download the e-mail [weblog file](https://goo.gl/A3MhFS) (dovecot.log)
* Output: A list with all the user names and how many times they tried to access the mail service, but only the ones with more than 100 entries
