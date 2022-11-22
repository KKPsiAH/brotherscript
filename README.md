# brotherscript
A Python script that uses Airium to generate HTML code for the [Alpha Eta website](https://github.com/KKPsiAH/website).

## Prerequisites
Requires [```Pip```](https://pypi.org/project/pip/) and [```Airium```](https://pypi.org/project/airium/)


In your Python environment, [install Pip](https://pip.pypa.io/en/stable/installation/).

Then, install Airium by typing into the commandline: ```pip install airium```


## Usage
1. Edit/update the CSV file that you're trying to generate HTML for (either ```active.csv```, ```conditionals.csv```, or ```officers.csv```)

2. In the directory with the script and csv file, run the script depending on which you're updating (```python active_brotherscript.py```, ```python conditional_brotherscript.py```, or ```python officer_brotherscript.py```)

3. If the CSV files are valid and everything worked correctly, an HTML file is generated under the name of ```generated_active.html```, ```generated_conditional.html```, or ```generated_officers.html```, and then you would copy and paste the contents of that file into the corresponding section in the HTML file of the website.

## Structure of each of the CSV files
### ```active.csv``` and ```conditionals.csv```
Name|Pronouns|Initiation Semester|Hometown|Instrument|Majors|Minors (if not applicable, type N/A)

### ```officers.csv```
Name|Pronouns|Officer Position|Officer Email|Initiation Semester|Major|Instrument|Quote about brotherhood (if not applicable, type N/A)

## A note about ```officer_brotherscript.py```
Currently, Alpha Eta has 8 Elected Officer positions and 8 Appointed Officer positions, and it is hardcoded to reflect those values through lines 33 and 34:
```
num_elected = 8
num_appointed = 8
```

If these numbers change through the creation or removal of officer positions, you can change those variables and it will work as intended. But, ```officers.csv``` must be set-up in the order that you would like for it to appear on the website.

## A note about pictures
Your machine may have a case-insensitive system, but HTML is a case-sensitive language, so in order for images to be displayed correctly, they must be named with the right casing, as in ```First_Last.JPG```. The pictures also must be 1000 x 1333 pixels for uniformity and decent image quality.

## A note to future Webmasters
Keep the CSV files updated every semester! And if you feel like this can be improved in any way, use your best judgment, don't break anything, and as always, test your code before you push it.