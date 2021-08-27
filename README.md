# DEK23_BTC
Cryptotrading and holding calculator. 

DEK23_BTC by Deckcard23
------------------------
If you need calculate your cryptotrading or hodling movements in a period of time (a year, a moth, etc) that´s your tool.
DEK23_BTC is a python3 script that work like a CLI in Kali Linux (perhaps it works in Ubuntu).
That´s script is a ALFA version and need to get better, use it with caution.

INSTALLATION
------------
You must install Python3 version 3.9.1+
You must install Pandas library:
      python -m pip install --upgrade pip
      pip3 install pandas
      
RUNNING
-------
If you put in terminal Linux the next order then will be appear the HELP information: 

      python3 DEK23_BTC_declaration.py -h

Usage: python3 DEK23_BTC_declaration.py [OPTION] [FILE]
Concatenate FILE to standard output.


-h, --help              This help menu
-e, --exchange          Select the crypto exchange
                                binance
                                bitstamp
-o, --output            Name of file to save information
Examples:
        python3 DEK23_BTC_declaration.py -e binance file.csv -o output_file.txt
        
IMPORTANT: the exchange file must be in CSV format.

EXCHANGES
---------
That BETA version only is available BINANCE exchange. BITSTAMP works bad with problems.



ABOUT FILES
-----------
DEK_23_declaration.py ---> main script
checker.py --> check the lines of CSV and tell you if pandas has read all the lines.
check.log --> log created by checker.py


