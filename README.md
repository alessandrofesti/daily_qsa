Daily quantified self app
================
Alessandro Festi
August 30, 2021

We can understand and improve our flaws as well as we can make them worse.
As human beings we tend to suffer from short term vision and remember better what's closer in time: however that doesn't mean that more recent events are more important than past ones. 

The path is important and imaging a long term and better perspective of ourselves requires visualizing trends of our historical behavior.

The daily quantified self webapp comes in handy to monitor day by day personal KPIs like happiness, healthy routine and adherence to our personal objectives in order to make the historical data of our personal changes visible and straightforward.

The app:
- automatically downloads data from google drive (we must fill daily our custom form with the metrics of interest)
- transforms and creates the necessary KPIs
- builds a local docker container to host the DASH webapp
- updates and runs the image every day through a cronjob

Below a couple of screens from the DASH webapp

<center>
<img src="README_images/qs.png" width="100%" />
</center>
<br/>

<center>
<img src="README_images/qs2.png" width="100%" />
</center>
<br/>
