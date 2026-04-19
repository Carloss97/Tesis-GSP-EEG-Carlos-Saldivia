# showScanner fallback

This folder contains a minimal fallback implementation for a global
`showScanner` function. The fallback prevents a `ReferenceError` when
the real scanner provider is not loaded before application code.

How to use

- Include `web/fallbacks/showScannerFallback.js` in your HTML before
  application bundles:

```html
<script src="/path/to/web/fallbacks/showScannerFallback.js"></script>
<script src="/assets/index-....js"></script>
```

- Or import it in your application's entry point before other modules:

```js
import './web/fallbacks/showScannerFallback.js';
// then import app
import './index.js';
```

Notes

- This is a defensive no-op. For full functionality you must ensure the
  real `showScanner` implementation (provided by the scanner vendor or
  a plugin) is loaded and assigns `window.showScanner`.
