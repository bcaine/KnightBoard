# Knight Board

By: Ben Caine

### Requirements
networkx

### Running
Running requires specifying the data file and the level.

    ben@ava:~/Development/jobs/cruise$ python knight -h
    usage: knight [-h] -p PATH -l LEVEL

    Solution to Cruise's Knight Board Challenge

    optional arguments:
      -h, --help            show this help message and exit
      -p PATH, --path PATH  Path to Board
      -l LEVEL, --level LEVEL
                            Level 1-5

So for example, running level 4 (32x32 shortest path):

    python knight -l 4 -p data/32x32.txt



