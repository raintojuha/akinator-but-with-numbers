# Python number guesser game
A quick and dirty "game" in the style of Akinator. Fun to make. Not so to play.

- The user thinks of a number between 0 and 1000
    - Target values can be changed in code
    - _future idea: user can set values in the beginning of each game_

- The machine guesses the number
    - Machine has two values in memory: _mininum_ and _maximum_
    - The guess is made via a random integer function
        - _future idea: develop a model that runs through most likely numbers_
        - _future idea: guesses shouldn't be made too close to each other e.g. 223 -> 224_
    - Should the guess be too high, or low, the _min_/_max_ values are updated to restrict future guesses to known range


**From RNG to a data model**
Maybe there aught to be a list of likely numbers that are guessed before others.


**Things to do before "ready"**
- Stop users from using Higher or Lower commands if guess is right on the edge
    - e.g.
Selecting Lower on 0
Selecting Higher on max_possible


- Stylize console outputs and inputs
    - More ASCII art
- Come up with BANTER, CURSE and CELEBRATE messages