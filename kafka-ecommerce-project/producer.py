from kafka import KafkaProducer
import csv
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    key_serializer=lambda k: k.encode('utf-8'),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

with open('data/orders.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        producer.send(
            'ecommerce.orders',
            key=row['order_id'],
            value=row
        )

        print(f"Sent: {row['order_id']}")

producer.flush()
print("All messages sent successfully!")