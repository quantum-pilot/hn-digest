# Explanation of everything you can see in htop/top on Linux (2019)

- Score: 371 | [HN](https://news.ycombinator.com/item?id=48784777) | Link: https://peteris.rocks/blog/htop/

## TL;DR
The article is a field guide to Linux’s top/htop: it decodes every header, column, and graph, with emphasis on how CPU, load, and memory statistics are actually computed and where they mislead (especially virtual vs resident memory). HN readers share workflow tips like using process-tree mode, different sort keys, and alternative tools such as btop, and debate which memory metric (RSS, PSS, private working set) best reflects real usage without panicking users.  
*Content unavailable; summarizing from title/comments.*

## Comment pulse
- btop as modern replacement for htop → richer UI, power/network/GPU stats, even used on macOS; lacks zram/ZFS/Arc GPU support and musl builds.  
- htop tuning → disabling user threads and enabling tree view gives clearer parent-child relations; but tree mode prevents dynamic resorting, hiding top CPU hogs.  
- Memory metrics are tricky → virtual vs resident clarified; some favor PSS or Windows Private Working Set — counterpoint: no metric stays accurate under swapping.  

## LLM perspective
- View: Tools like htop/top/btop are only useful if users truly understand each field’s semantics and limitations.  
- Impact: Better CPU/memory/I/O models reduce blame and enable smarter performance debugging, cluster scheduling, and capacity planning.  
- Watch next: standardized, cross-platform metrics (RSS, PSS, GPU, zram, cgroup stats) exposed consistently across terminals and GUIs to prevent misinterpretation.
