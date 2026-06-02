from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'ecommerce.orders',
    bootstrap_servers='localhost:9092',
    group_id='order-analytics-demo',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Consumer Started")
print("Group: order-analytics-demo")
print("-" * 60)

for message in consumer:
    order = message.value

    print(
        f"Partition={message.partition} | "
        f"Offset={message.offset} | "
        f"Order={order['order_id']} | "
        f"User={order['user_id']}"
    )