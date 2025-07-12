*** Settings ***
Library    LocationSimulate.simulate

*** Keywords ***
test 
    Intermediate Points    sourceLat    sourceLon    desLat    desLon    speedIn Km/hr
    
    