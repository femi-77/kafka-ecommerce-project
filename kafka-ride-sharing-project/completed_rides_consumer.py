from kafka import KafkaConsumer, KafkaProducer
import json

consumer = KafkaConsumer(
    'ride.events',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("Listening for ride events...")

for message in consumer:
    ride = message.value

    if ride['status'] == 'COMPLETED':
        producer.send('ride.completed', value=ride)

        print(
            f"Completed Ride Forwarded: "
            f"{ride['ride_id']} Driver={ride['driver_id']}"
        )

        producer.flush()