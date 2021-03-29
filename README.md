Track Side

### Site owners goals:
-	Create a active community, for people with and without experience of track cars, giving them ability to buy uprated products for their vehicle and hobby.
### External Users goals:
-	To be able to easily buy uprated products for their track car
-	The user can create a profile and save their preffered details along with viewing past orders.
### Primary function
A shop, so users can:
-	buy specific uprated products for their car+

### Content culture
Prominently aimed at people with a motoring hobby, people who already spend a lot of time, racing in their own time, or who are looking into doing so.

### Content relevant
It wants to be orientated around cars, mainly track ready cars and what’s the best way to prepare yours to be prepared and safe for a track day.

### Technology appropriate?
-	A shop where customers can purchase product

### Why is it special?
This tends to be a hobby, where people tend to know everything there is about it, or they know barely anything. The shop will let users buy, only the best and tested products for their cars. 

### Why would a user want this site?
A user would want this site, as it’ll be easy to buy the best and already tested products for their cars, the site can become a main source of help them throughout their hobby and supply them with the products that they require.

### Emotional triggers
There is a big a excitement that people experience on track day sessions. An initial buzz, you can smell burning rubber and high octane content in the air, and once you get out on the track ,you just keep on smiling and enjoying yourself as you push yourself and try and better yourself from the previous lap that you’ve just done on the track. The website is wanting to tap into that emotion, giving customers the chance to offer better performance upgrades for their cars, making them handle, grip and perform better on their next track day. 

### Scope
Features:
-	Online store for performance products
-	Social media links

### Priority :
The main aim of the website, is for users to be able to purchase products that they desire for their track car.

### Structure
Theme
The theme is going to aim for Track day sessions, so a darkish black background (for the tarmac) with various banners having white surrounds (road markings), Orange for standout parts, like sales or offers (same colour as the traffic cones along the track side), Red writing – stands out, against the black, but again another colour considered on the track, as it’s seen with the tail lights. This is mainly for the shop. For the forum (TBC, but possibly called Track side forum) to have a green grass and black and white theme, similar colours you’d see pit side, spectating on others on the track, allowing you to talk to other drivers on their experience in the sport.

This is how I originally intended for my website to look:

<img src="/media/Index_home_page.png" alt="Base page" style="max-width:100%;">

In the beginning, I wanted to include various other services within the website, including a forum, in which people could leave reviews on the products, so other users could see, along with renting and buying track cars.

This is how it actually looks: 

<img src="/media/index_page.png" alt="Base page" style="max-width:100%;">


After entering the shop, this is how I wanted it to be:

<img src="/media/Shop_Front.png" alt="Base page" style="max-width:100%;">

I also wanted to include picture links, but after toying with the idea, it wouldn't of worked very well on mobile views, so this is why I went for the menu choice below.

As you can see, this is what I opted for.
<img src="/media/shortened_menu.png" alt="Base page" style="max-width:100%;">


Now, as for the product listings, I did initially want it like this, but it didn't sit right for me as you'd only be able to see so many products at once, where as on the latest product list, you can see up to 4 products at once.

<img src="/media/Specified_car_product_list.png" alt="Base page" style="max-width:100%;">

As you can see, you can easily see 4 products, as well as the start of 4 below, leaving the customer to want to keep scrolling to see the other available products.
<img src="/media/product_lists.png" alt="Base page" style="max-width:100%;">

The actual product detail page didn't vary that much from the initial design, the only thing that wasn't included, was obviously the part about the reviews.

<img src="/media/Specified_car_product_detail.png" alt="Base page" style="max-width:100%;">

Actual:
<img src="/media/product_detail.png" alt="Base page" style="max-width:100%;">


### Features 
Home page - 
On the home page, it includes a few features that are carried out through out all the other pages, as the header and footer is on all the pages.

- header
    - Home button (including the TRACK-SIDE logo)
    - Shop - You can choose the category between different cars to narrow down the specific products
    - Search bar - enabling the user to quickly search for products that are Specified_car_product_list
    - My account - allows users to do the following:
        - Log in / out
        - register for an account
        - click onto their own profile
        ( if a super user)
        - click on product management and add products to the database
    - Shopping bag - takes the users to their shopping bag at any time.
    - Messages appear in the top right, notifying the user of different things happening
<img src="/media/success_message.png" alt="Base page" style="max-width:100%;">

- Body of the index page
    - The home page itself includes a carousel of track cars (that we supply parts for) on the track, so when the customer arrives on the website straight away, they already know they're in the right place, when looking for performance parts.

