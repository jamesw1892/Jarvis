from Validation import true_false

from kivy.utils import platform # str equal to one of ‘win’, ‘linux’, ‘android’, ‘macosx’, ‘ios’ or ‘unknown’


if platform == "win":
    from OSWindows import main
    main(true_false("Listen? "), true_false("Speak? "))
elif platform == "android":
    from OSAndroid import main
    main(true_false("Listen? "), true_false("Speak? "))
else:
    raise NotImplementedError()
