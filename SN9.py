## Author DrFargo
## Created: 2021-02-07
## Latest update: 2021-02-10
 
from src.base import starshipSimulation as SS

g = 9.81 #m/s2 Gravity of Earth
mass_lox = 30e3 #Liquid oxygen
Raptor = 3 # 1 Raptor Engine = 2.3 meganewton
 
Sim = SS()
Sim.Render('SN9')