- footer
 - Gives the user the ability to click on the social media accounts and follow them


Other features when viewing products
    - Can click on the menu on home page and take them to products directly listed with the vehicle they're after
 This is how every normal user sees products listed:

<img src="/media/normal_user.png" alt="Base page" style="max-width:100%;">

This is how super user sees products listed:

<img src="/media/super_user.png" alt="Base page" style="max-width:100%;">

This makes it easier for Super users to quickly sope through and modify or delete specific products when required.

Product detail page features:
    - The customer gets a description of the product, along with a price and a rating,
    - If wanted, the customer can click onto the picture to get a bigger view of the product Specified_car_product_list
    - The customer can click and add the product on view into their shopping bag, or click Keep shopping

Shopping bag features
    - features include a list of products added to bag
    - ability to adjust quantity and remove products if required
    - return shopping
    - Carry on to a secure check out to purchase the products

Checkout features
    - This lets the customer fill in their details for the order,
    - gives them a final view of the products they're ordering
    - If the customer is logged in with their account, their details can be saved on their account as default for the next purchase by clicking the specified tick box
    - Allows anonymous customers to buy products without creating an account
    - Gives the customers a secure payment via Stripe

Checkout Success features
    - Once the payment has gone through, it takes the customer through to this page
    - This page shows the customer a summary of their order, including where it'll be posted to and which email the confirmation email has been sent to.

### Technologies used
To start with, I've used the basic HTML, css to create the foundations of the site and edit it to my design

I've just Javascript and JQuery, to implement things like:
- drop down menu from the header
-the dropdown boxes for the forms
-validate forms, like signup login
-it allowed us to build a base page, in which all of the other pages extended from it, making it easier to have pages for products, without having to make individual pages for each product, we can just create a template and load in the relevant data required.

Bootstrap
- Used bootstrap to give the page a responsive design and help with the layout

Stripe 
- to be able to successfully take payments from customers

Python
- was used to build the applications themselves, to make the website funciton

### Testing 
When testing the website, a lot of it was done whilst in development
- for example, when writing the code for the webhook handlers, you have to make the various faults occur, to see if the handlers report the fault like a non payment to you

One of the biggest worrys, is that the site may let any normal user, that might now the url, to add, edit or even delete products from the database, 

When on super user, you can edit products like so (also note the easy url to get to edit)

<img src="/media/super_edit_view.png" alt="Base page" style="max-width:100%;">

When logged in as a normal user an entering the same url as above :

<img src="/media/normal_user.png" alt="Base page" style="max-width:100%;">

The normal user is unable to add, edit or delete products, due to the restrictions put in place.

All of the coding used on this project has been tested, and ensures everything is working as it should be, allowing it to work on the following browsers:
  - Google Chrome
  - Opera
  - Microsoft Edge
  - Mozilla Firefox


Credits
Content, the content used in the products, is from partly being made up by me, or from vairous sites like https://www.sico-developments.co.uk/

The media
the media used, the pictures of products were taken from Google images, the Index background photo, was taken by myself, the photos for the carousel, were taken from a track day i went on, the photo's are uploaded online on https://www.flickr.com/photos/javelintrackdays/albums/72157716162637626/

Acknowledgements
The idea from this project, is from going on previous track day sessions with friends, its always a struggle to find good reliable products, that aren't going to let you down when really needed.

### Deployment
Do to the site being a python application, it won't run on GitHub alone, so the python app itself, is deployed via Heroku. The website is designed with github, and linked and pushed up to Heroku. But with the website having images on, the images are stored on the AWS service, letting the public view all of the images uploaded.

The Config vars Have their own specific requirements which are stored on herkou, so it knows how it needs to run the application, including the Secret key, ass it's a database, so not everyone should have access to the database itself.

### Given more time
I don't want to make this into a sob story, I've been struggling with working full time (all the way through this covid outbreak), I've got a 18 month hold, currently tearing my house to bits, and also supporting my wife who's working on the front line as a nurse, So I haven't had as much time as I'd of liked to dedicate myself to this project.

My initial idea was to include a forum within the site, so that users could actually write up their own reviews on the products, to let other users how they've genuinley got on with the product, whether it was good or bad.

My other idea, was to have the ability to be able to offer a service to rent out the track car to customers that wanted to try out a track day, before commiting to the hobby fully, also with an option to buy fully prepped cars themselves.

Links
The link to the deployed app on Heroku is http://track-side.herokuapp.com/

The link for the git hub repositories is https://github.com/Blakeman260/track-side