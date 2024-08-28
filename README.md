Five insights

* It seems as if many of these cereals have a surprising amount of sodium. I do not necessarily think "salty" when I think of cereal...
* All of these cereals have a comparable amount of calories and protein, while some cereals can have zero fat sodium or fiber.
* There seem to be negative numbers throughout the dataset that skews the data, this was discussed in class and there wasn't a conclusion as to why. In the case of weight, this is strange since they seem to be all measured with a unit of 1, except for the ones that are -1...
* Sugar is generally the biggest health concern with cereal, and the data seems to say that the amount of sugar is fairly evenly distributed from 0 (or -1...) to 15, with a standard deviation of 4.4. I interpreted this to mean that the amount of sugar in cereal can vary widely by what brand you get.
* Fiber is an interesting statistic to look at. In the percentiles between the minimum and 75%, it seems that the amount of fiber varies from 0 to 3. However, the max seems to be 14. This can be due to the fact that consumers seem to enjoy fiberous cereals and companies like making them, so the cereals specialized for fibers contain a lot of fiber.


Paragraph 1: 
I am not very good at Excel, and I have used the "pandas" library for python, so I just used that. It was actually super easy! Here are the lines of code I used:
```python
    import pandas as pd

    df = pd.read_csv('cereal.csv')
    print(df.describe())
```


Issues: 
Python was actually very easy to use, so I did not have to spend much time to get some worthwhile statistics. However, I did run into some tiny struggles. Namely, the data was a little strange and I think there may be something wrong with it. Another issue I ran into was transfering an excel sheet to a csv to use in this project. 