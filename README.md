# End-to-End Data Engineering & Infrastructure Project

## Overview

This project demonstrates a complete end-to-end data engineering pipeline consisting of:

- A FastAPI-based mock market data API
- A Python ETL pipeline
- PostgreSQL database storage
- Docker containerization and orchestration

The system simulates real-time financial market data ingestion, validation, transformation, anomaly detection, and storage.

---

# Architecture

```text
FastAPI API
     ↓
ETL Pipeline
     ↓
PostgreSQL
```

All services are containerized using Docker and orchestrated with Docker Compose.

---

# Technologies Used

- Python 3.13
- FastAPI
- PostgreSQL
- Pydantic
- Docker
- Docker Compose
- psycopg2
- Requests

---

# Project Structure

```text
DataEngineeringAssignment/
│
├── api/
│   ├── app/
│   ├── Dockerfile
│   └── requirements.txt
│
├── etl/
│   ├── app/
│   ├── Dockerfile
│   └── requirements.txt
│
├── docker-compose.yml
├── .env
└── README.md
```

---

# Features

## API Layer

- Real-time synthetic market data generation
- Fault injection for resilience testing
- Random malformed data responses
- Random HTTP 500 errors

### Endpoint

```http
GET /v1/market-data
```

---

# ETL Pipeline Features

## Extraction

- Polls market data API
- Handles API failures and timeouts

## Validation

- Pydantic schema validation
- Invalid records separated safely

## Transformation

### VWAP Calculation

Volume Weighted Average Price is calculated per instrument.

### Outlier Detection

Records are flagged when price deviates more than 15% from average batch price.

## Loading

- Valid records inserted into PostgreSQL
- Duplicate prevention using:
  - instrument_id
  - timestamp unique constraint

## Logging

The pipeline logs:
- Records processed
- Records dropped
- Execution time
- Outlier count

---

# Database Schema

```sql
CREATE TABLE market_data (

    id SERIAL PRIMARY KEY,

    instrument_id VARCHAR(50) NOT NULL,

    price DOUBLE PRECISION NOT NULL,

    volume DOUBLE PRECISION NOT NULL,

    timestamp TIMESTAMP WITH TIME ZONE NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE (instrument_id, timestamp)
);
```

---

# Setup Instructions

## Prerequisites

- Docker Desktop
- Git

---

# Running the Project

From the project root directory:

```bash
docker compose up --build
```

---

# API Access

Swagger UI:

```text
http://localhost:8000/docs
```

---

# Environment Variables

Environment variables are stored in `.env`

```env
POSTGRES_DB=market_data_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_PORT=5432
```

---

# Docker Services

## API Service
- FastAPI application

## DB Service
- PostgreSQL database

## ETL Service
- Data extraction and processing pipeline

---

# Scaling Strategy

If the system needed to handle 1 billion events per day:

## Recommended Architecture

- Kafka for distributed streaming ingestion
- Apache Spark for distributed processing
- Airflow for orchestration
- Kubernetes for container orchestration
- Cloud object storage (S3/ADLS/GCS)
- Distributed OLAP systems like ClickHouse or BigQuery

## Benefits

- Horizontal scalability
- Fault tolerance
- Parallel processing
- High throughput ingestion

---

# Monitoring Strategy

Production monitoring could include:

- Docker health checks
- Prometheus metrics
- Grafana dashboards
- Centralized logging
- Alerting systems
- API uptime monitoring

Health checks would validate:
- API availability
- ETL execution status
- Database connectivity

---

# Recovery & Idempotency

To ensure idempotency and avoid duplicate processing:

- Database unique constraints prevent duplicate inserts
- Failed transactions are rolled back
- ETL validates data before insertion
- Batch processing can be checkpointed
- Retry mechanisms can be added for transient failures

This ensures partial failures do not corrupt downstream systems.

---

# Assignment Requirements Covered

- FastAPI API
- Fault injection
- ETL pipeline
- Schema validation
- VWAP calculation
- Outlier detection
- PostgreSQL storage
- Duplicate prevention
- Structured logging
- Docker containerization
- Docker Compose orchestration
- Secret management using `.env`

---

# Author

Ashish Kumar