"""
A simple module to colorize text in the terminal.

This module provides a simple way to colorize text in the terminal.
"""

# see also: http://misc.flogisoft.com/bash/tip_colors_and_formatting


from typing import Optional

RESET = 0
BLACK = 30
RED = 31
GREEN = 32
BROWN = 33
BLUE = 34
PURPLE = 35
CYAN = 36
LIGHT_GRAY = 37
_OTHER = 38
DEFAULT = 39
DARK_GRAY = 90
LIGHT_RED = 91
LIGHT_GREEN = 92
YELLOW = 93
LIGHT_BLUE = 94
LIGHT_PURPLE = 95
LIGHT_CYAN = 96
WHITE = 97

BOLD = 1
DIM = 2  # not working on Konsole
UNDERLINE = 4
BLINK = 5  # not working on Konsole and gnome Terminal
INVERSE = 7
HIDDEN = 8  # not working on Konsole

_ESC = "\033"
_ESC = "\x1b"
_BACKGROUND = 10
_RESET_EFFECT = 20


def colorize(
    text: str,
    color: Optional[int] = None,
    background: Optional[int] = None,
    effects: Optional[list[int]] = None,
    color_256: Optional[int] = None,
    background_256: Optional[int] = None,
    with_end: bool = True,
) -> str:
    """
    Colorize a text.

    Arguments:
    ---------
    text: the text to be colorize
    color: the text color code
    background: the background color code
    effects: the effect code (BOLD, DIM, UNDERLINE, BLINK, INVERSE, HIDDEN)
    color_256: The 256 text color code, use print_colors to get the possible values
    background_256: The 256 background color code, use print_colors to get the possible values
    with_end: Set to False to don't add the end tag

    """
    if effects is None:
        effects = []
    start = []
    end = []

    if color is not None:
        start.append(color)
        end.append(DEFAULT)
    elif color_256 is not None:
        start += [_OTHER, 5, color_256]
        end.append(DEFAULT)

    if background is not None:
        start.append(background + _BACKGROUND)
        end.append(DEFAULT + _BACKGROUND)
    elif background_256 is not None:
        start += [_OTHER + _BACKGROUND, 5, background_256]
        end.append(DEFAULT + _BACKGROUND)

    for effect in effects:
        start.append(effect)
        end.append(effect + _RESET_EFFECT)

    start_code = f"{_ESC}[{';'.join([str(s) for s in start])}m" if text != "" else ""
    end_code = f"{_ESC}[{';'.join([str(e) for e in end])}m" if with_end else ""
    return f"{start_code}{text}{end_code}"


def print_colors() -> None:
    """Print a small help with all the color."""
    color_pivot = [0]
    color_pivot += [e * 6 + 16 for e in range(37)]
    color_pivot.append(256)
    color_pivot_start = color_pivot[:-1]
    color_pivot_end = color_pivot[1:]
    color_table_list = [range(cs, ce) for cs, ce in zip(color_pivot_start, color_pivot_end)]

    for color_table in color_table_list:
        text = ""
        for color in color_table:
            color_string = str(color)
            padding = "".join([" " for e in range(3 - len(color_string))])
            text += colorize(f" {padding}{color_string} ", background_256=color, with_end=False)
        print(text + colorize("", background=DEFAULT))


if __name__ == "__main__":
    print_colors()
