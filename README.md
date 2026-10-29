# Jiahao Shu's personal website

A bilingual English/Chinese homepage built with HTML, CSS, and a small language-switching script. No package installation or build step is required.

- Primary source: [JiahaoShu/JiahaoShu.github.io](https://github.com/JiahaoShu/JiahaoShu.github.io)
- GitHub Pages: https://jiahaoshu.github.io/
- Canonical public address: https://www.jiahaoshu.top/
- Vercel deployment mirror: [JiahaoShu/jiahaoshu.top](https://github.com/JiahaoShu/jiahaoshu.top)

## Preview

From this directory, run `python -m http.server 8765 --bind 127.0.0.1`, then open http://127.0.0.1:8765/.
Check both languages and a narrow mobile viewport before publishing.

## Keep both deployments in sync

Make content changes in this repository first. The two repositories deploy separately; pushing here does **not** automatically update Vercel.

1. Start with a clean local checkout of `JiahaoShu/jiahaoshu.top`.
2. Run `python tools/sync_site.py /path/to/jiahaoshu.top` from this repository.
3. Review the changes in both repositories, commit, and push each to its existing `main` branch.
4. Run `python tools/sync_site.py /path/to/jiahaoshu.top --check` to verify that the shared files match.
5. Verify both live sites, including the language button, images, and dates. Verify Vercel's response headers after deployment.

The sync helper copies only the explicitly listed public website files. It does not copy credentials, Git metadata, README files, or unrelated files, and it never pushes or deletes anything.

## Security and maintenance

- Keep the site static and dependency-free unless a new feature requires otherwise.
- The HTML contains a Content Security Policy for both hosts. Scripts and styles load from the same origin; there are no third-party scripts or inline scripts.
- `vercel.json` adds response headers on Vercel, including CSP `frame-ancestors`, `nosniff`, and restrictions on unused browser features. GitHub Pages does not apply `vercel.json`; its HTML policy cannot enforce `frame-ancestors`.
- If adding an external image, script, font, or service, review the CSP instead of broadly allowing all origins or inline scripts.
- Keep account access secure and the custom domain renewed. Hosting-provider infrastructure updates are managed by the providers.

Last updated: October 2026.
