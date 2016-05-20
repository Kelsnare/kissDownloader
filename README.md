KONICHIWA ANIME FAN TACHI

Kissanime is probably the most used free anime streaming service available right now. This little script lets you download all episodes of an anime series - but obviously a little work is needed from your end as well.

The follwing startup guide is on Ubuntu 14.04. I am pretty sure it will be mostly similar on a macbook. Windows users - well BEST OF LUCK.

1.	Make sure you have python installed. It comes preinstalled with Ubuntu 14.04. I developed this on Python 	 version 2.7.6

2.	You may need to install pip on Ubuntu:

	$sudo apt-get install -y python-pip

	Now install selenium for Python.

	$pip install selenium

	-----------OR-------------

	$sudo pip install selenium

	If permissions are required.

3.	Now the download manager

	$sudo apt-get install -y aria2

===============================================================================

Ok so thats all the setup done.
Now fork the git repo if you want to contribute.

If you just want the download==================

1. Copy the file kissDownloader.py in the directory where you want to download your Anime episodes.

2. Go to the main link of that anime in kissanime.to
   e.g. If you want to download Cowboy Bebop(sub) just search for it in kissanime and copy the url of the main anime page - in this case ------ https://kissanime.to/Anime/Cowboy-Bebop-Sub

3. Most important - you must must have a kissanime account. Remember your Username and Password.

4. Now open up a terminal. Navigate to that folder you want to download the anime to. Remember you have previously copied the kissDownloader.py script file in this directory. If you have not yet do it now. Type the following command
	
	$python kissDownloader.py username password https://kissanime.to/Anime/Cowboy-Bebop-Sub

NB : Please make sure you have Mozilla Firefox installed

===============================================================================

ENJOY!!!