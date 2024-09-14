#list comprehension
#dictionary comprehension

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split(" ")}
print(result["What"])

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:(weather_c[f"{day}"]*9/5)+32 for day in weather_c}

print(weather_f)


weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
 
weather_f = {day:temp * 9/5 + 32 for (day, temp) in weather_c.items()}
 
print(weather_f)