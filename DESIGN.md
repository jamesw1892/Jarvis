# Input and Output

In addition to text input, Jarvis supports listening to voice and using speech to text technology to convert it before being fed into the internal workings. Similarly, in addition to printing to a screen, Jarvis supports speaking the response using text to speech technology. While Jarvis's internal workings can be the same no-matter the device, listening and speaking changes depending on the device.

# Interfaces

The public-facing and necessary methods for classes to define and how they work.

## Jarvis's Core (`Core.py`)

### Init

Initialise state here which will play a role with machine learning when added.

### Respond

The respond function takes in a string (the command) and outputs a string (the reponse). It is Jarvis's job to understand the command and form a meaningful response.

## Systems Support (start with `OS`, e.g.: `OSWindows.py`, `OSAndroid.py`, ...)

Adding support for systems requires 2 classes - `Inputter` and `Outputter`. `Inputter` requires an init and a `input_` method and `Outputter` requires an init and a `output` method. The init should ask the prefered medium of input/output, e.g.: listen or text input. The method itself should try to use the prefered medium (which is likely to be system specific), but if any problems should arise, it should revert to the backup mediums and log errors. In `IO.py` there are methods for text input (`input_`) and output (`output`). Errors should be logged using the `logging` library and the format is set up when `IO.py` is imported.

# Windows Saving Sound Files

On Windows, google TTS generates a sound file from the text which has to be saved before being opened. To potentially reduce the number of these needing to be created, I store all the sound files with an index recording what is said in each sound file. They are stored in `%TEMP%/Jarvis`, the index is `index.jarvis` which is a text file and the sound files are `mp3` files numbered from 0 upwards. The index file consists of a line (with trailing `\n`) for each response. The line number it is on (starting from 0) is the sound file to pick.