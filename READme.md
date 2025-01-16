# Bright Credit Service

A robust Django-based credit service application that enables loan providers to efficiently manage lending operations. The system handles loan disbursement, billing cycles, repayment processing, and comprehensive transaction management.

## Features

### Core Functionality
- User registration with credit score calculation
- Loan application and approval system
- Automated monthly billing with minimum due calculations
- Secure repayment processing
- Detailed transaction history and statements
- Automated periodic tasks via Celery

### Technical Highlights
- Asynchronous credit score calculation using transaction data
- Atomic transactions to prevent race conditions
- Automated billing cycles with daily interest accrual
- RESTful API architecture
- Comprehensive test coverage

## Technology Stack

- **Framework**: Django + Django REST Framework
- **Task Queue**: Celery with Redis broker
- **Database**: SQLite (configurable for PostgreSQL/MySQL)
- **Testing**: Django Test Framework
- **Cache & Message Broker**: Redis
- **Language**: Python 3.x

## Project Structure

```
bright-credit/
├── myproject/             # Django project root
│   ├── settings.py        # Project configuration
│   └── urls.py           # Main URL routing
├── users/                # User management
│   ├── models.py         # User data models
│   ├── views.py         # User-related views
│   ├── serializers.py   # User data serialization
│   └── tasks.py         # User-related Celery tasks
├── loans/                # Loan management
│   ├── models.py         # Loan data models
│   ├── views.py         # Loan processing views
│   └── serializers.py   # Loan data serialization
├── billing/              # Billing operations
│   ├── models.py         # Billing models
│   ├── views.py         # Billing views
│   └── tasks.py         # Billing Celery tasks
└── payments/             # Payment processing
    ├── models.py         # Payment models
    ├── views.py         # Payment views
    └── serializers.py   # Payment serialization
```

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/bright-credit.git
   cd bright-credit
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # or
   venv\Scripts\activate     # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Initialize Database**
   ```bash
   python manage.py migrate
   ```

6. **Start Redis Server**
   ```bash
   redis-server
   ```

7. **Launch Celery Worker**
   ```bash
   celery -A myproject worker --loglevel=info
   ```

8. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

## API Documentation

### User Management

#### Register User
```http
POST /api/users/register-user/
Content-Type: application/json

{
    "name": "John Doe",
    "email": "john@example.com",
    "annual_income": 200000
}
```

#### Apply for Loan
```http
POST /api/loans/apply-loan/
Content-Type: application/json

{
    "user_id": "uuid",
    "amount": 5000,
    "interest_rate": 12,
    "term_period": 6,
    "disbursement_date": "2025-01-01"
}
```

#### Process Payment
```http
POST /api/payments/make-payment/
Content-Type: application/json

{
    "loan_id": "uuid",
    "amount": 1000
}
```

#### Fetch Statement
```http
GET /api/billing/get-statement/?loan_id=uuid
```

## Business Logic

### Credit Score Calculation
- Minimum score for loan approval: 450
- Based on transaction history and income
- Calculated asynchronously via Celery

### Loan Processing
1. User submits loan application
2. System verifies credit score
3. If approved, loan is disbursed
4. EMI schedule is generated

### Billing Cycle
- Monthly billing periods
- Automated minimum due calculation
- Daily interest accrual
- Late payment penalties

