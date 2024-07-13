#!/usr/bin/python
# -*- coding: utf-8 -*-

# for reference see https://github.com/MakeMagazinDE/Mobi-C/blob/main/src/transformGCODE.ahk
'''
ProcessMillingFunction(fileContent)
{
    ;Start new file with command to switch off LEDs
    newFileContent := "M04`nM09`n"
    PositionFlag := "High" ; Assume starting position is High
    Loop, parse, fileContent, `n, `r
    {
        line := A_LoopField

        ; Delete lines starting with M03, M04, M05, M08, or M09
        if (RegExMatch(line, "^(M03|M04|M05|M08|M09)"))
            continue

        ; Check for G00 lines with Z followed by a number >= 1
        if (SubStr(line, 1, 3) = "G00" && RegExMatch(line, "Z([1-9]\d*)") && PositionFlag = "Low")
        {
            newFileContent .= "M08`nM00`nM09`n"
            PositionFlag := "High"
        }

        ; Check for G0 lines containing "Z-" when PositionFlag is High
        if (SubStr(line, 1, 2) = "G0" && InStr(line, "Z-") && PositionFlag = "High")
        {
            newFileContent .= "M03`nM00`nM04`n"
            PositionFlag := "Low"
        }

        ; Add the current line after any inserted lines
        newFileContent .= line . "`n"
    }
    return newFileContent
}
'''

import sys
import re

gcode_pause = "M00"
gcode_led_green_on = "M03"
gcode_led_green_off = "M04"
gcode_led_red_on = "M08"
gcode_led_red_off = "M09"

#--------------------------------------------
def main(argv):

    if (len(argv) < 2):
        print ("Call: TransformGCode.py <infile> <outfile>")
        exit(1)

    infile_name = argv[0]
    outfile_name = argv[1]

    with open(infile_name, 'r') as infile:
        gcode = infile.read()

    valid_gcode = False
    PositionFlag = "High" # Assume starting position is High

    new_gcode_list = []
    new_gcode_list.append (gcode_led_green_off)
    new_gcode_list.append (gcode_led_red_off)
    for line in gcode.splitlines():

        # Check for G00 lines; if none are found we assume the infile is not a valid gcode file
        if line.startswith('G00'):
            valid_gcode = True

        # Delete lines starting with M03, M04, M05, M08, or M09
        if re.search("^(M03|M04|M05|M08|M09)", line):
            continue

        # Check for G00 lines with Z followed by a number >= 1
        if line.startswith('G00') and re.search("Z([1-9]\d*)", line) and PositionFlag == "Low" :
            new_gcode_list.append (gcode_led_red_on)
            new_gcode_list.append (gcode_pause)
            new_gcode_list.append (gcode_led_red_off)
            PositionFlag = "High"
            continue

        # Check for G0 lines containing "Z-" when PositionFlag is High
        if line.startswith('G0') and re.search("Z-", line) and PositionFlag == "High" :
            new_gcode_list.append (gcode_led_green_on)
            new_gcode_list.append (gcode_pause)
            new_gcode_list.append (gcode_led_green_off)
            PositionFlag = "Low"
            continue

        # Add the current line after any inserted lines
        new_gcode_list.append (line)

    if not valid_gcode:
        print ("Error: no valid G code found in file '%s'!" % (infile_name))
        sys.exit(1)

    # convert list of lines to single string with multiple lines
    new_gcode = '\n'.join(new_gcode_list)

    with open(outfile_name, 'w') as outfile:
        outfile.write(new_gcode)

    print ("File processing complete. New file saved as '%s'" % (outfile_name))
#--------------------------------------------

#--------------------------------------------
if __name__ == "__main__":
    main(sys.argv[1:])
#--------------------------------------------
