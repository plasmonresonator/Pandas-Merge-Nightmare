# Pandas Merge Nightmare

This is a very small example of the sort of data I am trying to combine.

I want to line up/merge historical sales and territory data with new territory assignments and predictions. However, the powers that be provided a file with inconsistent account naming and shipping ID information.

To make things worse, the excel file with the new territory assignments is ~10,000 rows by 40 rows and the historical sales data file is about 4,200 rows by 20 rows.

I can get the matching rows merged ok, but I'm having trouble working through the process of after the initial merge on Account, how do I look for other columns that might provide matches (like Ship to ID, or a corrected account name, etc.) and merge that into the final file, without duplicating or losing sales data (from the old sales file) or future projection data (from the new territory file)?

### Any help would be MUCH appreciated!
