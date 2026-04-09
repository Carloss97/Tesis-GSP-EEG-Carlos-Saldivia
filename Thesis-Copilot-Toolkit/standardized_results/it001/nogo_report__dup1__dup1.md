# No-Go Report — it01

**DECISION: NO-GO ✗**

## Failed Criteria

- G1 MAE improvement
- G2 RMSE improvement
- G5 QA gates

## Diagnostics

- QA gates status: QA-01=PASS, QA-02=PASS, QA-03=PASS, QA-04=PASS, QA-05=PASS, QA-06=FAIL, QA-07=PASS

- error_rate: 0.0455

## Recommended Actions

- QA FAIL gates: ['QA-06']. Review data quality.
- G1/QA-06 FAIL: TV/Time MAE not better than best instant. Check method implementations.