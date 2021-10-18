# Maps
[![License:MIT](https://img.shields.io/badge/License-MIT-lightgray.svg?style=flt-square)](https://opensource.org/licenses/MIT)  [![Binder](https://binder.pangeo.io/badge_logo.svg)](https://binder.pangeo.io/v2/gh/NASA-SMODE/Maps/main)


This repository contains basic code for manipulating the S-MODE operations area polygon and visualizing ancillary data in the SMODE region. The operations area polygon  in `tools/ops_area_polygon.csv` comes from page 7 of S-MODE Pilot Experimental Plan. This polygon is exported to json in the notebook [OpsAreaPolygon.ipynb](./OpsAreaPolygon.ipynb). 

As shown in the demo notebooks, the operations area file can be read straight from the Github repository:

```python
import pandas as pd 
map_url = 'https://raw.githubusercontent.com/NASA-SMODE/Maps/main/tools/' 
opsarea = pd.read_json(map_url + 'ops_area_polygon.json')
```

There's also a shoreline file that comes in handy for quick-and-dirty plots:
```python 
shore = pd.read_json(map_url + 'NorthCalShoreLine.json')
```

## Demo Notebooks:
    - [Plotting a map of the operations area](./MapOperationsArea.ipynb)
    - [Fetching and visualizing current positions of S-MODE in-situ assets](./InsituAssetsCurrentPosition.ipynb).
    - [Visualizing basic satellite SST and SSH data](./SSTSnapshot.ipynb).
