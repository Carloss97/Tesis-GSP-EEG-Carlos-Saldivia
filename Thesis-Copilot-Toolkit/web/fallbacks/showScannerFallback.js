// Fallback safe global for `showScanner` to avoid ReferenceError when missing.
// Include this script before your application bundles (e.g., in <head>) so
// that any code calling `showScanner()` will not throw if the provider is
// not present at runtime.

(function () {
  if (typeof window === "undefined") {
    return;
  }

  if (typeof window.showScanner !== "function") {
    window.showScanner = function () {
      // No-op fallback: preserve call signature and log for debugging.
      try {
        if (console && typeof console.warn === "function") {
          console.warn("[Fallback] showScanner not defined — call ignored.");
        }
      } catch (e) {
        // swallow logging errors
      }
      return null;
    };
  }
})();
