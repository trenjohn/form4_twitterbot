<h4>Form 4 Twitterbot</h4>
---
This library consists of 3 Python scripts written to extract insider transactions from the SEC EDGAR database as reported on SEC Form 4, convert recent transactions into tweets, and tweet them. The respective files performing these functions are *edgar_scrape.py*,   *twitter_status_generation.py*, and *twitter_post.py*, respectively. More detail on the .json files required for input and created as output from these scripts is explained in the sections that follow.

<h6>Required Libraries</h6>
In addition to Python 2.7, these scripts require the following python libraries be installed:

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
* [twitter 1.17.1](https://pypi.python.org/pypi/twitter/1.17.1)

<h6>edgar_scrape.py</h6>

This file requires a .json file *"CIK_list.json"*  (included in this library) formatted as in the following example:

*{"Company": "Apple", "Ticker": "AAPL", "CIK": "0000320193"}*

The company CIK is appended to the EDGAR database URL string, the URL requested, parsed with Beautiful Soup, and results meeting criteria of an insider purchase or sale are written to an output .json file *"edgar.json"*.

<h6>twitter_status_generation.py</h6>

This file opens *"edgar.json"* and converts the raw scraped data into tweets. The output file is *"status_updates.json"*.

<h6>twitter_post.py</h6>

Lastly, this file opens *"status_updates.json"* and uses the python twitter library to tweet each of the insider transactions.
