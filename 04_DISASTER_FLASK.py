import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, join
from flask import Flask, jsonify
from config import connect_string

# Database Setup
engine = create_engine(f'postgresql://{connect_string}/disaster_db')
Base = automap_base()
Base.prepare(engine, reflect=True)

Factors = Base.classes.factors
Disasters = Base.classes.disasters
Affected = Base.classes.affected

# Flask Setup
app = Flask(__name__)

# Flask Routes

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Route:<br/>"
        f"/api/disasters/years-summary (Shows basic information for all years)<br/>"
        f"/api/disasters/years-details (Shows detailed information for all years)<br/>"
        f"/api/disasters/summary/(year) (Shows detailed information for one year)<br/>"
        f"/api/disasters/details/(year) (Shows detailed information for one year)<br/>"
    )

@app.route("/api/disasters/years-summary")
def summary():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return data for all years"""
    # Query all passengers
    results = session.execute('select factors.year, factors.avg_temp, disasters.all_disaster_count, disasters.all_disaster_cost, affected.deaths from factors join disasters on disasters.year = factors.year join affected on affected.year = disasters.year')

    session.close()

    # Create a dictionary from the output
    output = []
    for year, avg_temp, all_disaster_count, all_disaster_cost, deaths in results:
        year_dict = {}
        year_dict["year"] = year
        year_dict["avg_temp"] = avg_temp
        year_dict["all_disaster_count"] = all_disaster_count
        year_dict["all_disaster_cost"] = all_disaster_cost
        year_dict["deaths"] = deaths
        output.append(year_dict)

    return jsonify(output)

@app.route("/api/disasters/years-details")
def details():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return data for all years"""
    # Query all passengers
    results = session.execute('select disasters.year, disasters.all_disaster_count, disasters.drought_count, disasters.earthquake_count, disasters.extreme_temp_count, disasters.extreme_weather_count, disasters.flood_count, disasters.impact_count, disasters.landslide_count, disasters.dry_mass_movement_count, disasters.volcanic_count, disasters.wildfire_count, disasters.all_disaster_cost, disasters.drought_cost, disasters.earthquake_cost, disasters.extreme_temp_cost, disasters.extreme_weather_cost, disasters.flood_cost, disasters.impact_cost, disasters.landslide_cost, disasters.dry_mass_movement_cost, disasters.volcanic_cost, disasters.wildfire_cost, factors.avg_temp, factors.emissions, affected.deaths, affected.injured, affected.damage, affected.affected, affected.homeless from disasters join factors on disasters.year = factors.year join affected on affected.year = disasters.year')

    session.close()

    # Create a dictionary from the output
    output = []
    for year, all_disaster_count, drought_count, earthquake_count, extreme_temp_count, extreme_weather_count, flood_count, impact_count, landslide_count, dry_mass_movement_count, volcanic_count, wildfire_count, all_disaster_cost, drought_cost, earthquake_cost, extreme_temp_cost, extreme_weather_cost, flood_cost, impact_cost, landslide_cost, dry_mass_movement_cost, volcanic_cost, wildfire_cost, avg_temp, emissions,deaths, injured, damage, affected, homeless in results:
        year_dict = {}
        year_dict['year'] = year
        year_dict['all_disaster_count'] = all_disaster_count
        year_dict['drought_count'] = drought_count
        year_dict['earthquake_count'] = earthquake_count
        year_dict['extreme_temp_count'] = extreme_temp_count
        year_dict['extreme_weather_count'] = extreme_weather_count
        year_dict['flood_count'] = flood_count
        year_dict['impact_count'] = impact_count
        year_dict['landslide_count'] = landslide_count
        year_dict['dry_mass_movement_count'] = dry_mass_movement_count
        year_dict['volcanic_count'] = volcanic_count
        year_dict['wildfire_count'] = wildfire_count
        year_dict['all_disaster_cost'] = all_disaster_cost
        year_dict['drought_cost'] = drought_cost
        year_dict['earthquake_cost'] = earthquake_cost
        year_dict['extreme_temp_cost'] = extreme_temp_cost
        year_dict['extreme_weather_cost'] = extreme_weather_cost
        year_dict['flood_cost'] = flood_cost
        year_dict['impact_cost'] = impact_cost
        year_dict['landslide_cost'] = landslide_cost
        year_dict['dry_mass_movement_cost'] = dry_mass_movement_cost
        year_dict['volcanic_cost'] = volcanic_cost
        year_dict['wildfire_cost'] = wildfire_cost
        year_dict['avg_temp'] = avg_temp
        year_dict['emissions'] = emissions
        year_dict['deaths'] = deaths
        year_dict['injured'] = injured
        year_dict['damage'] = damage
        year_dict['affected'] = affected
        year_dict['homeless'] = homeless
        output.append(year_dict)

    return jsonify(output)

