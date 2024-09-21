def compute_quantiles(ds):
    import xarray as xr
    from scipy.stats import rankdata

    # Convert Dataset to DataArray
    data_array = ds
    # Stack all dimensions
    stacked = data_array.stack(all_dims=data_array.dims)
    # Compute ranks
    ranks = xr.DataArray(rankdata(stacked, method='average') - 1, coords=stacked.coords, dims='all_dims')
    # Compute quantiles
    quantiles = ranks / (len(stacked) - 1)
    # Unstack dimensions
    quantiles = quantiles.unstack('all_dims')

    return quantiles

def array_midpoints(x):
    return (x[1:]+x[:-1])/2
