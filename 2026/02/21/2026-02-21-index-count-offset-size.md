# Index, Count, Offset, Size

- Score: 152 | [HN](https://news.ycombinator.com/item?id=47058584) | Link: https://tigerbeetle.com/blog/2026-02-16-index-count-offset-size/

### TL;DR

TigerBeetle uses a four-word naming convention to make dimensional mistakes visible: count means a number of elements, index selects an element, size measures bytes, and offset identifies a byte position. The core invariants become index below count and size equal to element width times count. It avoids length as ambiguous, appends qualifiers so related variables cluster, and aligns paired names. Commenters praised easier review and grep-based navigation, while others preferred distinct compiler-checked types or argued that length and count already carry different conventional meanings.

### Comment pulse

- Consistent suffixes let reviewers spot unit mismatches without reconstructing the algorithm — counterpoint: dedicated types could make the compiler reject them.
- Index for zero-based positions and number or ordinal for one-based positions was proposed as another useful distinction.
- Name alignment can expose copy-paste errors, though automatic formatters may remove intentional spacing.
