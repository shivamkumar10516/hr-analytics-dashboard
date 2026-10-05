# Corporate HR Insights Platform

A production-grade workforce analytics portal built to monitor key performance indicators (KPIs), analyze departmental attrition trends, and manage operational employee records dynamically. This application decouples business logic from presentation components to ensure scalability and maintainability.

## Architectural Overview

The application follows a modular architecture separating data ingestion, computational logic, and UI rendering layers:

*   **Data Layer:** Simulates realistic corporate structures using demographic and financial parameters.
*   **Business Logic Layer:** Isolates workforce calculations (attrition ratios, average experience profiles, and salary brackets) from framework dependencies.
*   **Presentation Layer:** Overrides default styles using targeted CSS overrides for an executive dashboard interface.

---

## Features

### Executive Metrics Grid
*   **Total Workforce Count:** Real-time visibility into overall headcount.
*   **Organizational Attrition Rate:** Live percentage calculations reflecting current turnover.
*   **Financial Allocations:** High-precision average salary trackers.
*   **Tenure Mapping:** Metric summaries tracking average organizational experience.

### Advanced Data Controls
*   **Dynamic Subsetting:** Multi-select sidebar controls to filter metrics and workforce rosters instantly by operational department.
*   **Production-Ready Data Grid:** Interactive table views supporting manual column resizing, custom hiding, global column sorting, and programmatic data exports.
*   **Native Theming Support:** Complete layout flexibility matching user-agent preferences (Light, Dark, and System configurations).

---

## Directory Structure

```text
hr-analytics-dashboard/
├── data/
│   └── mock_data_generator.py  # Simulation engine for generating balanced HR telemetry
├── src/
│   ├── metrics.py              # Stateless core business logic & KPI arithmetic
│   └── ui_components.py        # Tailored DOM element layouts and custom CSS injections
├── .gitignore                  # Development environment system rule file
├── app.py                      # Application bootstrap script and routing logic
└── README.md                   # Operational architecture documentation
```

---

## Installation & Setup

### Prerequisites
Ensure your local environment runs **Python 3.9+** and has `pip` configured.

### 1. Clone & Initialize the Project Workspace
Navigate to your target workspace folder and structure the project directories:
```bash
git clone <repository-url>
cd hr-analytics-dashboard
```

### 2. Dependency Management
Install the core application frameworks directly via python package manager:
```bash
pip install streamlit pandas numpy
```

### 3. Launching the Application
Execute the bootstrap script via your environment terminal. Streamlit will initiate a local web server (typically bound to `localhost:8501`):
```bash
streamlit run app.py
```

---

## Technical Specifications & Implementations

*   **State Optimization:** Leverages Streamlit cache mechanisms (`@st.cache_data`) to prevent expensive dataset regeneration on user interactions or filter swaps.
*   **Presentation Layer Styling:** Bypasses boilerplate component styles using isolated `st.markdown()` styling sheets to achieve a customized executive design language.
*   **Fault-Tolerant Computations:** Core functions isolate calculation exceptions gracefully, protecting dashboard runtime from bad array inputs.
