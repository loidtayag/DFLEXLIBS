image = 'controls/demo/myImage.png'
download = ['controls/demo/myControl.py']

download_shed_zone_temp_adjs = ['controls/hvac/sequences/python/strategies/stra_zone_temp_shed_price.py', 
                                'controls/hvac/sequences/python/functions/fu_ashrae_TSet_adjust.py',
                                'controls/hvac/sequences/python/functions/fu_runaway_condition.py',
                                'controls/hvac/sequences/python/functions/fu_runaway_TsetCooZon.py',
                                'controls/hvac/sequences/python/functions/fu_runaway_TsetHeaZon.py',
                                'controls/hvac/sequences/python/functions/fu_shed_price_event.py',
                                'controls/hvac/sequences/python/functions/fu_shed_TsetCooZon.py',
                                'controls/hvac/sequences/python/functions/fu_shed_TsetHeaZon.py',
]

chart_shed_zone_temp_adjs = 'controls/demo/chart_shed_zone_temp_adjs.png'
performance_shed_zone_temp_adjs = 'controls/demo/performance_shed_zone_temp_adjs.png'


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
        "requirements": "@prefix brick: <https://brickschema.org/schema/Brick#> .\n"
                    "@prefix owl: <http://www.w3.org/2002/07/owl#> .\n"
                    "@prefix sh: <http://www.w3.org/ns/shacl#> ."
                    "@prefix xsd: <http://www.w3.org/2001/XMLSchema#> ."
                    "@prefix ref: <https://brickschema.org/schema/Brick/ref#> ."
                    "@prefix constraint: <https://nrel.gov/BuildingMOTIF/constraints#> ."
                    "@prefix : <urn:shed_zone_temp_adjs/> ."

                    ": a owl:Ontology ;"
                    "    owl:imports <https://brickschema.org/schema/1.3/Brick> ."
                                
                    ":zone a sh:NodeShape, owl:Class ;"
                    "    sh:targetClass brick:Zone ;"
                    "    sh:property [ sh:path brick:hasPoint ;"
                    "            sh:qualifiedValueShape [sh:targetClass brick:Max_Air_Temperature_Setpoint];"
                    "            sh:qualifiedMinCount 1 ] ,"
                    "    [ sh:path brick:hasPoint ;"
                    "            sh:qualifiedValueShape [sh:targetClass brick:Min_Air_Temperature_Setpoint];"
                    "            sh:qualifiedMinCount 1  ] ,"
                    "    [ sh:path brick:hasPoint ;"
                    "            sh:qualifiedValueShape [sh:targetClass brick:Zone_Air_Temperature_Sensor];"
                    "            sh:qualifiedMinCount 1 ] ,"
                    "    [ sh:path brick:hasPoint ;"
                    "            sh:qualifiedValueShape [sh:targetClass brick:Occupancy_Sensor];"
                    "            sh:qualifiedMinCount 1 ] ;            "
                    "    sh:property ["
                    "        sh:path brick:hasPoint ;"
                    "        sh:qualifiedValueShape [ sh:or ("
                    "            [sh:targetClass brick:Zone_Air_Cooling_Temperature_Setpoint;]"
                    "            [sh:targetClass brick:Zone_Air_Heating_Temperature_Setpoint;] "
                    "            [sh:targetClass brick:Zone_Air_Temperature_Setpoint;] "
                    "        )] ;"
                    "        sh:qualifiedMinCount 1 ;"
                    "    ] ;"
                    "."

                    ":timeseries-identifier a sh:NodeShape ;"
                    "    sh:targetClass brick:Max_Air_Temperature_Setpoint,"
                    "                brick:Min_Air_Temperature_Setpoint,"
                    "                brick:Zone_Air_Temperature_Sensor,"
                    "                brick:Zone_Air_Cooling_Temperature_Setpoint,"
                    "                brick:Zone_Air_Heating_Temperature_Setpoint,"
                    "                brick:Zone_Air_Temperature_Setpoint,"
                    "                brick:Occupancy_Sensor;"

                    "    sh:property ["
                    "        sh:path ref:hasExternalReference ; "
                    "        sh:minCount 1;"
                    "        sh:nodeKind sh:BlankNode ;"
                    "       sh:property ["
                    "            sh:path ref:hasTimeseriesId ; "
                    "            sh:minCount 1;"
                    "            sh:maxCount 1;"
                    "            sh:datatype xsd:string ;"
                    "        ] ;	"
                    "   ] ;"
                    ".",
        "download": download_shed_zone_temp_adjs,
        "configuration": [
            [
                "choice",
                "graph_path",
                [
                    "apples",
                    "oranges"
                ]
            ],
            [
                "text",
                "sparql_query"
            ],
            [
                "slider",
                "myNumber",
                {
                    "min": 2,
                    "max": 5,
                }
            ],   
            [
                "number",
                "myNumber",
                {
                    "min": 2,
                    "max": 5,
                }
            ],           
        ],
        "configuration_file": {
            "sparql_query": None,
            "myNumber:": None,
            "graph_path": None,
            "myOtherNumber": None
        }
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
def getConfigurationFiles(control_name, configs):
    apps[control_name]["configuration_file"]['sparql_query'] = configs[1]
    apps[control_name]["configuration_file"]['myNumber'] = configs[2]
    apps[control_name]["configuration_file"]['graph_path'] = configs[0]
    apps[control_name]["configuration_file"]['myOtherNumber'] = configs[3]

    return apps[control_name]["configuration_file"]