@app.route("/api/disasters/summary/<int:ayear>")
def asummary(ayear):
    pass
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return data for all years"""
    # Query all passengers
    results = session.execute(f'select factors.year, factors.avg_temp, disasters.all_disaster_count, disasters.all_disaster_cost, affected.deaths from factors join disasters on disasters.year = factors.year join affected on affected.year = disasters.year where disasters.year={ayear}')

    session.close()

    # Create a dictionary from the output
    output = []
    for year, avg_temp, all_disaster_count, all_disaster_cost, deaths in results:
        year_dict = {}
        year_dict["year"] = year
        year_dict["avg_temp"] = avg_temp
        year_dict["all_disaster_count"] = all_disaster_count
        year_dict["all_disaster_cost"] = all_disaster_cost
        year_dict["deaths"] = deaths
        output.append(year_dict)

    return jsonify(output)

@app.route("/api/disasters/details/<int:ayear>")
def adetails(ayear):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return data for all years"""
    # Query all passengers
    results = session.execute(f'select disasters.year, disasters.all_disaster_count, disasters.drought_count, disasters.earthquake_count, disasters.extreme_temp_count, disasters.extreme_weather_count, disasters.flood_count, disasters.impact_count, disasters.landslide_count, disasters.dry_mass_movement_count, disasters.volcanic_count, disasters.wildfire_count, disasters.all_disaster_cost, disasters.drought_cost, disasters.earthquake_cost, disasters.extreme_temp_cost, disasters.extreme_weather_cost, disasters.flood_cost, disasters.impact_cost, disasters.landslide_cost, disasters.dry_mass_movement_cost, disasters.volcanic_cost, disasters.wildfire_cost, factors.avg_temp, factors.emissions, affected.deaths, affected.injured, affected.damage, affected.affected, affected.homeless from disasters join factors on disasters.year = factors.year join affected on affected.year = disasters.year where disasters.year = {ayear}')

    session.close()

    # Create a dictionary from the output
    output = []
    for year, all_disaster_count, drought_count, earthquake_count, extreme_temp_count, extreme_weather_count, flood_count, impact_count, landslide_count, dry_mass_movement_count, volcanic_count, wildfire_count, all_disaster_cost, drought_cost, earthquake_cost, extreme_temp_cost, extreme_weather_cost, flood_cost, impact_cost, landslide_cost, dry_mass_movement_cost, volcanic_cost, wildfire_cost, avg_temp, emissions,deaths, injured, damage, affected, homeless in results:
        year_dict = {}
        year_dict['year'] = year
        year_dict['all_disaster_count'] = all_disaster_count
        year_dict['drought_count'] = drought_count
        year_dict['earthquake_count'] = earthquake_count
        year_dict['extreme_temp_count'] = extreme_temp_count
        year_dict['extreme_weather_count'] = extreme_weather_count
        year_dict['flood_count'] = flood_count
        year_dict['impact_count'] = impact_count
        year_dict['landslide_count'] = landslide_count
        year_dict['dry_mass_movement_count'] = dry_mass_movement_count
        year_dict['volcanic_count'] = volcanic_count
        year_dict['wildfire_count'] = wildfire_count
        year_dict['all_disaster_cost'] = all_disaster_cost
        year_dict['drought_cost'] = drought_cost
        year_dict['earthquake_cost'] = earthquake_cost
        year_dict['extreme_temp_cost'] = extreme_temp_cost
        year_dict['extreme_weather_cost'] = extreme_weather_cost
        year_dict['flood_cost'] = flood_cost
        year_dict['impact_cost'] = impact_cost
        year_dict['landslide_cost'] = landslide_cost
        year_dict['dry_mass_movement_cost'] = dry_mass_movement_cost
        year_dict['volcanic_cost'] = volcanic_cost
        year_dict['wildfire_cost'] = wildfire_cost
        year_dict['avg_temp'] = avg_temp
        year_dict['emissions'] = emissions
        year_dict['deaths'] = deaths
        year_dict['injured'] = injured
        year_dict['damage'] = damage
        year_dict['affected'] = affected
        year_dict['homeless'] = homeless
        output.append(year_dict)

    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)