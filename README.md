# Python Uncertainties

Python uncertainties with Josh and Ruhan.
Hello, if you're reading this, something has happened. Something terrible.
I can only give you one clue, but there are 39 total, the 39 clues.
The clue lies in this read me file, this very text has a deeper meaning.
Anyways, back to the code...
Right now, our Main.py has the "old version" of our python uncertainties module. There's no user interface. To create an value with an uncertainty, use `Values(a, b)` to create a values class, `a` being the value and `b` being the absolute uncertainty.

Store those in variables, and do math with them with our operator functions from our [Uncertainties.py](Uncertainties.py) module. In it you can add, mutiply, divide, and subtract Values. You can also scale values by a certain constant and raise values to a constant power.

You cann't add constant values to a Value yet but we'll inplement that when we do our UI.