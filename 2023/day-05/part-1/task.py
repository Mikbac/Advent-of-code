# cat sample | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2023

def main():
	next_section_counter = 0

	seeds_to_soil = []
	soil_to_fertilizer = []
	fertilizer_to_water = []
	water_to_light = []
	light_to_temperature = []
	temperature_to_humidity = []
	humidity_to_location = []

	locations = []

	seeds = [eval(i) for i in input().strip().split(':')[1].split()]
	input().strip()
	input().strip()
	while True:
		try:
			input_line = input().strip()
			if input_line == '':
				next_section_counter += 1
				input().strip()
			elif next_section_counter == 0:
				seeds_to_soil.append([eval(i) for i in input_line.split()])
			elif next_section_counter == 1:
				soil_to_fertilizer.append([eval(i) for i in input_line.split()])
			elif next_section_counter == 2:
				fertilizer_to_water.append([eval(i) for i in input_line.split()])
			elif next_section_counter == 3:
				water_to_light.append([eval(i) for i in input_line.split()])
			elif next_section_counter == 4:
				light_to_temperature.append([eval(i) for i in input_line.split()])
			elif next_section_counter == 5:
				temperature_to_humidity.append([eval(i) for i in input_line.split()])
			elif next_section_counter == 6:
				humidity_to_location.append([eval(i) for i in input_line.split()])
		except EOFError:
			break

	for seed in seeds:
		soil = find_destination(seed, seeds_to_soil)
		fertilizer=find_destination(soil, soil_to_fertilizer)
		water=find_destination(fertilizer, fertilizer_to_water)
		light=find_destination(water, water_to_light)
		temperature=find_destination(light, light_to_temperature)
		humidity=find_destination(temperature, temperature_to_humidity)
		location=find_destination(humidity, humidity_to_location)
		locations.append(location)

	lowest_location = min(locations)
	print('Answer: {}'.format(lowest_location))


# destination range start, source range start, range length
def find_destination(location, map):
	for i in map:
		if location >= i[1] and location <= i[1] + i[2] - 1:
			return i[0] + (location - i[1])
			break
	return location


if __name__ == "__main__":
	main()
