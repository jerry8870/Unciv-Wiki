# Unciv Wiki

The community guide and database for [Unciv](https://github.com/yairm210/Unciv), the open-source remake of Civilization V.

## About

- **English-first**, targeting international players via Google search
- Data pages and V3 achievements use a checked-in, checksummed 4.21.20 (1293) snapshot; normal builds need no game repository.
- Built with [Astro](https://astro.build) + [Starlight](https://starlight.astro.build)

## Develop

```bash
pnpm install --frozen-lockfile
pnpm validate # data, analytics, build, sitemap and all content-page checks
pnpm preview --host 127.0.0.1 # http://127.0.0.1:4321/Unciv-Wiki/
```

See the [maintenance and launch runbook](docs/MAINTENANCE-AND-LAUNCH.md) and [local implementation report](docs/IMPLEMENTATION-2026-09-12.md). GA4 stays off unless configured and explicitly accepted by the visitor.

## Deploy

Hosted on GitHub Pages at `https://jerry8870.github.io/Unciv-Wiki/`.
Pushing to `main` triggers the GitHub Actions workflow in `.github/workflows/deploy.yml`.

## License

Site source: MIT. Game data is MPL-2.0 (Unciv) — see [Credits](https://github.com/jerry8870/Unciv-Wiki).
