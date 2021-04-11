### ```Project Summary:```

Predict levels of Work-Life Balance based on lifestyle factors, using a dataset of 12,757 survey responses to 23 lifestyle attributes. The actual survey was given by given Authenic-Happiness.come and is linked here:  http://www.authentic-happiness.com/your-life-satisfaction-score


Dataset: https://www.kaggle.com/ydalat/lifestyle-and-wellbeing-data?select=Wellbeing_and_lifestyle_data_Kaggle.csv

#### ```Project Goals:```
- Create a model that will identify drivers of high personal achievement based on lifestyle factors. 
- Create a single notebook with necessary helper functions and instructions that allow a user to reproduce results on their own. 

Trello board:  https://trello.com/b/ebZrkO2D/lifestyle-factors-that-affect-personal-achievement


#### ```Initial Thoughts:```

- expect high correlation with sleep, stress, negative emotions, meditation 
- curious about bmi and achievement
- does high stress = high achievement / can less stress still = high achievement?
- how does female achievement compare to male
- expect higher age to contribute to higher achievement
- possibly drop flow, lost vacation, places visited, fruit_veggies, todo_completed, sufficient income

#### ```Hypotheses:```

H${0}$: There is no relationship between daily stress levels and personal achievement.<br>
H${a}$: There is a dependent relationship between daily stress levels and personal achievement.<br>
H${0}$: There is no relationship between bmi and levels of personal achievement. <br>
H${a}$: There is a dependnt relationship between bmi and levels of personal achievement. <br>
H${0}$: There is no relationship between sleep and levels of personal achievement. <br>
H${a}$: There is a dependent relationship between sleep and levels of personal achievement. <br>

#### ```Data Dictionary:``` 

| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
sleep |typical number of hours of sleep per night over the course of a typical week |float64|
|stress | 0 (not much stress) to 5 (a lot of stress) experienced at work or at home, due to the environment (noise, pollution, insecurity...), co-workers, or because of tragic events such as divorce, job loss, serious illness, loss of family or friends on average over 12 months.|int64|
|recognition| Range of 0-9, or 10 or more significant public recognitions validating a personal level of expertise and engagement (for example: diploma, degree, certificate, accreditation, award, prize, published book, presentation at major conference, medals, cups, titles.)|
|is_female|0 = male, 1 = female |int|
|fruit_veggies|Number of fruits or vegetables eaten daily (0-5)| int64 |
|places visited| How many new places repondants visited in last 12 months (Includes new states, new cities as well as museum, places of interest and parks in your neighborhood.)| int64 |
|core_circle| Number of people respondant has in close circle (0-10) | int64 |
|supporting others|Number of people you help achieve a better life (0-10) |int64 |
|social network |Number of people you interact with daily (0-10)| int64 | 
|bmi|Respondant's body mass in kg divided by the square of height in meters ( 0 = < 25, 1 = > 25 |float64|
|todo_completed| How often do you completed your weekly to do list |float64|
|flow|Hour per day that respondant experienced flow. 'Flow' is defined as the mental state, in which you are fully immersed in performing an activity. You then experience a feeling of energized focus, full involvement, and enjoyment in the process of this activity. ||
|daily_steps|How many steps (in thousands) do you walk in a typical day? (<1 to 10+)||
|life vision|For how many years ahead do you have a clear life vision (0 to 10+)||
|daily_shouting|In a typical week do you shout or sulk at another person or express negative emotions in an active or passive manner. (0 to 10+)||
|donation|Over a period of 12 months, how many times do you donate your time or money to good causes? ||
|sufficient income| Is income sufficient to cover basic life expenses 0 = no/barely 1 = sufficient ||
|time for passion|Daily hours spent doing what you are passionate and dreaming about||
|achievement|Number of remarkable achievements respondent is proud of. (0-10)||
|lost vacation|Hours of vacation NOT taken. ||
|weekly meditation| Number of times respondant meditates, prays or engages in relaxation activities such as walking in a park or lunch breaks each week (0-10)||
| age|Age is binned in years as: < 20, 21 to 35, 36 to 50, 51 or more||
|work_life_balance_score|||


#### ```Instructions for Reproducing My Findings:```

1.  Start by cloning the github repository on your From your terminal command line, enter git clone git@github.com:barbmarques/Lifestyle_Predictors_of_Personal_Achievement.git

2.  Ensure the following files are in your working directory:  
 - Wellbeing.ipynb
 - acquire.py
 - prepare.py
 - explore.py
  
3. Run the Jupyter notebook, Zillow_Regression_Project, cell by cell, to reproduce my analysis.

