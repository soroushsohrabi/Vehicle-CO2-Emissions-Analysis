# Vehicle CO2 Emissions Analysis

I put this little project together to see what’s really going on with car CO2 emissions.  
The data’s from 2014, and it includes details like engine size, how many cylinders a car’s got, miles per gallon, and so on.  
I ran some Pearson correlation calculations, and now I’ve also added a simple linear regression to predict emissions from engine size.  
If you’re into cars or the environment (or both), you might find the patterns interesting.

## Why I Made This

I’ve always been curious—do bigger engines really pump out more CO2? What about fuel efficiency?  
So I grabbed a dataset, wrote a script, and let the math speak for itself.  
Originally it was just about spotting trends, but now it can also make predictions using a regression line.

## About the Data

The file’s called `FuelConsumption.csv` and here’s what’s inside:
- **ENGINESIZE** – engine capacity in liters.
- **CYLINDERS** – the number of cylinders in the engine.
- **FUELCONSUMPTION_COMB_MPG** – combined city/highway MPG.
- **CO2EMISSIONS** – grams of CO2 per kilometer.

It covers 1,067 vehicles—everything from small hatchbacks to big SUVs.

## What You’ll Need

Not much, really:
- **Python 3** (I used 3.8, but anything newer should work fine).
- No fancy libraries—just Python’s built‑in `csv`.

To install Python:
```bash
# Linux (Ubuntu/Debian)
sudo apt-get install python3
# Or just grab it from python.org for Mac/Windows
```

Make sure the CSV file is in the same folder as the script.

## How to Run It

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/car-emissions-data.git
   cd car-emissions-data
   ```

2. Put `FuelConsumption.csv` in there.

3. Run it:
   ```bash
   python3 Vehicle_CO2_Correlation.py
   ```

You’ll get correlation results and a regression equation.

## How It Works

The script (`Vehicle_CO2_Correlation.py`) does a few simple things:
- Reads the CSV into lists.
- Calculates averages, variance, standard deviation, covariance, and Pearson correlation.
- Runs **`linear_regression(x, y)`** to find the best-fit line between two variables.  
  This gives you a slope and intercept so you can predict CO2 from engine size.

Example bit from the code:
```python
slope, intercept = linear_regression(Enginsize, CO2EMISSIONS)
print(f"Engine Size to CO2 Correlation: {corr(Enginsize, CO2EMISSIONS):.3f}")
print(f"Linear Regression: CO2 = {slope:.2f} * EngineSize + {intercept:.2f}")
```

## Example Output

```
Engine Size to CO2 Correlation: 0.874
Cylinders to CO2 Correlation: 0.850
MPG to CO2 Correlation: -0.906
Linear Regression: CO2 = 39.48 * EngineSize + 187.65
```

What it means:
- Bigger engines and more cylinders usually mean more CO2.
- Higher MPG means less CO2 (negative correlation).
- The regression line lets you plug in an engine size and get an estimated CO2 value.

## Limitations

- The data has to be clean—no missing values or weird entries.
- It only looks at three factors: engine size, cylinders, and MPG.  
  Things like fuel type, car weight, or aerodynamics aren’t included.
- Both correlation and regression assume linear relationships.

## Contributing

If you’ve got ideas or improvements:
1. Fork the repo.
2. Create a branch (`git checkout -b my-change`).
3. Commit (`git commit -m "Added X feature"`).
4. Push and open a pull request.

## License

MIT License – do whatever you want with it, just keep this notice.

```text
MIT License

Copyright (c) 2025 Soroush Sohrabi

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be included in all copies
or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.
```
