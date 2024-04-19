image = 'demo/myImage.png'
download = []

download_zone_temp_shed_price = ['controls/hvac/sequences/python/strategies/stra_zone_temp_shed_price.py', 
                                'controls/hvac/sequences/python/functions/fu_ashrae_TSet_adjust.py',
                                'controls/hvac/sequences/python/functions/fu_runaway_condition.py',
                                'controls/hvac/sequences/python/functions/fu_runaway_TsetCooZon.py',
                                'controls/hvac/sequences/python/functions/fu_runaway_TsetHeaZon.py',
                                'controls/hvac/sequences/python/functions/fu_shed_price_event.py',
                                'controls/hvac/sequences/python/functions/fu_shed_TsetCooZon.py',
                                'controls/hvac/sequences/python/functions/fu_shed_TsetHeaZon.py',
]
control_flow_zone_temp_shed_price = 'controls/hvac/sequences/python/strategies/control_flow_zone_temp_shed_price.png'
performance_zone_temp_shed_price = 'controls/hvac/sequences/python/strategies/zone_temp_shed_price_results.png'

download_zone_temp_shift_shed_price = ['controls/hvac/sequences/python/strategies/stra_zone_temp_shift_shed_price.py', 
                                'controls/hvac/sequences/python/functions/fu_ashrae_TSet_adjust.py',
                                'controls/hvac/sequences/python/functions/fu_runaway_condition.py',
                                'controls/hvac/sequences/python/functions/fu_runaway_TsetCooZon.py',
                                'controls/hvac/sequences/python/functions/fu_runaway_TsetHeaZon.py',
                                'controls/hvac/sequences/python/functions/fu_shift_occ_price_event.py',
                                'controls/hvac/sequences/python/functions/fu_shift_TsetCooZon.py',
                                'controls/hvac/sequences/python/functions/fu_shift_TsetHeaZon.py',
                                'controls/hvac/sequences/python/functions/fu_shed_price_event.py',
                                'controls/hvac/sequences/python/functions/fu_shed_TsetCooZon.py',
                                'controls/hvac/sequences/python/functions/fu_shed_TsetHeaZon.py',
]
control_flow_zone_temp_shift_shed_price = 'controls/hvac/sequences/python/strategies/control_flow_zone_temp_shift_shed_price.png'
performance_zone_temp_shift_shed_price = 'controls/hvac/sequences/python/strategies/zone_temp_shift_shed_price_results.png'

