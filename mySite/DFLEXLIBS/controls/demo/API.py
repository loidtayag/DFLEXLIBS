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

# For "search"
def getControls():
    return apps

archtypes =  ["Residential buildings (e.g. split systems)", "Small commercial buildings (e.g. package units)", "Large commerical buildings (e.g. built-up systems)"]
targets = ["Zone level", "Distribution level",  "Plant level"]
zoneApps = ['shed os_zone_temp_adjs_rat', 'shed os_zone_temp_adjs_dem_rat', 'shift os_zone_precool_sim', 'shift/shed os_zone_precool_sim_temp_adjs_rat']
distributionApps = ['shift os_zone_precool_com']
plantApps = ['shed os_plant_chiller water_temp_reset']

# For "navigate"
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

# For "results/info"
def getInformation(control_name):
    return apps[control_name]

# For "results/configuration"
# The configs would be just a list or a dictionary
# For example ['my_value_for_my_title_1', 125, 'my_value_for_my_title_3']
def getConfigurationFiles(control_name, configs):
    paths = [download[0]]

    # Some logic to get the corresponding config file paths
    
    return paths
