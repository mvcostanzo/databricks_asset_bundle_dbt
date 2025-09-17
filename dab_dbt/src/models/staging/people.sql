{{
  config(
    materialized = 'table',
    schema = 'development'
    )
}}
SELECT * FROM financials.staging.people LIMIT 100;