apps = {
    "zone_temp_shed_price": {
        "description": 
                "Load shedding strategies entail reducing building demand for a short period of time during shed events, "
                "which typically coincident with electric power system peaks, such as extremely hot summer afternoons. "
                "These strategies can reduce demand by allowing the temperature to “float” to a " 
                "more relaxed setpoint, which delays the operation of HVAC system. "
                "Its effectiveness depends on thermal comfort boundaries, as well as internal and external heat gains.\n"
                "The zone_temp_shed_price application begins with a function that relaxes the comfort range for Demand Response (DR) "
                "event periods with customized offset values. Then, it includes a function that assesses the thermal comfort of different zones. "
                "If the zone temperature is within the expanded temperature band, it is considered eligible for DR control. "
                "When the zones are eligible, another function evaluates the current grid signal and assesses if a load shed event has started "
                "(i.e., if the price is above a threshold estimated as the third quartile of the input price distribution). "
                "When the shed event is detected, the shed function computes new setpoints according to the current HVAC operation mode "
                "and the zone setpoints. If no shed event is detected or the zones are not eligible for DR controls, "
                "the application releases the control, which means it incrementally returns the setpoints to their baseline values.",
        "flow_chart": control_flow_zone_temp_shed_price,
        "performance": performance_zone_temp_shed_price,
        "requirements": "@prefix brick: <https://brickschema.org/schema/Brick#> .\n"
                    "@prefix owl: <http://www.w3.org/2002/07/owl#> .\n"
                    "@prefix sh: <http://www.w3.org/ns/shacl#> .\n"
                    "@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n"
                    "@prefix ref: <https://brickschema.org/schema/Brick/ref#> .\n"
                    "@prefix constraint: <https://nrel.gov/BuildingMOTIF/constraints#> .\n"
                    "@prefix : <urn:zone_temp_shed_price/> .\n"
                    "\n"
                    ": a owl:Ontology ;\n"
                    "    owl:imports <https://brickschema.org/schema/1.3/Brick> .\n"
                                
                    ":zone a sh:NodeShape, owl:Class ;\n"
                    "    sh:targetClass brick:Zone ;\n"
                    "    sh:property [ sh:path brick:hasPoint ;\n"
                    "            sh:qualifiedValueShape [sh:targetClass brick:Max_Air_Temperature_Setpoint];\n"
                    "            sh:qualifiedMinCount 1 ] ,\n"
                    "    [ sh:path brick:hasPoint ;\n"
                    "            sh:qualifiedValueShape [sh:targetClass brick:Min_Air_Temperature_Setpoint];\n"
                    "            sh:qualifiedMinCount 1  ] ,\n"
                    "    [ sh:path brick:hasPoint ;\n"
                    "            sh:qualifiedValueShape [sh:targetClass brick:Zone_Air_Temperature_Sensor];\n"
                    "            sh:qualifiedMinCount 1 ] ,\n"
                    "    [ sh:path brick:hasPoint ;\n"
                    "            sh:qualifiedValueShape [sh:targetClass brick:Occupancy_Sensor];\n"
                    "            sh:qualifiedMinCount 1 ] ; \n"       
                    "    sh:property [\n"
                    "        sh:path brick:hasPoint ;\n"
                    "        sh:qualifiedValueShape [ sh:or (\n"
                    "            [sh:targetClass brick:Zone_Air_Cooling_Temperature_Setpoint;]\n"
                    "            [sh:targetClass brick:Zone_Air_Heating_Temperature_Setpoint;] \n"
                    "            [sh:targetClass brick:Zone_Air_Temperature_Setpoint;] \n"
                    "        )] ;\n"
                    "        sh:qualifiedMinCount 1 ;\n"
                    "    ] ;\n"
                    ".\n"
                    "\n"
                    ":timeseries-identifier a sh:NodeShape ;\n"
                    "    sh:targetClass brick:Max_Air_Temperature_Setpoint,\n"
                    "                brick:Min_Air_Temperature_Setpoint,\n"
                    "                brick:Zone_Air_Temperature_Sensor,\n"
                    "                brick:Zone_Air_Cooling_Temperature_Setpoint,\n"
                    "                brick:Zone_Air_Heating_Temperature_Setpoint,\n"
                    "                brick:Zone_Air_Temperature_Setpoint,\n"
                    "                brick:Occupancy_Sensor;\n"
                    "\n"
                    "    sh:property [\n"
                    "        sh:path ref:hasExternalReference ; \n"
                    "        sh:minCount 1;\n"
                    "        sh:nodeKind sh:BlankNode ;\n"
                    "       sh:property [\n"
                    "            sh:path ref:hasTimeseriesId ; \n"
                    "            sh:minCount 1;\n"
                    "            sh:maxCount 1;\n"
                    "            sh:datatype xsd:string ;\n"
                    "        ] ;	\n"
                    "   ] ;\n"
                    ".\n",
        "download": download_zone_temp_shed_price,
        "configuration": [
            [
                "text",
                "sparql_query"
            ],
            [
                "text",
                "graph_path"
            ],
            [
                "text",
                "price_identifier"
            ],
            [
                "slider",
                "Tlimit_min",
                {
                    "min": 0,
                    "max": 400,
                }
            ],   
            [
                "slider",
                "Tlimit_max",
                {
                    "min": 0,
                    "max": 400,
                }
            ],  
            [
                "multiple_choice",
                "hvac_mode_type",
                [
                    "Single HVAC control signal",
                    "Heating control signal",
                    "Cooling control signal"
                ]
            ],
            [
                "text",
                "hvac_mode_identifier"
            ],
            [
                "text",
                "heat_signal_identifier"
            ],
            [
                "text",
                "cool_signal_identifier"
            ],
            [
                "boolean",
                "adj_comfort_range_flag",
            ],  
            [
                "Number",
                "adj_comfort_range_value"
            ],    
        ],
        "configuration_file": {
            "sparql_query": None,
            "graph_path": None,
            "price_identifier": None,
            "Tlimit_min": None,
            "Tlimit_max": None,
            "hvac_mode_type": None,
            "hvac_mode_identifier": None,
            "heat_signal_identifier": None,
            "cool_signal_identifier": None,
            "adj_comfort_range_flag": None,
            "adj_comfort_range_value": None,
        }
    }, 
    "zone_temp_shift_shed_price": {
        "description": 
                "Load shifting strategies refer to the ability to change the timing of electric demand, often moving consumption "
                "from peak periods to off-peak times. Shift is frequently implemented as a combination of a “take strategy” "
                "that increases energy consumption (e.g., pre-cooling in the morning) and a “shed strategy” (e.g., relaxing "
                "setpoints during the hot summer afternoons), which reduces energy use, compared to a baseline."
                "Pre-cooling or pre-heating a building to shift energy is more effective in high-mass buildings, "
                "where thermal inertia allows to slow down the temperature (rise or dip) when the setpoints are relaxed. "
                "The magnitude of the energy shifted is also a function of outside temperature, outside air flow rate, "
                "internal heat gain, and solar heat gains. \n"
                
                "The zone_temp_shift_shed_price application begins with a function that relaxes the comfort range for Demand Response (DR) "
                "event periods with customized offset values. Then, it includes a function that assesses the thermal comfort of different zones. "
                "If the zone temperature is within the expanded temperature band, it is considered eligible for DR control. "
                "When the zones are eligible, the control first evaluates the potential for load increase based on a combination of future price signals, "
                "occupancy patterns, and the current zone temperatures. The concept of “future” can be customized by setting a specific time horizon, "
                "indicating when the application can begin to check for appropriate conditions (e.g., 3 h before high-price periods). "
                "If, at this future time, the price surpasses a certain threshold, and the zone is expected to be occupied, while the "
                "current temperature remains within the comfort range, the function will recognize the need to start pre-heating or pre-cooling "
                "the building. Then, the application computes a new setpoint based on the current season and zone temperature setpoints."
                "Once the shift period finishe, another function evaluates the current grid signal and assesses if a load shed event has started "
                "(i.e., if the price is above a threshold estimated as the third quartile of the input price distribution). "
                "When the shed event is detected, the shed function computes new setpoints according to the current HVAC operation mode "
                "and the zone setpoints. If no shed event is detected or the zones are not eligible for DR controls, "
                "the application releases the control, which means it incrementally returns the setpoints to their baseline values.",      
        "flow_chart": control_flow_zone_temp_shift_shed_price,
        "performance": performance_zone_temp_shift_shed_price,
        "requirements": "@prefix brick: <https://brickschema.org/schema/Brick#> .\n"
                    "@prefix owl: <http://www.w3.org/2002/07/owl#> .\n"
                    "@prefix sh: <http://www.w3.org/ns/shacl#> .\n"
                    "@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n"
                    "@prefix ref: <https://brickschema.org/schema/Brick/ref#> .\n"
                    "@prefix constraint: <https://nrel.gov/BuildingMOTIF/constraints#> .\n"
                    "@prefix : <urn:zone_temp_shift_shed_price/> .\n"
                    "\n"
                    ": a owl:Ontology ;\n"
                    "    owl:imports <https://brickschema.org/schema/1.3/Brick> .\n"
                                
                    ":zone a sh:NodeShape, owl:Class ;\n"
                    "    sh:targetClass brick:Zone ;\n"
                    "    sh:property [ sh:path brick:hasPoint ;\n"
                    "            sh:qualifiedValueShape [sh:targetClass brick:Max_Air_Temperature_Setpoint];\n"
                    "            sh:qualifiedMinCount 1 ] ,\n"
                    "    [ sh:path brick:hasPoint ;\n"
                    "            sh:qualifiedValueShape [sh:targetClass brick:Min_Air_Temperature_Setpoint];\n"
                    "            sh:qualifiedMinCount 1  ] ,\n"
                    "    [ sh:path brick:hasPoint ;\n"
                    "            sh:qualifiedValueShape [sh:targetClass brick:Zone_Air_Temperature_Sensor];\n"
                    "            sh:qualifiedMinCount 1 ] ,\n"
                    "    [ sh:path brick:hasPoint ;\n"
                    "            sh:qualifiedValueShape [sh:targetClass brick:Occupancy_Sensor];\n"
                    "            sh:qualifiedMinCount 1 ] ; \n"            
                    "    sh:property [\n"
                    "        sh:path brick:hasPoint ;\n"
                    "        sh:qualifiedValueShape [ sh:or (\n"
                    "            [sh:targetClass brick:Zone_Air_Cooling_Temperature_Setpoint;]\n"
                    "            [sh:targetClass brick:Zone_Air_Heating_Temperature_Setpoint;] \n"
                    "            [sh:targetClass brick:Zone_Air_Temperature_Setpoint;] \n"
                    "        )] ;\n"
                    "        sh:qualifiedMinCount 1 ;\n"
                    "    ] ;\n"
                    ".\n"
                    "\n"
                    ":timeseries-identifier a sh:NodeShape ;\n"
                    "    sh:targetClass brick:Max_Air_Temperature_Setpoint,\n"
                    "                brick:Min_Air_Temperature_Setpoint,\n"
                    "                brick:Zone_Air_Temperature_Sensor,\n"
                    "                brick:Zone_Air_Cooling_Temperature_Setpoint,\n"
                    "                brick:Zone_Air_Heating_Temperature_Setpoint,\n"
                    "                brick:Zone_Air_Temperature_Setpoint,\n"
                    "                brick:Occupancy_Sensor;\n"
                    "\n"
                    "    sh:property [\n"
                    "        sh:path ref:hasExternalReference ; \n"
                    "        sh:minCount 1;\n"
                    "        sh:nodeKind sh:BlankNode ;\n"
                    "       sh:property [\n"
                    "            sh:path ref:hasTimeseriesId ; \n"
                    "            sh:minCount 1;\n"
                    "            sh:maxCount 1;\n"
                    "            sh:datatype xsd:string ;\n"
                    "        ] ;	\n"
                    "   ] ;\n"
                    ".\n",
        "download": download_zone_temp_shift_shed_price,
        "configuration": [
            [
                "text",
                "sparql_query"
            ],
            [
                "text",
                "graph_path"
            ],
            [
                "text",
                "price_identifier"
            ],
            [
                "slider",
                "Tlimit_min",
                {
                    "min": 0,
                    "max": 400,
                }
            ],   
            [
                "slider",
                "Tlimit_max",
                {
                    "min": 0,
                    "max": 400,
                }
            ],  
            [
                "multiple_choice",
                "hvac_mode_type",
                [
                    "Single HVAC control signal",
                    "Heating control signal",
                    "Cooling control signal"
                ]
            ],
            [
                "text",
                "hvac_mode_identifier"
            ],
            [
                "text",
                "heat_signal_identifier"
            ],
            [
                "text",
                "cool_signal_identifier"
            ],
            [
                "boolean",
                "adj_comfort_range_flag",
            ],  
            [
                "Number",
                "adj_comfort_range_value"
            ],    
            [
                "Number",
                "shift_horizon_time"
            ],     
        ],
        "configuration_file": {
            "sparql_query": None,
            "graph_path": None,
            "price_identifier": None,
            "Tlimit_min": None,
            "Tlimit_max": None,
            "hvac_mode_type": None,
            "hvac_mode_identifier": None,
            "heat_signal_identifier": None,
            "cool_signal_identifier": None,
            "adj_comfort_range_flag": None,
            "adj_comfort_range_value": None,
            "shift_horizon_time": None,
        }
    },
    "shed os_zone_temp_adjs_rat": {
        "description": "My description",
        "flow_chart": image,
        "performance": image,
        "requirements": "My requirements",
        "download": download,
        "configuration": [
        ],
        "configuration_file": {
        }
    }, 
    "shed os_zone_temp_adjs_dem_rat": {
        "description": "My description",
        "flow_chart": image,
        "performance": image,
        "requirements": "My requirements",
        "download": download,
        "configuration": [
        ],
        "configuration_file": {
        }
    },
    "shift os_zone_precool_sim": {
        "description": "My description",
        "flow_chart": image,
        "performance": image,
        "requirements": "My requirements",
        "download": download,
        "configuration": [
        ],
        "configuration_file": {
        }
    },
    "shift os_zone_precool_com": {
        "description": "My description",
        "flow_chart": image,
        "performance": image,
        "requirements": "My requirements",
        "download": download,
        "configuration": [
        ],
        "configuration_file": {
        }
    },
    "shed os_plant_chiller_water_temp_reset": {
        "description": "My description",
        "flow_chart": image,
        "performance": image,
        "requirements": "My requirements",
        "download": download,
        "configuration": [
        ],
        "configuration_file": {
        }
    },
    "shift/shed os_zone_precool_sim_temp_adjs_rat": {
        "description": "My description",
        "flow_chart": image,
        "performance": image,
        "requirements": "My requirements",
        "download": download,
        "configuration": [
        ],
        "configuration_file": {
        }
    }
}

