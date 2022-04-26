# Questions for Couples

## What it is
A simple web based game that gives couples, friends, or partners questions to ask each other. Players can choose between three levels of 'deepness' and get a new question at the click of a button. You can view the live app [here](https://questions-for-couples.herokuapp.com/chill/).

## Why I built it
Many times sitting around with my girlfriend, or friends, we've tried to come up with interesting questions to ask each other. There are a few apps you can buy in the app store to help with this, [this](https://www.nytimes.com/2015/01/09/style/no-37-big-wedding-or-small.html) classic but short NYT article, and a great card game that we own. But, at least by our judgement, there's no good websites for this. So I built a web app that we could use. 

## Features
The app is a very simple interface. Users can choose a level: chill, deep, deeper, or any. They then press the 'new question' button to be fed questions at that level. 

## Technologies
- Django app with a PostgreSQL database.
- [htmx](https://htmx.org/) allows users to generate a new question without a page reload
- HTML, CSS, Bootstrap frontend
- Deployed on Heroku 

## Future work
There are a number of small things I want to improve on this app
- The UI for level selection is clunky
- Right now, the 'New Question' button grabs a random question at that level. Because the total number of questions for any level isn't that high, a user will see a lot of repeats. Instead, it should go sequentially though questions. To improve experience, it could also load all questions for the level in memory when the level is selected. And then show them in random order, but keep track of what has been previously seen as to avoid duplicates.
- I need to add a lot more questions (turns out a lot of building products is grunt work).

## Lessons and reflections
I jumped into this project right after doing a few projects with structured with a seperate React frontend and Django Rest backend. I had learned how that could be a powerful combo. This project taught me when it is unneccesary. 

I first built this as a React app with a Django backend. I originally wanted to do so for the single page functionality. However, a batch-mate of mine at Recurse Center introduced me to htmx, which would allow me to get SPA like functionality within a a monolithich Django app. I ended up rebuilding the app that way which had a few benefits:
* It drastically reduced the total size of the app.
* It minimized complexity.
* Server side rendering would improve SEO if I ever choose to get users for this project.


While the app was pretty simple to build, it taught me to think about various ways I might approach an application's architecture up front. It also showed me that there may be a variety of ways to do something that you typically associate with one technology (i.e. not needing React for SPA behavior).
