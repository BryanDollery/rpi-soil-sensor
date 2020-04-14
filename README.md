# Raspberry Pi Soil Sensor

A Python-3 script to read events from a soil sensor. The other scripts I found were rather basic. The gpio pin triggers continuously so its necessary to ensure that we're ignoring spurious events and only responding to the initial event. There are two approaches to this, one in each python file, but only the first one really works.

The first approach, in soil.py, uses a timer to ensure that the events are more than a second apart, resetting the time on each event. In my experiments, the events are triggered approx. every 100ms, so a 1 second period is fine.

The second approach is to respond to events only when the gpio pin is 'high' (has a value of 1), which indicates that the sensor is wet. Unfortunately this leads to many false positives as the sensor isn't very high-quality and continually flicks between wet and dry.
