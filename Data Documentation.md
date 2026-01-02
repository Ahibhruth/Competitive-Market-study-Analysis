
# Dataset Documentation

**Competitive Market Event Dataset (Japan: Electronics Retail & Food Service)**

---

## 1. Introduction

This dataset documents **competitive market events** between firms offering similar services within the same industry. Each record represents a **single, verifiable strategic action** initiated by one firm and observed within a competitive context involving one or more rival firms.

The dataset is designed to support **economics and management-oriented empirical analysis**, particularly in the areas of **oligopolistic competition, strategic interaction, and competitive response behavior**. Rather than capturing transactional or customer-level data, the dataset focuses on **observable firm-level actions**, which are the primary signals through which competitive strategy is publicly revealed.

---

## 2. Dataset Scope and Design Rationale

### Scope

- **Industries included**:
    
    - Electronics Retail
        
    - Food Service (Quick Service Restaurants)
        
- **Geographic scope**: Japan
    
- **Time coverage**: 2018–2024
    
- **Unit of observation**: One competitive market event per row
    
- **Total events**: Structured across multiple competing firm pairs
    

### Design Rationale

Competitive behavior in real markets is often **event-driven**, such as:

- price reductions
    
- promotional campaigns
    
- service expansions
    
- digital initiatives
    
- product or menu changes
    

Accordingly, the dataset is **event-based**, allowing each row to represent a discrete strategic action. This design aligns with how competitive interactions are reported in practice and analyzed in **industrial organization and strategic management research**.

The selected time period captures:

- pre-pandemic competition
    
- COVID-era strategic adjustments
    
- post-pandemic normalization and digitalization
    

---

## 3. Data Sources and Origin

### Source Type

The dataset is constructed from **credible secondary data sources**, including:

- National and international business newspapers
    
- Financial and industry-focused media outlets
    

Examples of source publications include:

- Nikkei Asia
    
- Japan Times
    
- Reuters
    
- Mainichi
    
- Financial Times
    

### Source Selection Criteria

Sources were selected based on:

- verifiability of reported events
    
- consistency in publication archives
    
- focus on factual reporting of firm actions
    

### Dataset Classification

- **Hybrid dataset**
    
    - Real-world events (firms, dates, actions, sources)
        
    - Structured into a standardized analytical format
        

No numerical values were fabricated or inferred beyond what was explicitly reported.

---

## 4. Data Extraction and Construction Methodology

### Step-by-Step Construction

#### Step 1: Event Identification

Public news articles were screened to identify **explicit competitive actions**, such as:

- price changes
    
- promotions
    
- service or delivery expansions
    
- digital or loyalty initiatives
    
- product or menu introductions
    

#### Step 2: Event Qualification

An event was included only if:

- the initiating firm was clearly identified
    
- at least one competing firm operated in the same market
    
- the action had strategic or competitive relevance
    
- the event date and source were verifiable
    

#### Step 3: Attribute Assignment

For each qualifying event:

- the initiating firm and responding firm(s) were recorded
    
- the industry and country context were assigned
    
- the action type was standardized into a controlled vocabulary
    
- the source name and URL were preserved for traceability
    

#### Assumptions

- One event represents one strategic decision instance
    
- Competitive relevance is inferred from market overlap
    
- Absence of reported response implies no immediate observable response
    

---

## 5. Dataset Structure and Schema

### Schema Overview

|Column Name|Data Type|Description|
|---|---|---|
|`event_id`|String|Unique identifier for each competitive event|
|`industry`|Categorical|Industry classification (e.g., Electronics Retail, Food Service)|
|`country`|Categorical|Country where the event occurred|
|`initiating_company`|String|Firm initiating the strategic action|
|`responding_company`|String|Competing firm(s) affected by the action|
|`event_date`|Date (YYYY-MM-DD)|Date of the reported event|
|`source_name`|String|Name of the publication|
|`source_url`|String|URL linking to the original source|
|`action_type`|Categorical|Type of competitive action|

### Example Records

|event_id|industry|initiating_company|responding_company|action_type|
|---|---|---|---|---|
|EJP_ELEC_001|Electronics Retail|BIC Camera|Yodobashi Camera|Loyalty incentive|
|JPN_QSR_006|Food Service|Sukiya|Yoshinoya|Price increase|

---

## 6. Data Preprocessing and Cleaning

Data preprocessing was performed strictly to ensure **data integrity**, not to optimize analytical outcomes.

### Cleaning Procedures

- removal of duplicate events
    
- standardization of company names
    
- validation of date formats
    
- verification that all events fall within the defined time range
    

### Missing Data Handling

- No imputation was performed
    
- Attributes without reliable information were left blank
    
- This avoids introducing artificial precision or bias
    

---

## 7. Data Quality Assurance and Validation

Quality assurance measures included:

- cross-checking events across multiple publications where possible
    
- verifying consistency between action type and industry context
    
- ensuring all records contain a valid source URL
    

Logical checks ensured that:

- event dates align with reported time frames
    
- firms operate within the specified industry
    
- schema consistency is maintained across all rows
    

---

## 8. Dataset Reliability and Limitations

### Reliability

- High reliability for event occurrence and timing
    
- Strong transparency due to direct source linking
    

### Limitations

- No direct measures of sales, revenue, or demand
    
- No customer-level behavior data
    
- Competitive responses are inferred from observable actions only
    

### Potential Biases

- Media attention bias toward large or well-known firms
    
- Possible underrepresentation of minor or localized responses
    

These limitations are explicitly acknowledged to maintain analytical rigor.

---

## 9. Reproducibility and Transparency

The dataset is fully reproducible by:

1. Applying the same event inclusion criteria
    
2. Using identical source types
    
3. Following the documented schema and construction rules
    

All assumptions and transformations are explicitly stated, ensuring transparency for independent verification.

---

## 10. Conclusion

This dataset provides a **structured, transparent, and reproducible representation of competitive market events** across multiple firm pairs and industries. Its event-based design reflects real-world strategic behavior and is well-suited for **economics and management analysis**, including competitive response modeling, strategic comparison, and policy-relevant interpretation.

---

