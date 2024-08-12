<h1>A simple scraping tool template I created</h1>

<p>Had a client approach me who needed to collect and organize almost 5000 entries on a certain platform they were using and wanted to save these entries somewhere so they could stop using the service. They gave me their access credentials to the platform and just said "please figure it out".</p>

<p>Service provider didn't have the option to download their entries however, which is a scummy move if you ask me, trying to keep you tied to them by holding your clients' info hostage essentially. So I got to work.</p>

<p>Manually typing every single entry would be nigh impossible due to the sheer volume of information, every client had multiple properties attached to them, not to mention there were almost 5000 of them, so I started studying how that platform API worked,
and how could I take advantage of it, with a simple scraping script like this one I managed to collect every single one of the entries in just a few seconds, add in a little more time to properly filter, parse and convert the JSON file this script creates and
I had a proper spreadsheet for my client in less than an hour. </p>

<h2>Considerations</h2>

<ul>
  <li>This script is a simple template, if you want it to work for you, you'll need to edit it to suit your needs (auth tokens, pagination options, etc)</li>
  <li>Scraping itself is not an illegal activity, but like any other technology, it can be used for bad things, please don't do that</li>
  <li>This was the very first scraper script I made myself from scratch instead of using other sollutions from way more experienced people than me, so there's definitely room for improvement, but this one worked fine for me at the time</li>
  <li>I left out the filtering and formatting functions I used for my client because I believe those are better off coded in-house, so they can suit whatever you need them to better</li>
</ul>


