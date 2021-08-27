# DEK23_BTC
Cryptotrading and holding calculator. 

DEK23_BTC by Deckcard23
------------------------
If you need calculate your cryptotrading or hodling movements in a period of time (a year, a moth, etc) that´s your tool.
DEK23_BTC is a python3 script that work like a CLI in Kali Linux (perhaps it works in Ubuntu).
That´s script is a ALFA version and need to get better, use it with caution.
The script is in spanish.

COLLABORATORS
-------------
If you are interesting in become collaborator in this project then contact to me.

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
        
IMPORTANT: the exchange file must be in CSV format and you must DELETE the first empty file.

EXCHANGES
---------
That Bversion only is available BINANCE exchange. BITSTAMP works bad with problems.

BINANCE CSV FORMAT
------------------
You must get a CSV crypto movements from BINANCE and remember delete the first empty file.
In the first file must appear: UTC TIME - ACCOUNT - OPERATION - COIN - CHANGE - REMARK

The scripts only support:
- Type ACCOUNT: Spot.
- OPERATIONS: Sell, Buy, Fee, Withdraw, Commission History, Distribution, Deposit, Small assets exchange BNB, Transaction Related, Savings purchase, Savings Interest, Savings Principal redemption.
- COINS: ALL types. 

ABOUT FILES
-----------
DEK_23_declaration.py ---> main script.

checker.py --> check the lines of CSV and tell you if pandas has read all the lines.

check.log --> log created by checker.py

EXAMPLE
-------
To run the example CSV put the next:

                  python3 DEK23_BTC_declaration.py -e binance binance_example.csv -o declaracion.txt 

1. Appear the number of files inside the CSV file: 198 (write it down or remember that number)
2. Put the start date (you can see the CSV file)
3. Put the end date (you can see the CSV file)
4. The script start to work (in the screen will appeared all the information)
5. When script end to analyze with PANDAS then start checker.py: You must put 198 when question "Indique el numero de lineas analizar"
6. Then checker say you if all the lines are ok or if any line has been jumped.
7. Now you have the file declaration.txt in the folder with all the information.
