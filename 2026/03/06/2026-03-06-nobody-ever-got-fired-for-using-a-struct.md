# Nobody ever got fired for using a struct

- Score: 141 | [HN](https://news.ycombinator.com/item?id=47225655) | Link: https://www.feldera.com/blog/nobody-ever-got-fired-for-using-a-struct

## TL;DR
Feldera compiles SQL tables into Rust structs, so a customer’s table with 700+ nullable columns became a giant struct of `Option<T>` fields. In memory this was fine, but on disk rkyv’s archived layout blew up: `Option<ArchivedString>` can’t use Rust’s niche optimizations, so every nullable string paid an 8‑byte discriminant, more than doubling row size and killing throughput. They fixed it by serializing a bitmap of which fields are `NULL` plus the raw values (dense or sparse), cutting row size ~2x. HN debates native-language serialization, 700‑column schemas, and the primacy of data layout.

---

## Comment pulse
- Native-language serialization is dangerous for durable storage → history of Java, .NET BinaryFormatter, PHP, etc.; better to design explicit on‑disk formats—counterpoint: serde with JSON/Protobuf is exactly that.
- Data layout often beats clever algorithms → reorganizing structs/rows simplifies code and boosts speed—counterpoint: you still must design structures knowing how they’ll be used.
- 700‑column tables seen as schema malpractice → some never encounter them; others in enterprise/manufacturing (and Feldera) say hundreds–thousands of nullable columns are common and must be supported, often via columnstores.

---

## LLM perspective
- View: When you don’t control schemas, adapt serialization/layout around them (bitmaps, sparse rows) instead of forcing idealized models.
- Impact: Stream processors, CDC engines, and warehouses ingesting wide, nullable enterprise tables gain most from such row‑format engineering.
- Watch next: Compare this bitmap+dense/sparse row storage to Arrow/Parquet in mixed workloads; document schema evolution and security guarantees of the custom rkyv strategy.
