# Python

My solutions to [Project Euler](https://projecteuler.net/) written in Python will be here.

## Progress

![4 problems solved in Pyhton language out of 761](https://progress-bar.dev/4/?scale=761&title=solved&width=761&suffix=/761)

## Thoughts and References for each Problem

001. 
002. 
003. 
004. __Largest palindrome product:__ 

My first idea was to write two nested loops: the outer one starting in 999 and breaking when its iterator squared were least than the stored largest palindrome product; the inner loop should start at the current value of the outer one and test whether the product (with the value of the outer one) were the a palindrome and largest than the then-stored one. Additionally the inner loop would test whether its calculated product were least than the then-largest and break if it were. It would probably be enough for the corresponding code to run in under 1-minute.

But I found a [solution](https://adamdrake.com/an-unreasonably-deep-dive-into-project-euler-problem-4.html) that made me tweak some details. I haven't applied all optimizations because it's almost 3 AM and I wanted to solve a little more general version of the problem (n-digits) so I couldn't get the multiples of 11 thing to work. Other than that the blog post reminded me to check for short circuit in the `if` statement conditions and to write the `is_palindrome` function without converting my number to a string, reversing it and checking the equality.

In my laptop it ran just fine for 2, 3 and 4 digits, lagged a little for 5 and 6, and I gave up of waiting for the answer for 7 digits - which I would probably be able to get with the multiples of 11 thing.