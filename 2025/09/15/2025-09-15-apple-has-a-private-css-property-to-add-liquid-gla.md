# Apple has a private CSS property to add Liquid Glass effects to web content

- Score: 335 | [HN](https://news.ycombinator.com/item?id=45250370) | Link: https://alastair.is/apple-has-a-private-css-property-to-add-liquid-glass-effects-to-web-content/

- TL;DR
    - A developer spotted a private WebKit CSS property (-apple-visual-effect) that applies Apple’s new “Liquid Glass” materials to web content. It doesn’t work on public Safari and only renders in WKWebView if a private flag (useSystemAppearance) is enabled—so third‑party apps can’t ship it without App Store risk. The author’s demo suggests Apple likely uses it internally, reinforcing the idea that well‑done webviews are invisible. HN debated anticompetitive implications, guessed where Apple hides webviews, and split on Liquid Glass’s UX and accessibility.

- Comment pulse
    - Private CSS is anticompetitive → First‑party apps get unique UI. — counterpoint: Private APIs are common; cosmetic features rarely affect competition; legal harm standard not met.
    - Good webviews are invisible → Seamless integration hides them; users cite Settings/iCloud, App Store account pages, Music, Mail/Calendar. — counterpoint: Skeptics demand concrete examples.
    - Liquid Glass UX divides → Fans like personality and clearer affordances; critics report regressions, extra clicks, heavy animations, inconsistent Reduce Motion/Transparency.

- LLM perspective
    - View: Private CSS hints Apple treats webviews as core UI plumbing; public standardization may follow if stability and accessibility mature.
    - Impact: Third‑party apps can’t fully match iOS 26 visuals, widening polish gap and nudging more first‑party flows into webviews.
    - Watch next: WebKit flags surfacing in betas, an explainer/proposal to W3C CSSWG, and accessibility fixes honoring Reduce Motion/Transparency across Apple apps.
