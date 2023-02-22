# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 16:57:00 2023

@author: Sibel.Uskuplu
"""

from ukcp_api_client.client import UKCPApiClient

api_key = "t4r_aPNXzi7F4wgYINssjW_OgQTOIkAT"
emissions_scenario=['rcp26',
                    'rcp45',
                    'rcp85'
                    ]

for scenario in emissions_scenario:
    for m in [
        'jan',
        # 'feb','mar','apr','may','jun','jul','aug','sep','oct','nov',
        # 'dec'
          ]:
        cli = UKCPApiClient(outputs_dir="E:\\CC_Data\\data_review\\outputs\\RCPs", api_key=api_key)
    
        output_filename =f"{scenario}_{m}Panom_2050s.csv"
        cli.download(output_file=output_filename)
  
        request_url = f"https://ukclimateprojections-ui.metoffice.gov.uk/wps?service=wps&request=Execute&version=1.0.0&Identifier=LS1_Maps_01&Format=text/xml&Inform=true&Store=false&Status=false&DataInputs=Baseline=b8110;Collection=land-prob;DataFormat=csv;FontSize=m;ImageFormat=png;ImageSize=1200;JobLabel={scenario}_"+f'{m}'.capitalize()+f"Panom_2050s;Scenario={scenario};SpatialSelectionType=river_basin;TemporalAverage={m};TimeSlice=2040-2069;TimeSliceDuration=30y;Variable=prAnom"
    # "https://ukclimateprojections-ui.metoffice.gov.uk/wps?service=wps&request=Execute&version=1.0.0&Identifier=LS1_Maps_01&Format=text/xml&Inform=true&Store=false&Status=false&DataInputs=Baseline=b8110;Collection=land-prob;DataFormat=csv;FontSize=m;ImageFormat=png;ImageSize=1200;JobLabel=rcp45_"+f'{m}'.capitalize()+f"Panom_2050s;Scenario=rcp45;SpatialSelectionType=river_basin;TemporalAverage={m};TimeSlice=2040-2069;TimeSliceDuration=30y;Variable=prAnom"
        file_urls = cli.submit(request_url)