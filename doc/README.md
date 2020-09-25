The solution is a single player Hang Man game that uses api GET requests to retreive a random word of which the player will be guessing and at the end retrive the definition of the word to show to the player. The purpose is to not only be a form of entertainment but also to increase the users vocabulary and better their spelling.

The application will make a GET request to this API https://random-word-api.herokuapp.com/word?number=1&swear=0 with the parameters of only one word and swear words resticted. With a status code 200 the API will send back a random word in the format of json.

If the api throws an error or fails for any reason the application will get its word by reading a file called 'wordlist.txt' and picking a random word from there using the 'random.choice()' method.

Placeholders will be made (with the '-' symbol) with the length being the length of the word to show the user how many letters the word has.

When the user guesses a letter either one of two things will happen:

    1. The letter guessed will be in the word in which case the place holder of that letter will be replaced with the correct letter
    2. The letter guessed will not be in the word in which case a part of the Hang Man will be drawn on a seperate screen using the 'turtle' python module

In *either* case the letter will be added to a 'tried' list to show the user what they have previously tried that letter.

This prosses will loop through untill the user gets all of the letters correct or the man is complete (which is six incorrect letters) in which the terminal will display either 'YOU WIN !!!' or 'you lose :(' as well as the word if the user loses and a definition of the word if available (*and* if the word was succesfuly retrived by the random word API) by a GET request from this API  https://gad-proxy-prod-leap-2-1.us-east-1.elasticbeanstalk.com:443/api/v2/entries/

Then the user will be asked if they wish to play again if not exits the program with the exit code 0