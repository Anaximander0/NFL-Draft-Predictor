# NFL-Draft-Predictor
Machine Learning project, using python, pandas, and scikit-learn that predicts the first round of the 2026 NFL draft based on historical draft data. 
-----
The RandomForest model is trained on historical draft prospect data from the past decade (2015-2025 NFL Drafts). The training data includes combine measurements (Height, Weight, 40-Yd Dash, Bench Press, Shuttle, 3 cone, Long jump, Vertical jump, and more) along with prospects' collegiate statistics (Recieving, Passing, Rushing, Defensive stats all included). The Random Forest Regression model determines the relationship between these data points and where they were drafted in their respective class (1-32 for first round picks). This way, it learns what elite prospects looked like before they played in the NFL. 

Then, to predict the 2026 NFL draft, it was given ESPN's top 100 prospects for this years draft, along with the same measurements included previously (combine measurements, collegiate statistics, etc.). 
Each team picking in the first round of this years draft was given positions of need to target (Determined mainly by me, but also using PFF grades)

Lastly, a loop iterates through each slot, 1-32, and assigns the team the best graded player (who either fits a positional need, or is the best player available by a wide margin). The final results were printed and are shown below. 

The data for players was from Kaggle, CFBstats.com, NFL.com, and ESPN
To compile the data, I made a few parsers and mergers 

Data/ - includes CSV data training files for the ML
Merge/ - includes mergers to combine all of the many data CSV files together with combine information
Stats Parsers/ - includes data parsers which turned TXT files into readable CSV files
txtdatastats/ - includes all the raw txt data files which were parsed and turned into CSV files

--ML Draft Simulation--

Raiders-1-Fernando Mendoza-QB

Jets-2-David Bailey-EDGE

Cardinals-3-Arvell Reese-EDGE

Titans-4-Makai Lemon-WR

Giants-5-Caleb Downs-S

Browns-6-Monroe Freeling-LT

Commanders-7-Akheem Mesidor-EDGE

Saints-8-Caleb Banks-DT

Chiefs-9-Mansoor Delane-CB

Bengals-10-T.J. Parker-EDGE

Dolphins-11-Max Iheanachor-OT

Cowboys-12-Avieon Terrell-CB

Rams-13-Caleb Lomu-OT

Ravens-14-Carnell Tate-WR

Buccaneers-15-KC Concepcion-WR

Jets-16-Cashius Howell-EDGE

Lions-17-Spencer Fano-OT

Vikings-18-Christen Miller-DT

Panthers-19-Kenyon Sadiq-TE

Cowboys-20-Jermod McCoy-CB

Steelers-21-Ty Simpson-QB

Chargers-22-Omar Cooper-WR

Eagles-23-Blake Miller-RT

Browns-24-Olaivavega Ioane-OG

Bears-25-Brandon Cisse-S

Bills-26-Anthony Hill-ILB

49ers-27-Ted Hurst-WR

Texans-28-Kadyn Proctor-OT

Chiefs-29-Malachi Fields-WR

Dolphins-30-Logan Jones-OT

Patriots-31-Emmanuel Pregnon-OT

Seahawks-32-Jeremiyah Love-RB

--ML Draft Simulation--


