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

--Draft Simulation Results--

Raiders-1-Fernando Mendoza-QB
Jets-2-David Bailey-EDGE
Cardinals-3-Arvell Reese-EDGE
Titans-4-Makai Lemon-WR
Giants-5-Caleb Downs-S
Browns-6-Denzel Boston-WR
Commanders-7-T.J. Parker-EDGE
Saints-8-Caleb Banks-DT
Chiefs-9-Mansoor Delane-CB
Giants-10-Omar Cooper-WR
Dolphins-11-Max Iheanachor-OT
Cowboys-12-Chris Johnson-CB
Rams-13-Blake Miller-OG
Ravens-14-Olaivavega Ioane-OG
Buccaneers-15-Carnell Tate-WR
Jets-16-Keldric Faulk-EDGE
Lions-17-Monroe Freeling-OT
Vikings-18-Christen Miller-DT
Panthers-19-Kenyon Sadiq-TE
Cowboys-20-Daylen Everette-CB
Steelers-21-Ty Simpson-QB
Chargers-22-Chase Bisontis-OG
Eagles-23-Spencer Fano-OT
Browns-24-KC Concepcion-WR
Bears-25-Brandon Cisse-S
Bills-26-CJ Allen-ILB
49ers-27-Jordyn Tyson-WR
Texans-28-Caleb Lomu-OT
Chiefs-29-Keionte Scott-CB
Dolphins-30-Kadyn Proctor-OT
Patriots-31-Ted Hurst-WR
Seahawks-32-Jermod McCoy-CB

--Draft Simulation Results--


