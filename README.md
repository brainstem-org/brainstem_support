# BrainSTEM Documentation and Support Website

This repository hosts the documentation and support website for [BrainSTEM.org](https://brainstem.org). BrainSTEM is a collaborative electronic lab notebook for FAIR data sharing in neuroscience research. The website documents the BrainSTEM platform: the data model, the web interface, the API, the tools, AI integration (MCP server and agent skills), NWB export, tutorials, and the public data-sharing portal.

The site is published at [support.brainstem.org](https://support.brainstem.org/) and built with the [Just the Docs](https://just-the-docs.github.io/just-the-docs/) Jekyll theme.

## Repository layout

| Path | Content |
|---|---|
| `docs/` | The Jekyll site. Hand-written pages for the data model, web interface, tutorials and tools; generated pages for the API resources and schemas. |
| `docs/assets/datamodel/` | `explorer.html`, the page that hosts the interactive data model. The model itself (graph, type summaries and renderer) is fetched from the BrainSTEM server when the site is built and is not committed. |
| `docs/_preambles/` | Hand-written introductions inserted into generated schema pages. |
| `docs/_includes/` | `datamodel_embed.html` (the focused diagram on model pages) and generated `schemas/*.md` snippets for models whose JSON fields have a schema. |
| `scripts/build_reference_docs.py` | Generates the API and schema pages from the server's public reference (`/reference/data/*.json`) and fetches the interactive data model (graph, type summaries, renderer) from it. |
| `.github/workflows/pages.yml` | Builds the site and deploys it to GitHub Pages on every push to `main` and daily, fetching the interactive data model from the server first (see [Deployment](#deployment)). |
| `.github/workflows/sync-reference.yml` | Weekly job that regenerates the API and schema pages from production and opens a pull request when they changed. |
| `scripts/screenshots.py` | Takes the documentation's screenshots from a BrainSTEM instance with the demo dataset (`docs/assets/images/screenshots/`). |
| `docs/assets/images/diagrams/` | Hand-authored SVG illustrations of the data model's concepts. |
| `AUTHORING.md` | What each kind of page must contain, and how the site is kept in step with the server. |

Generated pages carry a `<!-- generated:start -->` marker; do not edit inside it. See [AUTHORING.md](AUTHORING.md) before writing or changing a page.

## Keeping the site in step with BrainSTEM

```bash
# Regenerate the API and schema pages and fetch the interactive data model from the production server
python scripts/build_reference_docs.py --server https://www.brainstem.org --clean

# Or from a BrainSTEM checkout (for a release that is not deployed yet)
python scripts/build_reference_docs.py --brainstem /path/to/brainstem --clean
```

The sync workflow regenerates the pages every Monday and on demand ("Run workflow") and opens a pull request with the diff. The interactive data model is ignored by git; the Pages workflow fetches it at every build.

## Deployment

The site is published to [support.brainstem.org](https://support.brainstem.org/) by the workflow [`.github/workflows/pages.yml`](.github/workflows/pages.yml), which runs on every push to `main`, daily, and on demand ("Run workflow"). It:

1. fetches the interactive data model from the BrainSTEM server (`build_reference_docs.py --assets-only`) into `docs/assets/datamodel/`;
2. builds the Jekyll site;
3. publishes it to GitHub Pages.

The workflow is needed because the interactive data model is not committed: GitHub's built-in Pages build only builds what is in the repository and cannot fetch it.

### GitHub settings

- **Settings > Pages > Build and deployment > Source** must be **GitHub Actions**. With "Deploy from a branch", GitHub builds `docs/` itself without the data model, and the interactive views stay empty. Switch it when `pages.yml` reaches `main`: until the workflow has run, nothing new is published, but the last published site stays online. The setting needs admin rights on the repository.
- The custom domain (support.brainstem.org) stays in the Pages settings; `docs/CNAME` is kept for reference.
- The repository variable **`BRAINSTEM_SERVER`** (Settings > Secrets and variables > Actions > Variables) chooses the server the data model is fetched from; without it, production (`https://www.brainstem.org`). "Run workflow" also takes a server for a single build.

### Server requirements and failures

- The server must publish its reference at `/reference/` with the interactive data model (reference format 1.2 or later). If it does not, the fetch fails, nothing is published, and the live site stays as it was. Merge documentation for an unreleased BrainSTEM version only after that version is deployed.
- The server allows 600 requests a minute to `/reference/`, and the data model is some 450 files, so the fetch takes about a minute; when throttled, it waits as long as the server's `Retry-After` header asks.
- A branch without `docs/assets/datamodel/explorer.html` does not embed the data model and skips the fetch.

## Contribution and feedback

We encourage dialog, feedback, and contributions to improve BrainSTEM and the documentation and tutorials:

- **[Issues](https://github.com/brainstem-org/brainstem_support/issues):** report bugs, suggest improvements, or request new documentation content.
- **[Discussions](https://github.com/brainstem-org/brainstem_support/discussions):** engage with the community, ask questions, or propose ideas for the platform.

## Local development

1. Clone this repository:
   ```bash
   git clone https://github.com/brainstem-org/brainstem_support.git
   ```
2. Navigate into the docs directory:
   ```bash
   cd brainstem_support/docs
   ```
3. Install Jekyll and dependencies:
   ```bash
   bundle install
   ```
4. Fetch the interactive data model (run from the repository root; use `--server http://localhost:8000` or `--brainstem /path/to/brainstem` for an unreleased version):
   ```bash
   python scripts/build_reference_docs.py --server https://www.brainstem.org --assets-only
   ```
5. Serve the site locally:
   ```bash
   bundle exec jekyll serve
   ```
6. Open `http://localhost:4000`.

## License

The documentation, the site's source and the scripts in this repository are released under the [MIT License](LICENSE).

The interactive data model shown on the site (everything under `docs/assets/datamodel/` apart from `explorer.html`) is not part of this repository and is not covered by its licence; the site's build fetches it from the BrainSTEM server. Its data model graph and type schemas are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); the diagram renderer (`vendor/`) is © BrainSTEM, all rights reserved.
