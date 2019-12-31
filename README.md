# Research_SPI_Calculations
## SURGE
  The overall goal of this for this project is to help predict social unrest. With worldwide instability and unrest, the Social Unrest Reconnaissance GazEtteer (SURGE) project was created to predict this underlying problem. It emphasizes making long-term predictions using dynamic social media data and multiagent simulations. This project’s overall goal is to devise a system--integrating data, creating novel algorithms, and conducting multi agent simulations--that automatically and accurately anticipate social unrest events.  With this project, the purpose is to improve on the current distance function used to identify a conceptual neighborhood of a social unrest event, to more effectively group similar unrest events. This, in turn, enables the system to more accurately predict social unrest by including influences or impacts from neighboring events.  A conceptual neighborhood is beyond just spatial distances, as the distance function also involves temporal, social-economic, and infrastructural gaps. Specifically, in this project, we will observe how additional factors, mainly provided by the Global Database of Events, Language, and Tone (GDELT) database, can contribute to this distance function through the implementation of more positively influenced factors. With different variables, SPI is potentially one of many influencers of social unrest. We will be focusing specifically on SPI here. This project is funded by the NGA and lead by Dr. Soh at the University of Nebraska-Lincoln.

## What Is SPI?
  The Standard Precipitation Index (SPI) is a commonly used meteorological drought index based on precipitation. Precipitation records within a moving window are compared with the same period in the historical records. The moving window can be any period of length. 1, 3, 6, 9, 12, 24, and 48-month periods are the most common. Because aggregate precipitation deficits in different periods are influenced by various water resources such as snowpack, soil moisture, and groundwater, the different moving windows can reflect the changes of different water features. For example, a short-term SPI such as 1-month SPI can efficiently monitor the changes of soil moisture and crop stress in the growing season while a long-term SPI such as 12-month SPI performs higher correlations with stream flows and reservoir levels. 
  
  Before determining the SPI, we take raw precipitation data and fit it into normal gamma distribution. The length of the study period of precipitation data set taken varies from research to research. However, typically, 30-50 years is a good range (we will use 30 years of data for this research). Once we have acquired this data, we must determine our SPI window size. SPI can be created for different periods. For example, if we want to calculate SPI1 (one month) at the end of February, we would compare the total precipitation for February in the desired year to the total precipitation of February in all historical records. If we want to calculate SPI3 (three months), we would compare the previous 3 months with the whole historical records. If we are currently looking at the end of April for SPI3, we will look back at February, March, and April. Now with our raw data, we will calculate SPI using this moving window size. Once we have this window, SPI can now be computed.
  
  The positive (negative) SPI values are greater (less) than the median precipitation that is zero because of the standardization. The magnitude of the departure from zero is a probabilistic measure of the severity of a wet (+) or dry (-) condition (WMO, 2012; Guttman, 1999). 
  
SPI Value | Condictions
------------ | -------------
2.0+ | Extremely Wet
1.5 to 1.99 | Very Wet
1.0 to 1.49 | Moderately Wet
-0.99 to 0.99 | Near Normal
-1.0 to -1.49 | Moderately Dry
-1.5 to -1.99 | Very Dry
-2.0 and less | Extremely Dry

## The Calculations
  Please note for this research, we calculated SPI3 using the following steps:
  1. First, we need to determine the No Data Value of our image
      1. Since precipitation from CHIRPS is from satellite, the developers had selected a magic number for areas where you wouldn’t care about. For example, we would not care about the precipitation in the Pacific so we would set the values around the Pacific Ocean to -9999. So when we see the number -9999 at any pixel, we can determine that that is a NoData value. 
      2. We can determine the NoData value by using QGIS or ArcGIS. For this example, we will us QGIS. First, open QGIS and then drive one of the raw images into the application. One the image is opened in the application, select the “Identify Features” button on the toolbar at the top. The keyboard for it on Windows 10 is Ctrl+Shift+I. Click on a pixel in the ocean and it should give you a value. Typically the value should be -9999. Now that we found our NoData value, we can look at the code. 
  2. Clipping the Images
      1. Currently, everything is hardcoded, but can easily be changed for easier usage. Change the variable ‘odir’ to your desired out directory. Change the variable ‘idir’ to the location of your raw data. Change ‘inMash’ to the path of your Shapefile. 
      2. If your NoData value is not -9999, locate the ‘cmd’ variable. Within that variable, replace the value -9999 to the data’s actual NoData value.  
      3. Once all these changes are completed, run the script and it will begin clipping. **Please note, depending on how much your shapefiles are, this can take up a lot of space and use a lot of time.**
  3. Calculating SPI with the clipped images
      1. Open SPI3_Analysis
          * Note this current code takes in only h5 file. You might need to change the clipped images to an h5 value.
      2. Once this change is made, we can simply run the script
          * However, if we are not computing SPI3 with 30 days you can change the variable ‘spi’. The parameters for spi is ( 1D or 2D numpy precipitation array, scale (i.e. gamma distribution), data start year, calibration year initial, calibration year final, periodicity). For more information about the parameters, locate indices.py in the climate_indices package. 

## Resources
  * QGIS (https://www.qgis.org/en/site/) 
      * ArcGIS is another alternative
  * Anaconda (https://www.anaconda.com/)
      * Recommended Packages:
          * GDAL
          * Climate-Indices
            * **PLEASE NOTE**: Due to installation conflicts, We had to directed download the Climate-Indices Package. As a result, we did not create or change any scripts in the Climate_indices folder. The Original Source can be found at https://github.com/monocongo/climate_indices.
  * Precipitation Data 
      * Example precipitation set from CHRIPS: ftp://ftp.chg.ucsb.edu/pub/org/chg/products/CHIRPS-2.0/global_daily/tifs/p05/
  * Shapefile of the desired region
      * Example of Bangladesh: https://data.humdata.org/dataset/administrative-boundaries-of-bangladesh-as-of-2015
  
