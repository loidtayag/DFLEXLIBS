# Below is for frontend
# Add loading icon while waiting
# Transcational error when you try to upload again
# Create form for configuratoins page

# Discussions
# 1. What UI to use for home page search and filter in top right?
# Maybe use same as "http://localhost:8000/results" without the Valid column
# Or just add a third box in the home page
# 2. How does the archetype and target schematic work?
# 3. How does the configuration download work?

image = 'demo/myImage.png'
download = ['demo/myControl.py']

apps = {
    "shed os_zone_temp_adjs_rat": {
        "description": "My description",
        "flow_chart": image,
        "performance": image,
        "requirements": "My requirements",
        "download": download,
        "configuration": [
            [
                "text",
                "my_title_1"
            ],
            [
                "number",
                "my_title_2"
            ],
            [
                "choice",
                "my_title_3",
                [
                    "my_choice_1",
                    "my_choice_2"
                ]
            ]            
        ]
    }, 
    "shed os_zone_temp_adjs_dem_rat": {
        "description": "My description",
        "flow_chart": image,
        "performance": image,
        "requirements": "My requirements",
        "download": download,
        "configuration": [
            [
                "text",
                "my_title_1"
            ],
            [
                "number",
                "my_title_2"
            ],
            [
                "choice",
                "my_title_3",
                [
                    "my_choice_1",
                    "my_choice_2"
                ]
            ]            
        ]
    },
    "shift os_zone_precool_sim": {
        "description": "My description",
        "flow_chart": image,
        "performance": image,
        "requirements": "My requirements",
        "download": download,
        "configuration": [
            [
                "text",
                "my_title_1"
            ],
            [
                "number",
                "my_title_2"
            ],
            [
                "choice",
                "my_title_3",
                [
                    "my_choice_1",
                    "my_choice_2"
                ]
            ]            
        ]
    },
    "shift os_zone_precool_com": {
        "description": "My description",
        "flow_chart": image,
        "performance": image,
        "requirements": "My requirements",
        "download": download,
        "configuration": [
            [
                "text",
                "my_title_1"
            ],
            [
                "number",
                "my_title_2"
            ],
            [
                "choice",
                "my_title_3",
                [
                    "my_choice_1",
                    "my_choice_2"
                ]
            ]            
        ]
    },
    "shift/shed os_zone_precool_sim_temp_adjs_rat": {
        "description": "My description",
        "flow_chart": image,
        "performance": image,
        "requirements": "My requirements",
        "download": download,
        "configuration": [
            [
                "text",
                "my_title_1"
            ],
            [
                "number",
                "my_title_2"
            ],
            [
                "choice",
                "my_title_3",
                [
                    "my_choice_1",
                    "my_choice_2"
                ]
            ]            
        ]
    }
}

# For "http://localhost:8000/"
# Discussion 1
def getControls():
    return apps

# For "http://localhost:8000/results/info"
def getInformation(control_name):
    return apps[control_name]

# For "http://localhost:8000/results/configuration"
# Discussion 3
# The configs would be just a list or a dictionary
# For example ['my_value_for_my_title_1', 125, 'my_value_for_my_title_3']
def getConfigurationFiles(control_name, configs):
    paths = [download[0]]

    # Some logic to get the corresponding config file paths
    
    return paths

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
