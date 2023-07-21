import pandas as pd
from astropy.coordinates import SkyCoord
import astropy.units as u

def input_data(csv_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_path)

    # Add new columns to df
    df['RA (deg)']  = 0
    df['Dec (deg)'] = 0

    # Loop over dataframe and convert RA and Dec to degrees
    for index, row in df.iterrows():
        ra_hms  = row['RA (HMS)']
        dec_hms = row['Dec (DMS)']

        # Create a SkyCoord object and specify the units
        c = SkyCoord(ra=ra_hms, dec=dec_hms, unit=(u.hourangle, u.deg))
        # Access the converted RA and Dec in degrees
        ra_deg  = c.ra.deg
        dec_deg = c.dec.deg

        # Update the DataFrame with the converted values
        df.at[index, 'RA (deg)']  = ra_deg
        df.at[index, 'Dec (deg)'] = dec_deg

    return df