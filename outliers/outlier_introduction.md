**Outlier Detection**  
Data exploration is the backbone of any machine learning algorithm.
Before jumping into the main task everyone needs to put lots of
effort in data. There is a universal truth that everyone must agree 
"Your Quality of Input Decides the Quality of Output".
So we need to be very very scrupulous before running your algorithm 
on the raw data. This is the reason that people spend 60-70% of there time
on cleaning and preparing the data for there algorithm.
There are several steps that needs to be done to get the dream data for your algorithm.
But here we are going to play with outlier detection and how we can deal with the problem.

For better understanding for anything, the best way is to  ask question and find its answer.  
So,  
**What is outlier**
- Anything that is fluctuating from there usual behaviour.  
- Unusal, Unlike elements, away from the standard, different from normal.  

**Why should i care about outlier**  
You should, if you are dealing with any type of algorithm, you should aware about the outlier within you dataset.
Once a wisest of wise man said, you always understimate the value of salt in presence of some famous spice, but once you missed the salt in your food, all the spices will become tasteless.
That's the power of salt and here outlier detection is a salt for your algorithm. It's presence is not look like that important from top, but deep inside the algorithm, outlier detection will always boost your algorithm.
Enough non-practical explanation, give me a real life example.  
Okay sir,  
Let's say i have a dataset:  
a=[3,6,101,9,4,5]  
b=[3,6,8,9,4,5]  
Now let me calculate a simple mean for the two dataset  
mean of a : 21.33  
mean of b : 5.833  
This is the impact that the OUTLIER  can cause on your data, there is significant difference between the two mean. What i faced as of now in my experiences to detect/predict anything in machine learning 
or any similar kind of stuff,
 we need to set some sort of thresholds, sometimes we set thresholds explicitly or used any library that internally used thresholds to decide/predict.
So let's stand on the fact, we need thresholds.
So the next question, how we decide the thresholds or any library set the thresholds. The aanswer is pretty simple
based on some statictics calculation, like mean,median,mode,variance,standard deviation etc.. that helps to set the thresholds for any algorithm.
And we just see above the example of mean with and without outlier data.
This kind of significant difference in mean(or other stat) pushed the thresholds in un appropriate range just because of few data, that's affecting miserably  by there presence in the data.  


 
**How to check whether my data contain any outlier or not**    
There are several way to check and aplly some filter on your dataset
to find the outlier from your dataset. 
But after applying some technique, i found the best way and less complex is to take help of **boxplot**.  
From this way you will be able to visualize the outlier on your screen and also list down the outlier data.  


**After getting the outlier what should i do**  
There are several ways, depending upon your use cases.
-  Get rid from the outlier by deleting it from the dataset
-  Replace the outlier with some more relevant value, its not a good approach in my point of view, but it also work in some of the scenario.  


**Which language is ideal for detecting outlier**  
There are no hard and fast rule or language barier while detecting outlier. You can go with any language in some language you need to write the logic for detecting outlier in some language they provide some mazic library by which in couple of lines of code you can detect outlier and be a hero.
Don't confuse me !!!
Okay
I find, python worked well.
Go for it.

**There are several algorithm for detecting outlier, which one should i use**
It's damm true!!  
You can pick any algorithm and hang on it should work.  
In my case my first pick was INTERQUARTILE RANGE(IQR).  

**Explainp a bit**
The interquartile range (IQR) is a measure of variability,
 based on dividing a data set into quartiles.  
 Quartiles divide a rank-ordered data set into four equal parts.
  
- The values that divide each part are called the first, second, 
  and third quartiles; 
  - and they are denoted by Q1, Q2, and Q3, respectively.
  - Q1 is the "middle" value in the first half of the rank-ordered data set.
  
  - Q2 is the median value in the set.
  - Q3 is the "middle" value in the second half of the rank-ordered data set.
  - The interquartile range is equal to Q3 minus Q1.

For example, 
- consider the following numbers: 1, 3, 4, 5, 5, 6, 7, 11.
 - Q1 is the middle value in the first half of the data set.
 - Since there are an even number of data points in the first half of the data set, 
  the middle value is the average of the two middle values; that is, Q1 = (3 + 4)/2 or Q1 = 3.5. 
 -  Q3 is the middle value in the second half of the data set. 
 -  Again, since the second half of the data set has an even number of observations, 
  the middle value is the average of the two middle values; that is, Q3 = (6 + 7)/2 or Q3 = 6.5. 
 - The interquartile range is Q3 minus Q1, so IQR = 6.5 - 3.5 = 3.


**Why you pick IQR and what its pros and cons** 
Being a lazy guy you always go for the simplest one, that's the reason for picking up this one. 
- pros : 
    - Main pros of it, it can detect outlier.  
    - You can visualize it using the box plot.
    - it's damm short and essay if you are fighting your battle using python.  
    - It's an unsupervised way.
    - very lightweight.
- Cons :
    - I didn't find yet, might be something would there, as nothing in this world without having a cons in it.  


**For any suggestion, feel free to ping me**  
[linkedin](https://www.linkedin.com/in/vishal-yadav-90231b12a/)  

 




 