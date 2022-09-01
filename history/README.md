# IP Ranges History

This directory includes a history of the `ip-ranges.json` file from AWS.

Technically it's possible to pull most of this history from Git (some of the first two years was manually added later).  Hopefully a second copy here makes it easy to parse if you want to run any scripts on the historical data.  The layout should be fairly self-explanatory, just note that the timestamp is based off of the timestamp in the JSON file.  It tends to be off by up to a minute, and notably the seconds in the timestamp is almost always an artificial value.

The script `pull_out_history.py` will run on a clone of this repo and create individual files from the git history for this repo of `ip_ranges.json` for the year in progress that's not yet checked into this folder.  The script `show_history.py` is an example script showing how to pull out each file from in and out of the tar files and process it in turn.

If anyone has any history I'm missing from 2015 and before, please drop me a [line](mailto:scott.seligman@gmail.com)!
