"""
Create a function get_product_id that:

Takes a product page URL string from our online shop.
Returns the product ID.
Each URL follows this format:

Domain exampleshop.com
Product name, separated by dashes (-).
Letter p indicating the start of the product ID
Actual product ID (unlimited length)
8-digit date when the product was added, followed by .html
Notes:

The product name can contain the letter p or digits.
Return the product ID as a string.
All URLs are valid and follow the given structure.
Examples:

get_product_id("exampleshop.com/fancy-coffee-cup-p-90764-12052019.html") == "90764"
get_product_id("exampleshop.com/dry-water-just-add-water-to-get-water-p-147-24122017.html") == "147"
get_product_id("exampleshop.com/public-toilet-proximity-radar-p-942312798-01012020.html"
"""

def get_product_id(url: str) -> str:
    strurl = (url.split("-")
    product_id = strurl[-2]
    return(product_id)


get_product_id("exampleshop.com/fancy-coffee-cup-p-90764-12052019.html") # == "90764"
get_product_id("exampleshop.com/dry-water-just-add-water-to-get-water-p-147-24122017.html") #== "147"
get_product_id("exampleshop.com/public-toilet-proximity-radar-p-942312798-01012020.html")

