# Developers don't understand CORS (2019)

- Score: 355 | [HN](https://news.ycombinator.com/item?id=48614844) | Link: https://fosterelli.co/developers-dont-understand-cors

### TL;DR

The 2019 article uses Zoom’s localhost webserver vulnerability to argue developers often work around CORS instead of understanding it. Zoom encoded status in image dimensions, allowing arbitrary sites to trigger native-client behavior; the author recommends an origin-limited API, iframe restrictions, and user confirmation. HN exposed the nuance: Access-Control-Allow-Origin governs whether browser JavaScript may read responses, but simple requests still reach servers, while failed preflights can stop non-simple ones. Commenters stressed CORS is neither authentication nor complete CSRF protection; state-changing endpoints must enforce methods, content types, origins, and authorization.

### Comment pulse

- CORS relaxes the same-origin policy → it grants selected origins response access; treating it as server-side access control leaves simple cross-origin requests dangerous.
- Preflight semantics matter → non-simple methods and content types require OPTIONS approval, whereas forms and safe methods can be transmitted without that gate.
- Confusion is ecosystem-wide → contradictory tutorials encourage permissive headers and trial-and-error fixes — counterpoint: readers said MDN explains the model clearly when consulted.

### LLM perspective

- **View:** The browser’s split between sending requests and exposing responses is the conceptual seam most explanations fail to foreground.
- **Impact:** Localhost services deserve hostile-network assumptions because any visited page can attempt requests, even when response data remains unreadable.
- **Watch next:** Test endpoint matrices: simple versus preflighted requests, credentials, redirects, null origins, content types, iframe embedding, and browser variations.
