# Add loading icon while waiting
# Transcational error when you try to upload again
# 1. What UI to use for home page search and filter in top right?
# Maybe use same as "http://localhost:8000/results" without the Valid page
# 2. How does the archetype and target schematic work?

image = 'demo/myImage.png'
download = ['demo/myControl.py']

apps = {
    "shed os_zone_temp_adjs_rat": {
        "description": "My description",
        "flow_chart": image,
        "performance": image,
        "requirements": "My requirements",
        "download": download
    }, 
    "shed os_zone_temp_adjs_dem_rat": {
        "description": "My description",
        "flow_chart": image,
        "performance": image,
        "requirements": "My requirements",
        "download": download
    },
    "shift os_zone_precool_sim": {
        "description": "My description",
        "flow_chart": image,
        "performance": image,
        "requirements": "My requirements",
        "download": download
    },
    "shift os_zone_precool_com": {
        "description": "My description",
        "flow_chart": image,
        "performance": image,
        "requirements": "My requirements",
        "download": download
    },
    "shift/shed os_zone_precool_sim_temp_adjs_rat": {
        "description": "My description",
        "flow_chart": image,
        "performance": image,
        "requirements": "My requirements",
        "download": download
    }
}

# For "http://localhost:8000/"
# Discussion 1
def getControls():
    return apps

# For "http://localhost:8000/results/info"
def getInformation(control_name):
    return apps[control_name]

archtypes =  ["Residential buildings (e.g. split systems)", "Small commercial buildings (e.g. package units)", "Large commerical buildings (e.g. built-up systems)"]
targets = ["Zone level", "Distribution level",  "Plant level"]
zoneApps = ['shed os_zone_temp_adjs_rat', 'shed os_zone_temp_adjs_dem_rat', 'shift os_zone_precool_sim', 'shift/shed os_zone_precool_sim_temp_adjs_rat']
distributionApps = ['shift os_zone_precool_com']
plantApps = ['shed os_plant_chiller water_temp_reset']

# For "http://localhost:8000/filter"
def getFilters():
    return {
        archtypes[0]: {
            targets[0]: zoneApps
        },
        archtypes[1]: {
            targets[0]: zoneApps,
            targets[1]: distributionApps
        },
        archtypes[2]: {
            targets[0]: zoneApps,
            targets[1]: distributionApps,
            targets[2]: plantApps
        }
    }

# For "http://localhost:8000/filter"
# Discussion 2
def archValidation(file):
    # Some process to return its arch type from the archtypes
    # If it doesn't work for any, then just return None
    return archtypes[0]

# For "http://localhost:8000/filter"
# Discussion 2
def targetValidation(file):
    # Same thing as archValidation() except for targets this time
    return targets[0]
