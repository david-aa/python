#!/usr/bin/env python
import os, sys, subprocess
import os.path

NOTES = {
	40: {
		'name_flat': 'E2',
		'name_sharp': 'E2',
		'position': 7,
		'rect': (11, 5, 27, 235),
	},
	41: {
		'name_flat': 'F2',
		'name_sharp': 'F2',
		'position': 6,
		'rect': (43, 5, 26, 235),
	},
	42: {
		'name_flat': 'Gb2', 
		'name_sharp': 'F#2',
		'position': 5,
	},
	43: {
		'name_flat': 'G2',
		'name_sharp': 'G2',
		'position': 4,
	},
	44: {
		'name_flat': 'Ab2',
		'name_sharp': 'G#2',
		'position': 3,
	},
	45: {
		'name_flat': 'A2',
		'name_sharp': 'A2',
		'position': 2,
	},
	46: {
		'name_flat': 'Bb2',
		'name_sharp': 'A#2',
        'position': 1,
	},
	47: {
		'name_flat': 'B2',
		'name_sharp': 'B2',
		'position': 7,
	},
	48: {
		'name_flat': 'C3',
		'name_sharp': 'C3',
		'position': 6,
	},
	49: {
		'name_flat': 'Db3',
		'name_sharp': 'C#3',
        'position': 5,
	},
	50: {
		'name_flat': 'D3',
		'name_sharp': 'D3',
		'position': 4,
	},
	51: {
		'name_flat': 'Eb3', 
		'name_sharp': 'D#3',
        'position': 3,
	},
	52: {
		'name_flat': 'E3',
		'name_sharp': 'E3',
		'position': 2,
	},
	53: {
		'name_flat': 'F3',
		'name_sharp': 'F3',
		'position': 1,
	},
	54: {
		'name_flat': 'Gb3',
		'name_sharp': 'F#3',
        'position': 5,
	},
	55: {
		'name_flat': 'G3',
		'name_sharp': 'G3',
		'position': 4,
	},
	56: {
		'name_flat': 'Ab3', 
		'name_sharp': 'G#3',
        'position': 3,
	},
	57: {
		'name_flat': 'A3',
		'name_sharp': 'A3',
		'position': 2,
	},
	58: {
		'name_flat': 'Bb3',
		'name_sharp': 'A#3',
        'position': 1,
	},
	59: {
		'name_flat': 'B',
		'name_sharp': 'B',
		'position': 4,
	},
	60: {
		'name_flat': 'C4',
		'name_sharp': 'C4',
		'position': 3,
	},
	61: {
		'name_flat': 'Db4', 
		'name_sharp': 'C#4',
        'position': 2,
	},
	62: {
		'name_flat': 'D4',
		'name_sharp': 'D4',
		'position': 1,
	},
	63: {
		'name_flat': 'Eb4',
		'name_sharp': 'D#4',
        'position': 3,
	},
	64: {
		'name_flat': 'E4',
		'name_sharp': 'E4',
		'position': 2,
	},
	65: {
		'name_flat': 'F4',
		'name_sharp': 'F4',
		'position': 1,
	},	
}

DIR_AUDIO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "res/audio"))
DIR_IMG = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "res/img"))
LIMITS = (40, 65) 

def open_file(filepath):
    # c&p http://stackoverflow.com/questions/434597/open-document-with-default-application-in-python
    if os.name == 'mac' or sys.platform == 'darwin':
        subprocess.call(('open', filepath))
    elif os.name == 'nt':
        os.startfile(filepath)
    elif os.name == 'posix':
        subprocess.call(('xdg-open', filepath))         


if __name__ == '__main__':
	print NOTES, DIR_AUDIO, DIR_IMG
