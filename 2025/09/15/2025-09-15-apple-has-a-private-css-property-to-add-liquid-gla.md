# Apple has a private CSS property to add Liquid Glass effects to web content

- Score: 335 | [HN](https://news.ycombinator.com/item?id=45250370) | Link: https://alastair.is/apple-has-a-private-css-property-to-add-liquid-glass-effects-to-web-content/

### TL;DR

WebKit contains a private `-apple-visual-effect` CSS property that can render system blur materials and iOS 26 Liquid Glass inside WKWebView. It requires the private `useSystemAppearance` preference, making third-party App Store use effectively unavailable. The author demonstrated the effect and inferred Apple may use it to make internal webviews look native. HN debated whether withholding the capability is anticompetitive or merely normal internal API development, while using the discovery to discuss how well-integrated webviews become difficult to identify.

### Comment pulse

- Private styling prompted competition concerns → counterpoint: no supplied evidence shows first-party apps use it or that it causes meaningful market harm.
- Seamless webviews may hide in plain sight → suspected examples include account settings, App Store, Music, Mail, and Calendar surfaces.
- Liquid Glass itself divides users → supporters see clearer targets and personality; critics cite distracting motion, extra taps, and accessibility inconsistencies.

### LLM perspective

- View: The property is evidence of WebKit experimentation, not proof of deployment or competitive intent.
- Impact: Third-party developers cannot safely depend on the effect, so native-looking webviews still require public primitives.
- Watch next: Public API exposure, standards discussion, first-party usage evidence, and Reduce Motion or Transparency behavior.
