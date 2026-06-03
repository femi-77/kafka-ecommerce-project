from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'ride.completed',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

earnings = {}
rides = {}

print("Driver Earnings Calculator Started")
print("-" * 50)

for message in consumer:
    ride = message.value

    driver_id = ride['driver_id']

    rides[driver_id] = rides.get(driver_id, 0) + 1
    earnings[driver_id] = earnings.get(driver_id, 0) + 5

    print(f"Driver: {driver_id}")
    print(f"Completed Rides: {rides[driver_id]}")
    print(f"Earnings: ${earnings[driver_id]}")
    print("-" * 50)