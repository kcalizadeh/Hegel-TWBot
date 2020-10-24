This is a bot for generating tweets taken at random from sentences in Hegel's corpus. Currently the books that have been digested by the bot are:
- the three-volume set containing his lectures on the history of philosophy
- the Encyclopedia Logic 
- Philosophy of Nature
- the four-volume set containing his lectures on Fine Art
- the Science of Logic
- the Elements of Right
- the Philosophy of Spirit

Unfortunately, the Phenomenology of Spirit, one of his most famous works, was difficult to find a format that could be converted. So it is not on the list. Also, while the csv contains quotes from all these texts, the actual code to retrieve the quotes from the last 4 on this list was deleted due to a save-work error. At this time there are nearly 38000 tweetable quotes on the list.

There is a csv that holds all the quotes. Two notebooks are used - one cleans Project Gutenberg's .txt versions of Hegel's works, and the other sends the tweets themselves. The tweeter notebook has an option to preview tweets. If you find one that is formatted poorly despite the cleaning, you can remove it from the master sheet. If you like it, run another cell to send. A separate .py file is included that simply sends the tweets directly.

There also a sheet which contains the quote list from the original Hegel Bot.

