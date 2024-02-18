def getInformation(control_name):
    # Some function that gets the below information based
    # on the "control_name" passed

    image = 'demo/myImage.png'
    download = ['demo/myControl.py']

    return {
        "description": "My description",
        "flow_chart": image,
        "performance": image,
        "requirements": "My requirements",
        "download": download
    }

def getFilters():
    zoneApps = ['shed os_zone_temp_adjs_rat', 'shed os_zone_temp_adjs_dem_rat', 'shift os_zone_precool_sim', 'shift/shed os_zone_precool_sim_temp_adjs_rat']
    distributionApps = ['shift os_zone_precool_com']
    plantApps = ['shed os_plant_chiller water_temp_reset']

    return {
        "Residential buildings (e.g. split systems)": {
            "Zone level": zoneApps
        },
        "Small commercial buildings (e.g. package units)": {
            "Zone level": zoneApps,
            "Distribution level": distributionApps
        },
        "Large commerical buildings (e.g. built-up systems)": {
            "Zone level": zoneApps,
            "Distribution level": distributionApps,
            "Plant level": plantApps
        }
    }

def getFilters():
    zoneApps = ['shed os_zone_temp_adjs_rat', 'shed os_zone_temp_adjs_dem_rat', 'shift os_zone_precool_sim', 'shift/shed os_zone_precool_sim_temp_adjs_rat']
    distributionApps = ['shift os_zone_precool_com']
    plantApps = ['shed os_plant_chiller water_temp_reset']

    return {
        "Residential buildings (e.g. split systems)": {
            "Zone level": zoneApps
        },
        "Small commercial buildings (e.g. package units)": {
            "Zone level": zoneApps,
            "Distribution level": distributionApps
        },
        "Large commerical buildings (e.g. built-up systems)": {
            "Zone level": zoneApps,
            "Distribution level": distributionApps,
            "Plant level": plantApps
        }
    }
