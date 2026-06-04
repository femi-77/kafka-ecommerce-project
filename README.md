# Apache Kafka Projects

This repository contains two Apache Kafka projects developed using Python and Docker to demonstrate real-time event streaming, consumer groups, partition rebalancing, and event-driven processing.

## Technologies Used

* Apache Kafka
* Python
* kafka-python
* Docker

---

# Project 1: E-Commerce Event Processing

A Kafka-based order processing system demonstrating core Kafka concepts.

### Features

* Producer & Consumer
* Consumer Groups
* Partition Rebalancing
* Poison Message Handling

### Topic

```text
ecommerce.orders
```

### Workflow

```text
orders.csv
    ↓
Producer
    ↓
ecommerce.orders
    ↓
Consumers
```

### Screenshots

#### Topic Description

![Topic Description](kafka-ecommerce-project/topicdesc.png)

#### Producer Output

![Producer Output](kafka-ecommerce-project/producerop.png)

#### Consumer Output

![Consumer Output](kafka-ecommerce-project/consumerop.png)

#### Partition Rebalancing

![Consumer Rebalance 1](kafka-ecommerce-project/consumerrebalance1.png)

![Consumer Rebalance 2](kafka-ecommerce-project/consumerrebalance2.png)

#### Poison Message Handling

![Poison Message](kafka-ecommerce-project/poisonconsumer.png)

---

# Project 2: Ride Sharing Event Pipeline

A Kafka-based ride sharing system that processes ride events and generates driver analytics.

### Features

* Ride Event Producer
* Completed Ride Filtering
* Driver Earnings Calculation
* Top Drivers Reporting

### Topics

```text
ride.events
ride.completed
driver.earnings
```

### Architecture

![Architecture Diagram](kafka-ride-sharing-project/architecture.drawio.png)

### Workflow

```text
rides.csv
    ↓
Ride Producer
    ↓
ride.events
    ↓
Completed Ride Consumer
    ↓
ride.completed
    ↓
Driver Earnings Consumer
    ↓
driver.earnings
    ↓
Top Drivers CLI
```

### Screenshots

#### Ride Producer

![Ride Producer](kafka-ride-sharing-project/riderproducer.png)

#### Completed Ride Consumer

![Completed Ride Consumer](kafka-ride-sharing-project/riderconsumer.png)

#### Driver Earnings

![Driver Earnings](kafka-ride-sharing-project/riderearnings.png)

#### Top Drivers

![Top Drivers](kafka-ride-sharing-project/topdrivers.png)

---

# Learning Outcomes

* Kafka Producers & Consumers
* Kafka Topics & Partitions
* Consumer Groups
* Partition Rebalancing
* Event Filtering
* Event-Driven Architecture
* Real-Time Data Processing

---

# Author

**Femi Sunil**
