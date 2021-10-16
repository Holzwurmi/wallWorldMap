#!/usr/bin/env python3

import argparse
from pprint import pformat
import json
import textwrap

def main():
    print(textwrap.dedent('''
        Currently only a stump:
        creating physical map described in README.md via not completly satisfying map under
        [https://upload.wikimedia.org/wikipedia/commons/f/fd/Blank_map_of_the_world_%28Robinson_projection%29_%2810E%29.svg]
        because of one month deadline
        '''))
    return 0

    webResources = {
        "svg tutorial": "https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial",
    }
    parser = argparse.ArgumentParser(
        description=
            'Creates an svg from geographic coordinate system data via a supported projection',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='"Web-Resources": {0}'.
            format(json.dumps(webResources, indent=4))
    )
    # parser.add_argument('--projection', help='projection / mapping used to convert geographic coordinate system (GCS) data to a 2d projection of the world', )
    # parser.add_argument('inputData')
    # parser.add_argument('resolution')
    # parser.add_argument('output')
    # parser.add_argument('include countryBorders, rivers, countryStates')
    # parser.add_argument('colors countryBorders, rivers, countryStates')
    parser.parse_args()
