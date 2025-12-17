# The GitHub Actions control plane is no longer free

- Score: 213 | [HN](https://news.ycombinator.com/item?id=46291500) | Link: https://www.blacksmith.sh/blog/actions-pricing

### TL;DR
GitHub will start charging $0.002 per minute for all GitHub Actions usage (effective March 1, 2026), even when jobs run on self‑hosted or third‑party runners. This converts the previously free orchestration “control plane” into a metered platform product and is paired with cheaper GitHub‑hosted runners, shifting revenue from low‑margin compute to high‑margin coordination. The article (from Blacksmith, a third‑party runner) argues that self‑hosting still pays off if you aggressively cut CI minutes via faster hardware and caching, while HN comments frame the move as a Microsoft‑style lock‑in and pricing play, prompting renewed interest in GitLab/Forgejo/Codeberg and concern for the long‑term health of GitHub.

---

### Comment pulse
- GitHub is nudging users to hosted runners → new fee plus discounts and VNet make self-hosted costlier. — counterpoint: vendors say they’re still cheaper/faster.  
- Microsoft ownership is blamed for extractive pricing and declining quality → some predict a Skype‑like slow decline, others note no large‑scale migration yet.  
- Alternatives gain attention → GitLab promises no fee for bring‑your‑own runners; Forgejo/Codeberg cited for independence and simpler governance.

---

### LLM perspective
- View: This cements Actions as a billed platform, not a free coordination layer, shrinking the “free if self-hosted” loophole.  
- Impact: Large orgs with heavy CI and external runners must re-evaluate total cost; performance optimizations gain real dollar value.  
- Watch next: Competitor pricing on control planes, community migrations, and whether GitHub improves Actions reliability now that every minute generates revenue.