# For "search"
def getControls():
    return apps

archtypes =  ["Residential buildings (e.g. split systems)", "Small commercial buildings (e.g. package units)", "Large commerical buildings (e.g. built-up systems)"]
targets = ["Zone level", "Distribution level",  "Plant level"]
zoneApps = ['zone_temp_shed_price' , 'zone_temp_shift_shed_price', 'shed os_zone_temp_adjs_rat', 'shed os_zone_temp_adjs_dem_rat', 'shift os_zone_precool_sim', 'shift/shed os_zone_precool_sim_temp_adjs_rat']
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

import copy

# For "results/configuration"
def getConfigurationFiles(control_name, configs):
    appsDup = copy.deepcopy(apps)[control_name]
    expected = appsDup["configuration"]
    for key, value in configs.items():
        try:
            index = -1
            for i, item in enumerate(expected):
                if item[1] == key:
                    index = i

            type = expected[index][0]
            if (type == 'text' or  type == 'radio' or type == 'Number') and value == '':
                value = None
            elif type == 'boolean' and value == 'on':
                value = True

            appsDup['configuration_file'][key] = value
        except Exception as e:
            # Ignored
            2 + 2

    for i, item in enumerate(expected):
        if item[0] == 'boolean' and item[1] not in configs.keys():
            appsDup['configuration_file'][item[1]] = False

    return appsDup["configuration_file"]
