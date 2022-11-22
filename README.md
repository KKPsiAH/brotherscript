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
