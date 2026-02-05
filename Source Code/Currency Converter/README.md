# Currency Converter (Financial Engineering & Rate Analysis)

**Authors:**
- [Amey Thakur](https://github.com/Amey-Thakur) ([ORCID: 0000-0001-5644-1575](https://orcid.org/0000-0001-5644-1575))
- [Mega Satish](https://github.com/msatmod) ([ORCID: 0000-0002-1844-9557](https://orcid.org/0000-0002-1844-9557))

**Release Date:** January 9, 2022  
**License:** MIT License

---

## Quick Start
To execute this implementation, install the required dependency and run:
```bash
pip install -r requirements.txt
python CurrencyConverter.py
```

## 1. Definition
A **Currency Converter** is a computational tool designed to determine the relative value of one fiat or digital currency against another based on current market exchange rates. In algorithmic finance, this requires low-latency retrieval of forex data and precise mathematical normalization.

## 2. Technical Explanation
The core of currency conversion lies in the **Cross-Rate Calculation**. If a direct pair (e.g., EUR/JPY) is not available, the system must compute it through a base currency (usually USD):

$$
\text{Rate}_{\text{EUR/JPY}} = \text{Rate}_{\text{EUR/USD}} \times \text{Rate}_{\text{USD/JPY}}
$$

### Data Integrity & Latency
- **Polling Frequency**: Financial services must determine whether to use "Spot Rates" (immediate) or "Historical Rates."
- **Spread Analysis**: The difference between the 'Bid' (buy) and 'Ask' (sell) price, which represents the liquidity cost.

## 3. Computer Science Theory
- **Precision Floating Point**: Financial calculations must avoid binary rounding errors (e.g., $0.1 + 0.2 \neq 0.3$ in standard floats). Professional systems often use the `Decimal` type for arbitrary-precision arithmetic.
- **RESTful API Architecture**: The service implements asynchronous HTTP requests to external financial providers, requiring robust timeout and retry logic.
- **Rate Limiting (Leaky Bucket)**: APIs often enforce quotas to prevent DoS. The converter must handle `429 Too Many Requests` status codes gracefully.

## 4. Python Implementation Logic
- **`CurrencyConverterService`**: An encapsulated service using `requests` for data harvesting and JSON for serialization.
- **Atomic Operations**: Each conversion is treated as an independent transaction, ensuring thread safety and data consistency.
- **Normalization Engine**: Automatically sanitizes user input (casing, spaces) and validates ISO 4217 currency codes.

## 5. Visual Representation

### Financial Exchange Architecture
The analytic engine fetches live forex streams and performs sub-millisecond conversion calculations.

![Currency Converter Demo](Demo.png)

```mermaid
graph TD
    Client["User Input (Amount/Pair)"] --> Service["Converter Service"]
    Service -->|GET Request| API["Forex API Provider"]
    API -->|JSON Rate Stream| Service
    Service --> Logic["Normalization & Precision Math"]
    Logic --> Result["Converted Output"]
    Result --> Log["Forensic Transaction Log"]
```
