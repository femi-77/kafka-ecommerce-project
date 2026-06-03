from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'ecommerce.orders',
    bootstrap_servers='localhost:9092',
    group_id='order-analytics',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

user_count = {}

print("Consumer Started...\n")

for message in consumer:
    order = message.value
    user_id = order["user_id"]

    user_count[user_id] = user_count.get(user_id, 0) + 1

    print("Received:", order)
    print("Orders per User:", user_count)
    print("-" * 50) 