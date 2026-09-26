# Excel now supports multiple values in a single cell

- Score: 183 | [HN](https://news.ycombinator.com/item?id=49849832) | Link: https://techcommunity.microsoft.com/blog/microsoft365insiderblog/put-multiple-values-in-one-cell-with-lists-and-arrays-in-excel/4559395

### TL;DR

Excel is previewing lists, arrays stored within cells, and nested arrays for Windows and Mac Beta Channel users. Lists preserve individual values for filtering and calculation; brace-wrapped formulas keep arrays in one cell. New FLATTEN, HAS, HASANY, and HASALL functions manipulate or query them. Most nested-array calculations require workbook Compatibility Version 3, which can change existing formula results. Microsoft warns against important workbooks before general release, and current limitations exclude meaningful support from charts, PivotTables, Power Query, validation dropdowns, and several other features.

### Comment pulse

- Lists address real denormalized data → commenters cited comma-separated owners and applications that currently require awkward parsing.
- Excel remains valuable for analytical nonprogrammers → reactive calculations enable rapid iteration—counterpoint: complex workbooks still accumulate technical debt.
- First-class arrays suggest probabilistic workflows → commenters imagined storing samples in cells, though dedicated tools already model distributions directly.

### LLM perspective

- View: Native collection values are foundational, but the surrounding Excel ecosystem is not yet collection-aware.
- Impact: Early adopters can simplify variable-length records while accepting compatibility and interoperability risks.
- Watch next: General availability, Version 3 migration guidance, and array support across charts, pivots, validation, and Power Query.
