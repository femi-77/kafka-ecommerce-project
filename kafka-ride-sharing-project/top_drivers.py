from kafka import KafkaConsumer
import json
from collections import defaultdict

consumer = KafkaConsumer(
    'ride.completed',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    consumer_timeout_ms=5000,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

drivers = defaultdict(int)

for message in consumer:
    ride = message.value
    drivers[ride['driver_id']] += 1

print("\nTOP 5 DRIVERS")
print("-" * 30)

top_drivers = sorted(
    drivers.items(),
    key=lambda x: x[1],
    reverse=True
)[:5]

for driver, rides in top_drivers:
    print(f"{driver} -> {rides} completed rides")