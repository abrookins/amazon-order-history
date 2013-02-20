This script parses a CSV file containing your order history on Amazon.com, and loads it into `Order` and `Item` objects.

Currently it only gives you a) a breakdown of expenditures per category and b) total money spent at Amazon.com in your lifetime, but that'll be improved. Feel free to send pull requests!

# Obtaining your Amazon history

On your Amazon.com account page, click "Download order reports":

![](http://i.imgur.com/gvC8iMo.png)

Fill the form out to get the interval desired. I personally like getting everything; for that, you'd set the start date as January 1st of whatever earlier year it gives you, and then click "Use today" for the end date. Keep "Items" selected as the report type.

![](http://i.imgur.com/a021LU9.png)

Click "Request report"; it'll take Amazon some time to process, and then you'll get a link by email to download your report.

Place it in the same folder as this script, rename it to `amazon.csv`, and you can run the script!
