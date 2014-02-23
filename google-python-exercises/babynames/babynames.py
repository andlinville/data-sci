#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """

  # read and print file
  docstring = ""
  doclist = []
  with open(filename, 'r') as file:
    for line in file:
      docstring = docstring + line
      doclist.append(line)

  name_list = []
  # find year and add it to the result list
  year_match = re.search(r'Popularity in (\d\d\d\d)', docstring)
  if year_match:
    year = year_match.group(1)
    name_list.append(year)
  else:
    print 'no match found'

  # get names and ranks and print
  name_dict = {}
  for line in doclist:
    name_match = re.search(r'<td\b[^>]*>(\d+)</td><td\b[^>]*>(\w+)</td><td\b[^>]*>(\w+)</td>', line)
    if name_match:
      rank, male, female = name_match.group(1), name_match.group(2), name_match.group(3)
      name_dict[male] = rank
      name_dict[female] = rank

  # build names list
  keys = sorted(name_dict.keys())
  for k in keys:
    name_list.append(k + ' ' + str(name_dict[k]))

  print str(filename) + ' complete'
  return name_list


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for a in args:
    list = extract_names(a)
    if summary:
      with open(a + '.summary', 'w') as output:
        for l in list:
          output.write(str(l) + '\n')
      output.close()
    else:
      for n in list: 
        print n
  
if __name__ == '__main__':
  main()
