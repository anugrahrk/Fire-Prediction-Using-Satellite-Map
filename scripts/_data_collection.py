import ee

def run():
    # Initialize Google Earth Engine
    ee.Authenticate()
    ee.Initialize(project='earth-engine-project-449914')

    # Define ROI for Palakkad, Kerala
    roi = ee.Geometry.Rectangle([76.3, 10.5, 76.8, 11.0])

    # Load MODIS Active Fire Data
    fire_data = ee.ImageCollection('FIRMS').filterDate('2020-01-01', '2020-12-31').filterBounds(roi)

    # Load Landsat 8 imagery (Collection 2)
    landsat = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2') \
        .filterDate('2020-01-01', '2020-12-31') \
        .filterBounds(roi) \
        .select(['SR_B4', 'SR_B5', 'ST_B10'])  # Select specific bands

    # Export data to CSV
    task = ee.batch.Export.table.toDrive(
        collection=landsat,
        description='fire_data',
        fileFormat='CSV'
    )
    task.start()
    print("Data collection completed. Check Google Drive for the exported CSV.")