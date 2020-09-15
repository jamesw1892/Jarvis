# Introduction

Jarvis is my own virtual assistant, designed to separate internal workings from use so it can work on many devices. The internal workings are a function that takes a string input (the command) and outputs a string (the response). It is Jarvis's job to understand the command and form a meaningful response.

# Input and Output

In addition to text input, Jarvis supports listening to voice and using speech to text technology to convert it before being fed into the internal workings. Similarly, in addition to printing to a screen, Jarvis supports speaking the output using text to speech technology. While Jarvis's interal workings can be the same no-matter the device, listening and speaking changes depending on the device.

# Plan

Rather than having `speaker` and `listener` classes for each OS, have `inputter` and `outputter` classes for each device and within it, handle whether to listen, print, speak or get text input depending on what they want and if there are errors