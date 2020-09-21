# Input and Output

In addition to text input, Jarvis supports listening to voice and using speech to text technology to convert it before being fed into the internal workings. Similarly, in addition to printing to a screen, Jarvis supports speaking the output using text to speech technology. While Jarvis's internal workings can be the same no-matter the device, listening and speaking changes depending on the device.

# Plan

Rather than having `speaker` and `listener` classes for each OS, have `inputter` and `outputter` classes for each device and within it, handle whether to listen, print, speak or get text input depending on what they want and if there are errors

# Interfaces

## Jarvis's Core

### Init

Could initialise data here which could help with machine learning

### Respond

The respond function takes in a string (the command) and outputs a string (the reponse). It is Jarvis's job to understand the command and form a meaningful response.

## Systems Support

Adding support for systems required 2 classes - `Inputter` and `Outputter`. `Inputter` requires an init and a `input_` method and `Outputter` requires an init and a `output` method. The init should ask the prefered medium of input/output, e.g.: listen or text input. The method itself should try to use the prefered medium (which is likely to be system specific), but if any problems should arise, it should revert to the backup mediums and log errors. In `IO.py` there are methods for text input (`input_`) and output (`output`). Errors should be logged using the `logging` library. The logging system has already been set up