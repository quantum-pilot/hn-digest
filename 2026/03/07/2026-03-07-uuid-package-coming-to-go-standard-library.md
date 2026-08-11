# UUID package coming to Go standard library

- Score: 342 | [HN](https://news.ycombinator.com/item?id=47283665) | Link: https://github.com/golang/go/issues/62026

### TL;DR

A three-year Go proposal to add a `crypto/uuid` package has entered final-comment status as “Likely Accept.” The planned API centers on a comparable 16-byte type, cryptographically secure version 4 and sortable version 7 generation, permissive parsing compatible with the dominant Google package, text unmarshalling, `MustParse`, comparison, and zero/max values. Supporters want one stable ecosystem-wide type for JSON, text, and database boundaries. Critics fear freezing unsettled choices into Go’s compatibility promise, especially a generic `New` alias whose future behavior could silently change application semantics.

### Comment pulse

- Google’s package is a top ecosystem dependency, making standardization valuable even for projects that never generate identifiers.
- Version 4 avoids time leakage and write correlation; version 7 improves locality — neither is universally newer or better.
- A generator struct could aid testing and monotonic batches — counterpoint: injecting a `func() UUID` keeps the API smaller.
