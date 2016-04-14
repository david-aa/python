#!/bin/bash
python __lytpls.py
for l in *ly; do
	lilypond --png "$l"
	PNG=`echo $l | tr ".ly" ".pn"`g
	convert -crop 125x110+90+30 "$PNG" "$PNG"
done
rm -f *ps
rm -f *ly
