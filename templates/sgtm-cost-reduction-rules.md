# Server-Side GTM Cloud Run Cost Optimization Rules
1. **Filter Non-Essential Telemetry:** Drop scroll events and micro-clicks at web GTM container level before hitting sGTM Cloud Run endpoint.
2. **Consolidate Vendor Hits:** Fire single sGTM incoming event, fan out downstream to Meta CAPI, GA4, and TikTok Events API.
3. **Cache Static Assets via Cloudflare:** Route sGTM subdomain via Cloudflare proxy with caching enabled for `gtm.js`.
