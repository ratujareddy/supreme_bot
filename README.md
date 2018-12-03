# supreme_bot
Bot to scrape this website https://www.supremenewyork.com/


## Overview

This is a scraper built in Python using Beautiful Soup and Requests to scrape the [supreme clothing website](https://www.supremenewyork.com/) and automatically purhcase items in less than 3 seconds based on inputted keywords. 

This allowed a user to purchase items for the inital price every Thursday morning when new items were released before they were sold out. Many items sold out with in 10 seconds.

This tool was in use between July 2016 and June 2017 before the website began using image recognition to proceed to checkout -- maybe a future project!



## How this works

In the file `SupremeMain.py`, I've created a list of products I would like to attempt to purhcase. The list contains products of the class `product`, which is defined in `productClass.py`. The bot will iterate through the list in order of priority and search for the product by the name and keywords entered. It will be able to match substrings of the product if you do not know the entire name. You can input any number of sizes and colors and it will select the first available one, again in priority by the order in the list. If you set the parameter `any_color` to `True`, *if* the bot is not able to find the desired colors you have denoted, it will select the first one it finds. 


## Overview of the code

`SupremeFunctions.py`: in the works
`getLink.py`: in the works
`productClass.py`: in the works
`SupremeMain.py`: in the works



