#!/usr/bin/bash

rm -f speaker-notes-day1-morning.pdf
rm -f speaker-notes-day1-afternoon.pdf

rm -f speaker-notes-day2-morning.pdf
rm -f speaker-notes-day2-afternoon.pdf

for file in ./day-[12]/*.md; do
    echo $file
    # pandoc -V geometry:margin=2cm --from gfm --to pdf "$file" -o "${file%.*}.pdf"
done

pdftk ./day-1/speaker-notes-[1-5].pdf cat output speaker-notes-day1-morning.pdf
pdftk ./day-1/speaker-notes-[6-8].pdf cat output speaker-notes-day1-afternoon.pdf

pdftk ./day-2/speaker-notes-[1-5].pdf cat output speaker-notes-day2-morning.pdf
pdftk ./day-2/speaker-notes-[6-8].pdf cat output speaker-notes-day2-afternoon.pdf

