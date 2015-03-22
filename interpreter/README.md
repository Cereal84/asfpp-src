Description
============
This tool is something like an interpreter, it allows the user/s to write attacks description using the language
 available for ASF++ and furnish is XML representation that is understandable by ASF++.


Requirements
============

argparse library.

It is, also, necessary to have PLY (Python Lex-Yacc) created by David Beazley, you can download it from 
his personal [page] (http://www.dabeaz.com/ply/) or from his [Github page](https://github.com/dabeaz/ply).

Usage
=====

	$ python interpreter.py -o <file_output> -i <file_input>

Produce the XML attack configuration file for Castalia, according to the attack description in the input file.


Example
-------

	$ python interpreter.py -o output.xml -i description

Authors
=======
+ Alessandro Pischedda	alessandro.pischedda@gmail.com
+ Marco Tiloca		marco.tiloca84@gmail.com
+ Francesco Racciati  racciati.francesco@gmail.com 

