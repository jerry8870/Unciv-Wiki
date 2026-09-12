# Unciv Wiki

The community guide and database for [Unciv](https://github.com/yairm210/Unciv), the open-source remake of Civilization V.

## About

- **English-first**, targeting international players via Google search
- Data pages and achievements are generated from the Unciv source (see `scripts/`)
- Built with [Astro](https://astro.build) + [Starlight](https://starlight.astro.build)

## Develop

```bash
pnpm install
pnpm dev      # http://localhost:4321/
pnpm build
```

## Deploy

Hosted on GitHub Pages at `https://jerry8870.github.io/Unciv-Wiki/`.
Pushing to `main` triggers the GitHub Actions workflow in `.github/workflows/deploy.yml`.

## License

Site source: MIT. Game data is MPL-2.0 (Unciv) — see [Credits](https://github.com/jerry8870/Unciv-Wiki).
