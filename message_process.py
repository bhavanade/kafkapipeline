from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:29092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

for message in consumer:
    data = message.value
    # Process data (e.g., filter, transform)
    processed_data = {
        'user_id': data['user_id'],
        'locale': data['locale'],
        'timestamp': data['timestamp']
    }
    producer.send('processed-login', value=processed_data)
    print(f"Sent: {processed_data}")
