"""Color Palettes

Some sample color palettes for the various attractors. These can be customised.
Note that each color palette is a dictionary where the value is a color and the
key is the percentile rank (of frequencies in the histogram) at which that
color will occur. Colors between these pre-defined colors are linearly
interpolated with respect to the percentile rank.

If you customise the palettes or make your own, it is useful to note that the
percentile rank 0 corresponds to a frequency of zero (the minimum frequency)
and a percentile rank of 100 corresponds to the maximum frequency achieved in
the histogram. Percentile ranks can be floats. You can use the same color for
multiple percentile ranks, but preferably don't reuse the same percentile rank
in the same palette.
"""

D3 = {
    0: "060036",    # dark blue
    55: "002572",   # dark blue
    85: "AE0000",   # red
    92: "FF6F00",   # orange
    99: "FFFF5E",   # yellow
    100: "FFFFFF",  # white
}

D6 = {
    0: "FFFFFF",    # white
    20: "FFFFFF",   # white
    65: "ff80ff",   # light pink
    85: "8066ff",   # light purple
    95: "0041c5",   # dark blue
    98: "4c0076",   # dark purple
    100: "000000",  # black
}

D19 = {
    0: "FFFFFF",    # white
    35: "FFFF5E",   # yellow
    60: "FF6F00",   # orange
    85: "AE0000",   # red
    91: "8211A7",   # light purple
    96: "38004A",   # dark purple
    100: "060036",  # dark blue
}

D23 = {
    0: "FFFFFF",    # white
    70: "F5ECF5",   # very light purple
    85: "D0D1E6",   # light purple
    95: "DF4949",   # light red
    97: "AE0000",   # red
    98: "396707",   # green
    100: "014636",  # dark green
}

Z3 = {
    0: "FFFFFF",    # white
    70: "F5ECF5",   # very light purple
    91: "D0D1E6",   # light purple
    97: "63A7CD",   # light blue
    98: "0F96B1",   # teal
    100: "014636",  # dark green
}

Z4 = {
    0: "000000",    # black
    50: "001600",   # very dark green
    65: "003b00",   # dark green
    85: "008f11",   # light green
    98: "00ff41",   # very light green
    100: "82ffa2",  # almost white
}

Z5 = {
    0: "FFFFFF",    # white
    30: "fbfcbf",   # light yellow
    85: "feaa74",   # peach
    97: "ec585f",   # light red
    99: "be2dad",   # purple
    99.8: "261157", # dark purple
    100: "000000",  # black
}
