# Compute the EOFs and PCs of vertical velocity
#%%
import xarray as xr
import xeofs as xe
from glob import glob
from src.configs import *
from src.regions import *

#%%
# Extract region mass flux data
region = Congo()
w_files = sorted(glob(f'{project_root()}/data/daily_mean.w.*.nc'))
assert(len(w_files)>0)
w_ds = xr.concat([xr.open_dataset(f).W for f in w_files], dim='time')
massflux_da = (-1/9.81)*w_ds  # mass flux = -omega/g
region_massflux = massflux_da.sel(region.lat_lon_slices)

# %%
# Compute EOFs and PCs
model = xe.single.EOF(n_modes=10, center=True)
del model.attrs['solver_kwargs']
model.fit(region_massflux, ('lat', 'lon', 'time'))

  #%%  
# Save Output
out_dir = f'{project_root()}/data'
eof_fname = out_dir + f'/{region.region_name}.massflux_EOFs.nc'
pc_fname = out_dir + f'/{region.region_name}.massflux_PCs.nc'
model.components().to_netcdf(eof_fname)
model.scores(normalized=False).to_netcdf(pc_fname)
# %%
