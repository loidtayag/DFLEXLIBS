image = 'demo/myImage.png'
download = ['demo/myControl.py']

download_shed_zone_temp_adjs = ['hvac/sequences/python/strategies/stra_zone_temp_shed_price.py', 
                                'hvac/sequences/python/functions/fu_ashrae_TSet_adjust.py',
                                'hvac/sequences/python/functions/fu_runaway_condition.py',
                                'hvac/sequences/python/functions/fu_runaway_TsetCooZon.py',
                                'hvac/sequences/python/functions/fu_runaway_TsetHeaZon.py',
                                'hvac/sequences/python/functions/fu_shed_price_event.py',
                                'hvac/sequences/python/functions/fu_shed_TsetCooZon.py',
                                'hvac/sequences/python/functions/fu_shed_TsetHeaZon.py',
]

chart_shed_zone_temp_adjs = 'demo/chart_shed_zone_temp_adjs.png'
performance_shed_zone_temp_adjs = 'demo/performance_shed_zone_temp_adjs.png'


apps = {
    "shed zone_temp_adjs": {
        "description": 
                "Shed control strategies can reduce demand by allowing the temperature to “float” to a" 
                "more relaxed setpoint, which delays the operation of HVAC system.\n Its effectiveness depends on thermal comfort boundaries,"
                "as well as internal and external heat gains.\n"
                "This application was designed in a modular fashion, where self-contained functions were pieced together according to the "
                "chosen strategy. The application begins with a function that relaxes the comfort range for DF event periods with customized "
                "offset values. Then, it includes a function that assesses the thermal comfort of different zones. If the zone temperature is "
                "within the expanded temperature band, it is considered eligible for DF control. If the zones are eligible, another function "
                "evaluates the current grid signal and assesses if a load shed event has started (i.e., if the price is above a threshold "
                "estimated as the third quartile of the input price distribution). The shed function computes new setpoints according to the "
                "current HVAC operation mode and the zone setpoints. If no shed event is detected or the zones are not eligible for DF controls, "
                "the application releases the control, which means it incrementally returns the setpoints to their baseline values.",
        
        "flow_chart": chart_shed_zone_temp_adjs,
        "performance": performance_shed_zone_temp_adjs,
        "requirements": "hellooooooooooooooooooooooooooooooooooooo\n"
                        "world",
        "download": download_shed_zone_temp_adjs,
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
    
    "shed os_plant_chiller_water_temp_reset": {
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
zoneApps = ['shed zone_temp_adjs' ,'shed os_zone_temp_adjs_rat', 'shed os_zone_temp_adjs_dem_rat', 'shift os_zone_precool_sim', 'shift/shed os_zone_precool_sim_temp_adjs_rat']
distributionApps = ['shift os_zone_precool_com']
plantApps = ['shed os_plant_chiller_water_temp_reset']

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