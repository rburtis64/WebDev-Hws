# HW03


CS 421/621 Adv Web App Development
Summer 2019

Homework 3                                                       Due Date: 7/16/2019 11:59PM
Implementation of Poker API
Submission:
•	Submit a link of the forked project in canvas.

If you have followed the previous chapters properly, you should be able to build a poker API that will accept poker hands and return the type of hand (e.g., a pair, a full house). It would be interesting to add code to your Express server that stores the result of every hand and their type in Redis or Mongo. In other words, make it in such a way that your app keeps a track of every valid hand that is posted to your API along with the result. Don’t track the items that result in an error. If you do that, you can set up a get route that responds with a JSON object that includes all the posted hands. You may even want to make it so the get route returns only the five most recent hands. You want to make this example interesting by finding a library of playing card images and have your client show images of the cards in the posted hand instead of the JSON objects or a text description. The library comes in multiple parts. You can either just use the playingCard.js library, which has no UI rendering (just creates deck objects with the standard methods) or you can add on the playingCards.ui.js library, which adds the ability to render the cards to the page.
[Note: This library was just something that you can build for the sake of proving out that a deck of cards could be implemented in JavaScript and CSS. There is no real-world use-case for it. Additionally, you can add methods for managing hands/players, which is not part of the existing library.] 
To do this, you can create an images subdirectory in the client part of your application and store the images there.
You can search the internet for sample examples of Poker API but please make sure you follow UAB Academic code of Honesty. 

