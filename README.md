# SPS Speaker Notes

Script to generate the baseline notes for my notes about the speakers of the
[Swiss Python Summit](https://python-summit.ch)

## Usage

 * Create a new folder for the year:
   ```
   mkdir 2026
   ```
 * Copy the `./create_pdfs.sh` script to it:
   ```
   cp ./create_pdfs.sh 2026
   ```
 * Download the `schedule.json` from pretalx and generate the initial notes:
   ```
   cd 2026
   curl https://talks.python-summit.ch/swiss-python-summit-2026/schedule/export/schedule.json | jq > schedule.json
   python ../parse_schedule.py
   ```
