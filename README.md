# Trove zone totals

[![Frictionless](https://github.com/wragge/trove-zone-totals/actions/workflows/frictionless.yaml/badge.svg)](https://repository.frictionlessdata.io/report?user=wragge&repo=trove-zone-totals&flow=frictionless)

This repository contains an automated git scraper that uses the [Trove API](https://troveconsole.herokuapp.com/) to save data about the contents of Trove's zones. It runs every week and updates the following datasets:

* [trove-zone-totals.csv](data/trove-zone-totals.csv)

By retrieving all versions of these files from the commit history, you can analyse changes in Trove over time.

## Dataset details

### trove-zone-totals.csv

The dataset is saved as a CSV file containing the following columns:

* `zone` – name of the Trove zone
* `total` – number of records in the zone

---

Created by [Tim Sherratt](https://timsherratt.org). If you think this is useful, you can become a [GitHub sponsor](https://github.com/sponsors/wragge).

