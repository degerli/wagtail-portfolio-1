# Wagtail Onepage Portfolio Starter

A simple portfolio page made with Wagtail and Bootstrap4. Tried to hardcode as little as possible, almost everything can be added through Wagtail admin. For the sake of keeping it easy for first-timers I just used plain CSS instead of SASS. 

View the demo here: https://rafrasenberg.nl

## Features
- Bootstrap 4
- All content can be adjusted through Wagtail admin, so you can choose your preferred language
- Changeable jQuery (Yes, yes old boring jQuery get over it fancy JS folk) filters through Wagtail admin for portfolio items
- Google Analytics tracking code support


## Prerequisites
Python3 and virtualenv installed on your localmachine or server. There is enough you can find about that on Google.

## To install:

1. Create a virtual env: ```virtualenv -p python3 wagtail-portfolio```
2. Activate virtual env: ```source wagtail-portfolio/bin/activate```
3. Create src folder: ```mkdir src``` and cd into new folder with ```cd src```
4. Use ``` Git clone https://github.com/webconexus/wagtail-portfolio.git ```
5. ```cd wagtail-portfolio``` and use ``` pip install -r requirements.txt ```
6. Use command ``` django m ``` to migrate database. Added django-shortcuts to requirements to make life easier :)
7. Use command ```django csu``` (Create superuser)
8. Now run your server with ```django r```
9. Congratz you have your wagtail-portfolio running!


## NOTE! 
You will get a error when first launching the homepage because your are pulling child items from a parent page onto the homepage (portfolio items) which does not exist yet, so you should first create that parent page in Wagtail admin. Go to localhost:8000/admin, click the Wagtail page explorer and add a 'Projects page' page under your root page (Home). The slug should be portfolio-items, because this is how it is stated in the code. Ofcourse you can change it by yourself. 


## Some tips:
- Personal information, social media links and the counters can be adjusted in Wagtail admin. You will find this in settings --> portfolio settings.
- Portfolio filters can be added through settings --> filters settings. After this you can create a snippet 'Technology' which will be available to you when you add a project, through a checkbox. This will give visitors the option to filter through your projects by category.
- Analytics code can be added through settings --> Google analtyics.
- To add a portfolio item, create a child page (Individual Projects Page) of the parent page (Projects Page), here you can insert project image, link and title. I added some other field but they are not rendered in the template. Feel free to extend it by yourself.

Please feel free to use it. If you run into any issues please feel free to file an issue and I will try to resolve it.
