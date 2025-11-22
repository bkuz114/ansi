"""
handy reference of ansi escape sequences.
based on script by "Richard":
https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences

usage:
    python ansi.py
"""

import random

# min spaces between the columns displaying the esc sequences
base_padding = 2
# ansi esc seq for setting background color of text
# (.format with desired color -- int between 1-256 -- i.e. bgseq.format("2")
bgseq = "\033[48;5;{}m"
# ansi esc seq to set text color
# (.format with desired color -- int between 1-256 -- i.e. fgseq.format("2")
fgseq = "\033[38;5;{}m"
reset = "\033[39m\033[49m"  # ansi esc seq to undo color (bg or text color)
bold = "\033[1m"  # ansi esc seq for bold
bold_off = "\033[22m"  # turns bold off
blue = "\033[38;5;3;48;5;17m"  # blue color

print("\n\nTo help remember ansi escape sequences...")


def padding(n):
    """
    Returns whitespace padding to put after color esc
    sequences to that it will line up with the other cols.
    (context: this script prints esc sequences for the
    basic 256 colors; the sequences are varying widths
    due to colors being represented by ints 1-256, i.e.
    string "\033[38;5;2m" not as wide as "\033[38;5;100m"
    so when printing these escape sequences, need to add
    padding so that all the cols line up.

    :param int n: int between 1-256; the color for this esc seq
    :return: str: the ws padding to go after col
    """
    numstr = 3-len(str(n)) + base_padding  # 3 is max len of str(n) as n <= 256
    return " "*numstr


def color_str(string, bg):
    """
    assigns a random color to every char in a string

    :param str string: the string to color
    :param bool bg: if True, color the background,
        if False, color the text
    :return str: the string, with ansi esc sequences
        that will print every char in the string as
        a different color
    :example: print(color_str("hello"))
    """
    newstr = ''
    for i in string:
        char = str(random.randint(1, 256))
        if bg:
            newstr += bgseq.format(char)
        else:
            newstr += fgseq.format(char)
        newstr += i
    newstr += reset
    return newstr


def display(bg=False):
    """
    prints to stdout escape sequences for the 256 basic colors,
    either as colored text, or background color

    :param bool bg: if True, display background colors; if False,
        display text colors
    """

    cols = 10  # num esc sequences to display before line break

    print("")
    # create a header

    # text inside header
    innertext = " Colors! :-) "
    if bg:
        innertext = " Backgrounds! "
    # num - chars on sides of the header text
    # note: 14 is the length (num of chars in) the widest
    # possible esc seq (i.e. for a color like 256)
    # thus 14 + base_padding is the width of each col
    size = int(
            (((14 + base_padding) * cols) - len(innertext))
            / 2)
    header_side = '-'*size
    # print header with inner text bolded (remember to unbold)
    print(color_str(header_side, bg) +
          bold + blue +
          innertext +
          bold_off +
          reset +
          color_str(header_side, bg))

    # print the esc sequences, in tidy columns
    for i in range(1, 256):
        # padding to make the cols line up
        col_padding = padding(i)
        base = ''  # the actual ansi esc sequence i.e. \033[38;5;20m
        if bg:
            base = bgseq.format(str(i))
        else:
            base = fgseq.format(str(i))
        """
        line below explained...
        Goal is to print to stdout the ansi esc sequence
        for this color, IN this color i.e. want to print
        \033[38;5;5m to stdout in red; thus you must print
        the escape sequence (to start the color), then print
        an the _escaped_ escape sequence (i.e. the sequence
        with a leading "\" so that it's interpreted as a regular
        string). Code below:
        * 'base' is the ansi esc sequence
        * "\\033" + base[1:] is the "escaped" esc sequence
            (base[1:] removes the first char in base, which
            python interprets as the entire \033; so this
            essentially gives you \\033[38;5;2m [or we the
            color is...] -- python will interpret this as
            regular string so if you print it, it'll print
            it as text) note: can't just do "\" + base --
            it doesn't work
        * fyi: print(base) [the actual esc sequence] prints
            nothing to stdout -- it just starts the esc sequence
            (i.e. everything after it will be in that color)
        * col padding to add padding after the col
        * reset -- reset esc sequence to turn off the color
        * end='' means no newline after this print
        """
        print(base + "\\033" + base[1:] + col_padding + reset, end='')

        # each 10th col print a newline
        if not i % cols:
            print("")
    print("")


display()
print("")
display(True)

print("\n                   " +
      bold + blue + "Formatting Sequences" +
      reset + bold_off + "\n")
print("\\033[39m\\033[49m                 - Reset color")
print("\\033[2K                          - Clear Line")
print("\\033[<L>;<C>H or \\033[<L>;<C>f   - Put the cursor at line L and column C.")
print("\\033[<N>A                        - Move the cursor up N lines")
print("\\033[<N>B                        - Move the cursor down N lines")
print("\\033[<N>C                        - Move the cursor forward N columns")
print("\\033[<N>D                        - Move the cursor backward N columns")
print("\\033[2J                          - Clear the screen, move to (0,0)")
print("\\033[K                           - Erase to end of line")
print("\\033[s                           - Save cursor position")
print("\\033[u                           - Restore cursor position")
print("\\033[1m                          - \033[1mBold on\033[22m")
print("\\033[22m                         - Bold off")
print("\\033[3m                          - \033[3mIralic on\033[23m")
print("\\033[23m                         - Italic off")
print("\\033[4m                          - \033[4mUnderline on\033[24m")
print("\\033[21m                         - \033[21mDouble underline\033[24m")
print("\\033[24m                         - Underline off")
print("\\033[9m                          - \033[9mStrike-through\033[29m")
print("\\033[29m                         - Strike-through off")
print("\\033[5m                          - \033[5mSlow blink on\033[25m")
print("\\033[25m                         - Slow blink off")
print("\\033[11m                         - \033[11mAlternate font 1\033[10m")
print("\\033[12m                         - \033[12mAlternate font 2\033[10m")
print("\\033[13m                         - \033[13mAlternate font 3\033[10m")
print("\\033[14m                         - \033[14mAlternate font 4\033[10m")
print("\\033[15m                         - \033[15mAlternate font 5\033[10m")
print("\\033[16m                         - \033[16mAlternate font 6\033[10m")
print("\\033[17m                         - \033[17mAlternate font 7\033[10m")
print("\\033[18m                         - \033[18mAlternate font 8\033[10m")
print("\\033[19m                         - \033[19mAlternate font 9\033[10m")
print("\\033[10m                         - Regular font")
