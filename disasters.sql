drop table disasters;
drop table temps;

create table disasters(
	year int primary key,
	all_disaster_count int,
	drought_count int,
	earthquake_count int,
	extreme_temp_count int,
	extreme_weather_count int,
	flood_count int,
	impact_count int,
	landslide_count int,
	dry_mass_movement_count int,
	volcanic_count int,
	wildfire_count int,
	all_disaster_cost bigint,
	drought_cost bigint,
	earthquake_cost bigint,
	extreme_temp_cost bigint,
	extreme_weather_cost bigint,
	flood_cost bigint,
	impact_cost bigint,
	landslide_cost bigint,
	dry_mass_movement_cost bigint,
	volcanic_cost bigint,
	wildfire_cost bigint);

create table temps(
	year int primary key,
	avg_temp float);
