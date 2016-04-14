tpl = """
melody = {
  \clef bass
  \key c \major
  \\time 4/4
\set Staff.midiInstrument = #"trombone"
\override Staff.TimeSignature #'transparent = ##t
%s1 \\bar "||"
}
\score {
  \\new Staff \melody
  \layout { }
}
"""
notes = ('40-e,', '41-f,', '42-fis,', '42-ges,', '43-g,',
	'44-gis,', '44-aes,', '45-a,', '46-ais,', '46-bes,',
	'47-b,', '48-c', '49-cis', '49-des', '50-d',
	'51-dis', '51-ees', '52-e', '53-f', '54-fis', '54-ges',
	'55-g', '56-gis', '56-aes', '57-a', '58-ais', '58-bes',
	'59-b', "60-c'", "61-cis'", "61-des'", "62-d'", "63-dis'",
	"63-ees'", "64-e'", "65-f'")
for n in notes:
	__, note = n.split('-')
	ly = tpl % note
	out = open((n+'.ly').replace(',','').replace("'", ''), 'w')
	out.write(ly)
	out.close
