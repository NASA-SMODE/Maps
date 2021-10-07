# A simple modified version of the functions below
# may come in handy for any mesoscale/large-scale
# map one wishes to plot in the SMODE region

import numpy as np
import xarray as xr

import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import matplotlib.ticker as mticker
from mpl_toolkits.axes_grid1 import AxesGrid
from cartopy.mpl.geoaxes import GeoAxes

from config import OPSAREA, MAPEXTENT

import matplotlib as mpl
mpl.rcParams['contour.negative_linestyle']= 'solid'

def plot_operations_area(ax,
                         transform=None,
                         fill_area=False,
                         add_label=False
                ):
    
    """
        Plot S-MODE opeations area. 
        TODO: finish this docstring, adding a complete
              description of parameters.
    """
    
    kwargs_plot = dict(color='k',linewidth=4)
    kwargs_fill = dict(color='0.25', alpha=0.6)
    kwargs_text = dict(color='w',
                       fontsize=11,
                       fontweight='bold',
                       rotation=22,
                    )
    
    if transform:
        kwargs_plot['transform'] = transform
        kwargs_fill['transform'] = transform
        kwargs_text['transform'] = transform
                       
    
    ax.plot(OPSAREA['longitude'],
            OPSAREA['latitude'],
            **kwargs_plot
       )

    if fill_area:
        ax.fill(OPSAREA['longitude'],
                OPSAREA['latitude'],
                **kwargs_fill
               )

    if add_label:
        ax.text(-124.69, 36.9, 
                'S-MODE Operations Area',
                **kwargs_text,
               )
        
def plot_topography(ax,
                    transform=None,
                    colors=False):    
    """
        Plot S-MODE opeations area. 
        TODO: finish this docstring, adding a complete
              description of parameters.
    """

    # Get slice of ETOPO1 data from WHOI's GEOPORT thredds
    url = 'http://geoport.whoi.edu/thredds/dodsC/bathy/etopo1_bed_g2'
    bathy = xr.open_dataset(url)
    bathy = bathy.sel(lon=slice(MAPEXTENT[0],MAPEXTENT[1]),
                      lat=slice(MAPEXTENT[2],MAPEXTENT[3])
    )
    
    if colors:
    
        bathy['topo'].plot.pcolormesh(ax=ax,vmin=-5020,vmax=0,
                                      add_colorbar=False, shading='flat',
                                      extend='neither',cmap='Blues_r',
                                      transform=transform
        )


    clevels = [-5000,-4000,-3000,-2000,-1000,-200,-100]
    CS = bathy['topo'].plot.contour(ax=ax,levels=clevels,
                                    colors='k',linewidths=1,
                                     transform=transform
    )

    ax.clabel(CS, CS.levels, inline=True, fmt='%i', fontsize=10)

    
def plot_map_properties(ax,
                        transform=None,
                        add_grid=False):
    """
            TODO: write docstring
    """
    
    # Axis labels
    ax.set_yticks(np.arange(36,40,1), crs=transform)
    ax.set_xticks(np.arange(-126,-120,1), crs=transform)

    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    ax.set_xlabel('')
    ax.set_ylabel('')

    # Continent
    ax.add_feature(cfeature.NaturalEarthFeature('physical', 'land', '10m',
                   edgecolor='face', facecolor='0.1')
    )

    # Gridlines
    if add_grid:
        gl = ax.gridlines(linewidth=1, color='gray', alpha=0.5, linestyle='-')
        gl.xlocator = mticker.FixedLocator(np.arange(-126,-120,1))
        gl.ylocator = mticker.FixedLocator(np.arange(36,40,1))