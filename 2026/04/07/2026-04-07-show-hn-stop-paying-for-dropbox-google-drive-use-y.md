# Show HN: Stop paying for Dropbox/Google Drive, use your own S3 bucket instead

- Score: 224 | [HN](https://news.ycombinator.com/item?id=47673394) | Link: https://locker.dev

### TL;DR

Locker is an open-source, self-hostable file manager positioned against Dropbox and Google Drive. It stores data on local disks, AWS S3, Cloudflare R2, or Vercel Blob, selectable through one environment variable. Beyond uploads and organization, it offers password-protected, expiring share links with download limits, public upload links, full-text search across images and PDFs, a virtual shell, team roles, API keys, and a tRPC API. Its stack combines Next.js, PostgreSQL, Drizzle, BetterAuth, Tailwind, Turborepo, and pnpm.

### Comment pulse

- Commenters argued Dropbox’s real product is reliable desktop/mobile OS integration and effortless synchronization, not merely object storage behind a browser.
- Storage economics can reverse the pitch: a terabyte on major clouds may exceed bundled consumer plans once traffic and operations are included.
- Trust split sharply: inspectable self-hosted code offers control — counterpoint: a week-old, reportedly vibe-coded application is risky for irreplaceable files.

### LLM perspective

- **View:** Locker is currently closer to a self-hosted web file portal than a drop-in synchronization service.
- **Impact:** Power users gain backend portability and data control, while accepting database, authentication, backup, upgrade, and availability duties.
- **Watch next:** Native sync clients, encryption, conflict resolution, recovery documentation, audits, release cadence, and migration evidence determine replacement status.
