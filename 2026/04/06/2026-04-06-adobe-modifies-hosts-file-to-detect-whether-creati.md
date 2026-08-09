# Adobe modifies hosts file to detect whether Creative Cloud is installed

- Score: 212 | [HN](https://news.ycombinator.com/item?id=47664205) | Link: https://www.osnews.com/story/144737/adobe-secretly-modifies-your-hosts-file-for-the-stupidest-reason/

### TL;DR

Adobe Creative Cloud reportedly edits the Windows or macOS hosts file so Adobe’s website can detect whether the desktop software is installed. The site loads a special image; the presence or absence of Adobe’s mapping reveals installation status. Adobe previously probed localhost ports, but Chrome’s Local Network Access protections blocked that approach, prompting this workaround. HN readers viewed it as an undisclosed system-level modification and called for operating systems and installers to expose, authorize, log, and reverse configuration changes.

### Comment pulse

- Applications should install within scoped directories, not silently alter global configuration.
- Defender reportedly warns when hosts changes occur — counterpoint: administrators have always edited the file for legitimate purposes.
- Readers proposed installer previews showing a diff of every system change with reliable rollback.

### LLM perspective

- **View:** The trick is small; bypassing a browser privacy boundary without explicit consent is the real problem.
- **Impact:** Users inherit opaque state, while OS vendors face pressure for stronger installation sandboxes.
- **Watch next:** Adobe disclosure, uninstall cleanup, Defender behavior, and permission systems for hosts-file edits.
