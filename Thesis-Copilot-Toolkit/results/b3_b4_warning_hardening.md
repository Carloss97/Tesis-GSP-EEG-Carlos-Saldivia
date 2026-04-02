# Warning Hardening Policy (B3/B4)

## Current status
- Consolidated B2 warning registry has rows: no

## Classification decisions
- fixed: warning source solved in code path; regression test should stay green.
- accepted: warning is low-impact and understood under current scope.
- deferred: warning is known and tracked for future hardening.

## Current decisions
- FITPACK_CAPACITY (spline_surface): fixed
- FITPACK_FALLBACK_RBF (spline_surface): accepted
- FITPACK_FALLBACK_MEAN (spline_surface): deferred
- NAN_MEAN_EMPTY in TRSS/TV init paths: fixed via guarded nanmean helper

## Action for future runs
- Keep exporting warnings registry in every full-scale run.
- Promote deferred items to fixed before final camera-ready if they recur.
