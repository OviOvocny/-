#!/usr/bin/env python3

import argparse
import sys

# ARGS
ap = argparse.ArgumentParser(description="Přeložit C++ na Č++ a naopak")
# positional
ap.add_argument("vstup", help="cesta ke vstupnímu souboru")
ap.add_argument("výstup", default=None, nargs="?", help="cesta k výstupnímu souboru (jinak standardní výstup)")
# optional
ap.add_argument("-č", "--čpp", nargs="?", help="cesta k hlavičce Č++ (jinak očekává č.h zde)")
ap.add_argument("-o", "--obráceně", action="store_true", help="překládat Č++ na C++")
ap.add_argument("-u", "--ukecaný", action="store_true", help="vypisovat detaily o běhu na chybový výstup")

args = ap.parse_args()

# FILE SETUP
try:
  ifile = open(args.vstup, "r")
except FileNotFoundError:
  print(f"Nelze otevřít vstupní soubor {args.vstup}", file=sys.stderr)
  exit(11)

s = args.čpp
if not s:
  s = "č.h"

try:
  cfile = open(s, "r")
except FileNotFoundError:
  print(f"Nelze otevřít hlavičku {s}", file=sys.stderr)
  ifile.close()
  exit(11)

if args.výstup == "stdout":
  args.výstup = None

try:
  ofile = open(args.výstup, "w+")
except TypeError:
  ofile = sys.stdout
except FileNotFoundError:
  print(f"Nelze otevřít výstupní soubor {args.výstup}", file=sys.stderr)
  ifile.close()
  cfile.close()
  exit(12)

# HELPERS
def get_dict ():
  d = {}
  src = 2
  dst = 1
  if args.obráceně:
    src = 1
    dst = 2
  for line in cfile:
    if line.startswith("#define"):
      parts = line.rstrip().split()
      d[parts[src]] = parts[dst]
  vprint(f"Nalezeno {len(d)} definicí")
  return d

def translate (line, d):
  for f_key, f_value in d.items():
    if f_key in line:
      line = line.replace(f_key, f_value)
  return line

def vprint (text):
  if args.ukecaný:
    print(text, file=sys.stderr)

vprint("Vytváření slovníku")
d = get_dict()
vprint("Začíná překlad")
for line in ifile:
  line = translate(line, d)
  ofile.write(line)

# EXITING
vprint("Hotovo!")
ifile.close()
cfile.close()
ofile.close()