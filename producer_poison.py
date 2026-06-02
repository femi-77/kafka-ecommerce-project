from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092'
)

producer.send(
    'ecommerce.orders',
    value=b'{invalid_json'
)

producer.flush()

print("Poison Message Sent!")