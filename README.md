# Trove zone (and category) totals

[![Frictionless](https://github.com/wragge/trove-zone-totals/actions/workflows/frictionless.yaml/badge.svg)](https://repository.frictionlessdata.io/report?user=wragge&repo=trove-zone-totals&flow=frictionless)

This repository contains an automated git scraper that uses the [Trove API](https://troveconsole.herokuapp.com/) to save data about the contents of Trove's zones and categories. It runs every week and updates the following datasets:

* [trove-zone-totals.csv](data/trove-zone-totals.csv)
* [trove-zone-formats.csv](data/trove-zone-formats.csv)
* [trove-category-totals.csv](data/trove-category-totals.csv)
* [trove-category-formats.csv](data/trove-category-formats.csv)

By retrieving all versions of these files from the commit history, you can analyse changes in Trove over time.

Note that the Trove API v3 (released mid 2023) replaces 'zones' with 'categories' to align better with the web interface. There's no direct correspondence between the contents of 'zones' and 'categories', so the totals can't be easily compared. I'll continue to capture the 'zone' totals while the API v2 is available, so there will be an overlap between systems that will perhaps make it easier to understand changes over time.

## Dataset details

### trove-zone-totals.csv

The dataset is saved as a CSV file containing the following columns:

* `zone` – name of the Trove zone
* `total` – number of records in the zone

### trove-zone-formats.csv

The dataset is saved as a CSV file containing the following columns:

* `zone` – name of the Trove zone
* `format` – format type (see [list of formats](https://trove.nla.gov.au/about/create-something/using-api/api-technical-guide#formats))
* `total` – number of records in the zone with this format

### trove-category-totals.csv

The dataset is saved as a CSV file containing the following columns:

* `category_name` – display name of the Trove category
* `category_code` – category slug used in API calls and urls
* `total` – number of records in the category

### trove-category-formats.csv

The dataset is saved as a CSV file containing the following columns:

* `category_name` – display name of the Trove category
* `category_code` – category slug used in API calls and urls
* `format` – format type (see [list of formats](https://trove.nla.gov.au/about/create-something/using-api/api-technical-guide#formats))
* `total` – number of records in the category with this format

---

Created by [Tim Sherratt](https://timsherratt.org). If you think this is useful, you can become a [GitHub sponsor](https://github.com/sponsors/wragge).

