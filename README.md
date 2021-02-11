# lat_long_average

This script calculates the average between a list of addresses, cities, etc. using Google's Geocoding API and prints it to stdout.  This script is useful for calculating the most central location among a group of people in geographically separate locations.

## Configuration

1.  Clone the repository
2.  Make sure that you have python3 and pip3 installed.  Run the following code block:
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
3.  In `conf.py`, add your Google API key as a string.  To get a Google API key, see [here](https://developers.google.com/maps/documentation/geocoding/get-api-key)
4.  In loc_list, remove the comment at the top of the file and add your list of locations that you would like to average.  **These should be separated by a newline and enclosed in parenthesis (")**.  For example:
```
"New Haven, Connecticut"
"123 Main Street, Havertown, Pennsylvania"
"Pittsburgh, Pennsylvania"
```

If you would like to save multiple location lists, just change the first parameter in the function call below.

## Running the script
In the command line, run `python location_average.py loc_list`  
The first and only parameter is the file path of the location list you would like to average.

## Results
The results are an average latitude (avg_lat), and average longitude (avg_long), and the most accurate nearby landmark, like a road or a street address.  For example, the output from the loc_list example above is:
```
avg_lat: 40.57508813333333
avg_long: -76.07958316666667
920 Bear Creek Rd, Auburn, PA 17922, USA
```