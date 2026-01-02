---

# Dataset Documentation: Competitive Market Event Dataset

---

## 1. Introduction

This dataset has been constructed to support the empirical analysis of **competitive market behavior between firms offering similar services**. The primary purpose of the dataset is to systematically capture **observable competitive actions**—such as price changes, promotions, service expansions, and strategic initiatives—and to document how rival firms respond to these actions over time.

The dataset enables **event-based analysis of competitive dynamics**, allowing researchers to study response likelihood, response timing, and strategic interaction patterns in oligopolistic and competitive markets. It is designed to support **descriptive analysis, econometric modeling, and comparative strategy evaluation** within the domains of economics, management, and applied engineering analytics.

---

## 2. Dataset Scope and Design Rationale

### Scope

- **Industries covered**:
    
    - Electronics Retail
        
    - Food Service (Quick Service Restaurants)
        
- **Geographic scope**: Japan
    
- **Market structure**: Primarily duopoly / oligopoly
    
- **Time span**: 2018–2024
    
- **Unit of observation**: One competitive market event per row
    

### Design Rationale

The dataset is **event-based rather than transaction-based**, reflecting how competitive strategy is discussed and observed in real-world markets. Each record represents a **clearly identifiable strategic action** initiated by one firm and situated within a competitive context involving at least one rival.

The selected time span captures:

- Pre-COVID competitive behavior
    
- COVID-period strategic adjustments
    
- Post-COVID normalization and digital acceleration
    

Attributes were chosen to reflect **observable and verifiable market behavior** rather than inferred or estimated outcomes, ensuring analytical transparency.

---

## 3. Data Sources and Origin

### Data Origin

The dataset is constructed from **secondary publicly available sources**, including:

- Reputed business newspapers (e.g., Nikkei Asia, Japan Times, Reuters)
    
- Major national newspapers
    
- Financial and industry-focused media outlets
    

### Source Selection Justification

Sources were selected based on:

- Editorial credibility
    
- Verifiability of reported events
    
- Consistent archival availability
    
- Coverage of strategic firm actions rather than opinion
    

### Dataset Type

- **Hybrid dataset**
    
    - Real-world events (dates, firms, actions, sources)
        
    - Structured and standardized into a synthetic analytical format
        

No numerical values were fabricated. Where exact figures were unavailable, **categorical or directional descriptors** were used instead.

---

## 4. Data Extraction and Construction Methodology

### Step 1: Event Identification

- News articles and reports were screened to identify **explicit competitive actions**
    
- Only actions with clear initiating firms and competitive relevance were included
    

### Step 2: Event Filtering

Each event had to satisfy:

- Clear initiating company
    
- Identifiable competing firm(s)
    
- Explicit action type (price, promotion, service, product, digital)
    
- Verifiable publication source and date
    

### Step 3: Attribute Assignment

For each event:

- Firm roles (initiator, responder) were recorded
    
- Action categories were standardized
    
- Industry and country context were assigned
    
- URLs were preserved for traceability
    

### Assumptions Used

- One event represents one strategic decision instance
    
- Competitive relevance is inferred from market overlap
    
- Absence of a reported response is treated as **no immediate response**
    

### Sample Dataset Snippet

|event_id|industry|initiating_company|responding_company|action_type|
|---|---|---|---|---|
|EJP_ELEC_001|Electronics Retail|BIC Camera|Yodobashi Camera|Loyalty incentive|
|JPN_QSR_006|Food Service|Sukiya|Yoshinoya|Price increase|

---

## 5. Dataset Structure and Schema

### Schema Description

|Column Name|Data Type|Description|
|---|---|---|
|event_id|String|Unique event identifier|
|industry|Categorical|Industry classification|
|country|Categorical|Country of occurrence|
|initiating_company|String|Firm initiating action|
|responding_company|String|Competitor(s) affected|
|event_date|Date (YYYY-MM-DD)|Date of action|
|source_name|String|Publication name|
|source_url|String|Source URL|
|action_type|Categorical|Type of competitive action|

### Encoding Notes

- Dates follow ISO format
    
- Action types are text-based categorical labels
    
- No numerical normalization was applied at this stage
    

---

## 6. Data Preprocessing and Cleaning

Preprocessing focused strictly on **data integrity**, not outcome optimization.

### Cleaning Steps

- Removal of duplicate event entries
    
- Standardization of company names
    
- Validation of date formats
    
- Verification of URL presence
    

### Missing Data Handling

- No missing values were imputed
    
- Attributes without reliable information were left blank rather than assumed
    

This approach prioritizes **transparency over completeness**.

---

## 7. Data Quality Assurance and Validation

Quality assurance was ensured through:

- Cross-verification of events across multiple sources where possible
    
- Logical consistency checks (e.g., event dates within scope)
    
- Industry consistency validation for firms
    

The dataset was reviewed to ensure:

- Each event is independently traceable
    
- No conflicting attribute assignments exist
    
- All rows conform to a unified schema
    

---

## 8. Dataset Reliability and Limitations

### Reliability

- High reliability for **event occurrence and timing**
    
- Strong traceability through source URLs
    

### Limitations

- No direct sales, revenue, or demand quantities
    
- Market share changes are not numerically quantified
    
- Consumer behavior is inferred indirectly through strategic actions
    

### Bias Considerations

- Media coverage bias toward large firms
    
- Underreporting of minor or local competitive responses
    

The dataset prioritizes **analytical validity over exhaustive market coverage**.

---

## 9. Reproducibility and Transparency

The dataset is fully reproducible by:

1. Following the documented source selection criteria
    
2. Applying the same event definition rules
    
3. Using identical schema and inclusion constraints
    

All assumptions are explicitly stated, and no hidden transformations are applied.

---

## 10. Conclusion

This dataset provides a **structured, transparent, and reproducible foundation** for analyzing competitive market behavior across multiple firm pairs. Its event-based design reflects real-world strategic decision-making and supports empirical analysis using descriptive statistics, econometric models, and comparative strategy evaluation.

The dataset is well-suited for **economics and management-oriented studies**, enabling systematic examination of competitive responses without reliance on fabricated or unverifiable numerical assumptions.

---

