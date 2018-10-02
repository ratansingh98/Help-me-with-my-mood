# Help Me With My Mood

## Overview
Help Me With My Mood is application built using python and machine learning. It uses tweepy api which extract all the public tweets within timespan of 1 day and perform sentiment analyisis on it for the provided given username. Then based upon their emotion plays a song from soundcloud.

<ul>
<li>Ideation document : 
  <a href="https://docs.google.com/document/d/1QCQYZgRZxLHXSDS4FzBCd9FQCTYXklwgQol_-VUpiG8/edit">Open</a></li>
<li>Presentation Slides : <a href="https://docs.google.com/presentation/d/1O8lbF-uZxerNmsc-Nj5M1ZgxqpLyurYscAtIO0VPzjU/edit?usp=sharing">Open</a></li>
  <li>Watch the demo <a href="https://youtu.be/7IAx-mlBLK0">Watch</a></li>
</ul>

## Key Value Proposition
<ol>
  <li>Songs play automatically just after typing username.</li>
  <li>Used Machine learning model to classify current emotion of user.</li>
  <li>Highly Scalable.</li>
</ol>  

## To run

<b>1. To install all necessary libraries</b>
``$ pip install -r requirements.txt`` or ``$ pip3 install -r requirements.txt``

<b>2. Setup selenium driver for chrome</b>
You need to download suitable driver for your chrome from [Here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Then

<b><i>For ubuntu:</i></b>

``sudo mv chromedriver /usr/bin/chromedriver``

``sudo chown root:root /usr/bin/chromedriver``

``sudo chmod +x /usr/bin/chromedriver``

<b><i>For windows:</i></b>
Just execute chromedriver.exe

<b><i>For windows:</i></b>
Follow the instruction [here](https://www.kenst.com/2015/03/installing-chromedriver-on-mac-osx/)

<b>3. Execute application</b>
``python main.py``

## Hardware Requirements
<ul>
  <li>Processor with 2 cores or higher.</li>
  <li>Minimum of 8GB RAM.</li>
</ul>
