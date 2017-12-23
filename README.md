# CRDL Data visualizer

For now this is a quick test for visualizing data from the CRDL.

### what?
crdl_viewlinechart.html - experiment to visualize sensor data from the CRDL
maketestdata.py - python program to generate fake data for testing amount of datapoints etc.

### todo
- filter all points that are at zero (or under treshold), or do not log them from the python logger(!)
- color bits based on intensity, guess the kind of touch
- try and log from the CRDL software instead of the sensor readout