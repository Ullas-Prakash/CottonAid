"""
Treatment Database for Cotton Disease Management
Comprehensive database of treatments, prevention methods, and remedies
"""

# Comprehensive treatment database
TREATMENT_DATABASE = {
    'Fusarium Wilt': {
        'urgency': 'high',
        'description': 'Soil-borne fungal disease causing vascular wilt and plant death',
        'chemical_treatments': [
            {
                'product': 'Carbendazim',
                'active_ingredient': 'Carbendazim 50% WP',
                'dosage': '2g/L water',
                'application': 'Soil drench around root zone',
                'timing': 'At first sign of symptoms, repeat after 15 days',
                'precautions': 'Avoid application during flowering'
            },
            {
                'product': 'Thiophanate-methyl',
                'active_ingredient': 'Thiophanate-methyl 70% WP',
                'dosage': '1.5g/L water',
                'application': 'Foliar spray and soil application',
                'timing': 'Preventive application before disease onset',
                'precautions': 'Use protective equipment during application'
            }
        ],
        'organic_treatments': [
            {
                'method': 'Soil Solarization',
                'procedure': 'Cover soil with clear plastic sheets for 4-6 weeks during hot weather',
                'timing': 'Before planting season (summer months)',
                'effectiveness': 'Reduces soil-borne fungal population by 80-90%'
            },
            {
                'method': 'Trichoderma Application',
                'procedure': 'Apply Trichoderma viride @ 5g/kg seed or 2.5kg/ha soil',
                'timing': 'Seed treatment or soil application before sowing',
                'effectiveness': 'Biological control agent, 60-70% disease reduction'
            },
            {
                'method': 'Neem Cake Amendment',
                'procedure': 'Mix neem cake @ 200kg/ha into soil',
                'timing': '2-3 weeks before planting',
                'effectiveness': 'Improves soil health and reduces fungal load'
            }
        ],
        'prevention': [
            'Use certified disease-free seeds',
            'Plant resistant cotton varieties (e.g., Bt cotton with Fusarium resistance)',
            'Implement crop rotation with non-host crops (cereals, legumes)',
            'Improve soil drainage and avoid waterlogging',
            'Maintain proper plant spacing for air circulation',
            'Remove and destroy infected plant debris',
            'Avoid excessive nitrogen fertilization'
        ],
        'cultural_practices': [
            'Deep summer plowing to expose fungal structures to heat',
            'Balanced fertilization with emphasis on potassium',
            'Drip irrigation to avoid soil splash',
            'Regular field monitoring for early detection'
        ]
    },
    
    'Leaf Curl Disease': {
        'urgency': 'high',
        'description': 'Viral disease transmitted by whiteflies causing leaf curling and stunting',
        'chemical_treatments': [
            {
                'product': 'Imidacloprid',
                'active_ingredient': 'Imidacloprid 17.8% SL',
                'dosage': '0.5ml/L water',
                'application': 'Foliar spray targeting whitefly vectors',
                'timing': 'At first appearance of whiteflies, repeat every 10-15 days',
                'precautions': 'Avoid spraying during bee activity hours'
            },
            {
                'product': 'Thiamethoxam',
                'active_ingredient': 'Thiamethoxam 25% WG',
                'dosage': '0.4g/L water',
                'application': 'Foliar spray for whitefly control',
                'timing': 'Early morning or evening application',
                'precautions': 'Rotate with different mode of action insecticides'
            }
        ],
        'organic_treatments': [
            {
                'method': 'Neem Oil Spray',
                'procedure': 'Apply neem oil @ 5ml/L water with surfactant',
                'timing': 'Weekly applications during whitefly season',
                'effectiveness': 'Repels whiteflies and disrupts feeding'
            },
            {
                'method': 'Yellow Sticky Traps',
                'procedure': 'Install yellow sticky traps @ 25-30 traps/ha',
                'timing': 'From seedling stage throughout growing season',
                'effectiveness': 'Monitors and reduces whitefly population'
            },
            {
                'method': 'Reflective Mulch',
                'procedure': 'Use silver reflective mulch around plants',
                'timing': 'At planting time',
                'effectiveness': 'Confuses and repels whiteflies'
            }
        ],
        'prevention': [
            'Plant virus-resistant cotton varieties',
            'Use virus-free planting material',
            'Control weeds that serve as alternate hosts',
            'Install fine mesh barriers in nurseries',
            'Avoid planting near infected fields',
            'Remove and destroy infected plants immediately',
            'Implement vector management strategies'
        ],
        'cultural_practices': [
            'Early planting to avoid peak whitefly season',
            'Proper plant spacing to reduce humidity',
            'Regular monitoring with yellow sticky traps',
            'Quarantine measures for new plants'
        ]
    },
    
    'Bacterial Blight': {
        'urgency': 'medium',
        'description': 'Bacterial disease causing angular leaf spots and stem cankers',
        'chemical_treatments': [
            {
                'product': 'Copper Oxychloride',
                'active_ingredient': 'Copper Oxychloride 50% WP',
                'dosage': '3g/L water',
                'application': 'Foliar spray covering all plant parts',
                'timing': 'At first symptom appearance, repeat every 10 days',
                'precautions': 'Avoid copper buildup in soil with repeated use'
            },
            {
                'product': 'Streptomycin Sulfate',
                'active_ingredient': 'Streptomycin Sulfate 90% + Tetracycline 10%',
                'dosage': '0.5g/L water',
                'application': 'Foliar spray during cool, humid conditions',
                'timing': 'Preventive application before disease onset',
                'precautions': 'Use only when necessary to prevent resistance'
            }
        ],
        'organic_treatments': [
            {
                'method': 'Bordeaux Mixture',
                'procedure': 'Apply Bordeaux mixture (1% solution)',
                'timing': 'Preventive sprays during humid weather',
                'effectiveness': 'Traditional copper-based bactericide'
            },
            {
                'method': 'Pseudomonas Application',
                'procedure': 'Apply Pseudomonas fluorescens @ 10g/L water',
                'timing': 'Seed treatment and foliar application',
                'effectiveness': 'Biological control with 50-60% efficacy'
            }
        ],
        'prevention': [
            'Use certified pathogen-free seeds',
            'Treat seeds with hot water (50°C for 25 minutes)',
            'Avoid overhead irrigation',
            'Remove infected plant debris',
            'Implement crop rotation',
            'Avoid working in wet fields',
            'Disinfect tools between plants'
        ],
        'cultural_practices': [
            'Plant in well-drained soils',
            'Avoid excessive nitrogen fertilization',
            'Maintain proper plant spacing',
            'Remove weeds that harbor bacteria'
        ]
    },
    
    'Verticillium Wilt': {
        'urgency': 'medium',
        'description': 'Soil-borne fungal disease causing vascular discoloration and wilting',
        'chemical_treatments': [
            {
                'product': 'Propiconazole',
                'active_ingredient': 'Propiconazole 25% EC',
                'dosage': '1ml/L water',
                'application': 'Soil drench and foliar spray',
                'timing': 'Early season application before symptom development',
                'precautions': 'Avoid application during hot weather'
            }
        ],
        'organic_treatments': [
            {
                'method': 'Compost Amendment',
                'procedure': 'Incorporate well-decomposed compost @ 5-10 tons/ha',
                'timing': 'Before planting season',
                'effectiveness': 'Improves soil biology and suppresses disease'
            },
            {
                'method': 'Biocontrol Agents',
                'procedure': 'Apply Trichoderma harzianum @ 2.5kg/ha',
                'timing': 'Soil application before planting',
                'effectiveness': 'Competitive exclusion of pathogen'
            }
        ],
        'prevention': [
            'Plant resistant varieties when available',
            'Avoid planting in heavily infested soils',
            'Implement long crop rotations (4-6 years)',
            'Control root-knot nematodes',
            'Maintain optimal soil pH (6.0-7.5)',
            'Avoid soil compaction',
            'Use clean cultivation equipment'
        ],
        'cultural_practices': [
            'Deep plowing to bury infected debris',
            'Balanced fertilization avoiding excess nitrogen',
            'Adequate irrigation without waterlogging',
            'Regular soil testing for pathogen presence'
        ]
    },
    
    'Alternaria Leaf Spot': {
        'urgency': 'medium',
        'description': 'Fungal disease causing circular brown spots with concentric rings',
        'chemical_treatments': [
            {
                'product': 'Mancozeb',
                'active_ingredient': 'Mancozeb 75% WP',
                'dosage': '2.5g/L water',
                'application': 'Foliar spray with good coverage',
                'timing': 'At first spot appearance, repeat every 10-14 days',
                'precautions': 'Use sticker-spreader for better coverage'
            },
            {
                'product': 'Azoxystrobin',
                'active_ingredient': 'Azoxystrobin 23% SC',
                'dosage': '1ml/L water',
                'application': 'Foliar spray during humid conditions',
                'timing': 'Preventive application before disease onset',
                'precautions': 'Rotate with different fungicide groups'
            }
        ],
        'organic_treatments': [
            {
                'method': 'Baking Soda Spray',
                'procedure': 'Mix 5g baking soda + 2ml liquid soap per liter water',
                'timing': 'Weekly applications during humid weather',
                'effectiveness': 'Changes leaf surface pH, inhibits fungal growth'
            },
            {
                'method': 'Garlic Extract',
                'procedure': 'Apply garlic extract @ 20ml/L water',
                'timing': 'Bi-weekly applications as preventive measure',
                'effectiveness': 'Natural antifungal properties'
            }
        ],
        'prevention': [
            'Remove infected leaves and debris',
            'Ensure good air circulation',
            'Avoid overhead watering',
            'Plant in well-drained locations',
            'Apply balanced fertilization',
            'Monitor humidity levels',
            'Use disease-free planting material'
        ],
        'cultural_practices': [
            'Proper plant spacing for air movement',
            'Morning watering to allow leaves to dry',
            'Regular field sanitation',
            'Avoid working in wet fields'
        ]
    },
    
    'Anthracnose': {
        'urgency': 'medium',
        'description': 'Fungal disease causing reddish-brown lesions on stems, leaves, and bolls',
        'chemical_treatments': [
            {
                'product': 'Chlorothalonil',
                'active_ingredient': 'Chlorothalonil 75% WP',
                'dosage': '2g/L water',
                'application': 'Foliar spray with thorough coverage',
                'timing': 'At first lesion appearance, repeat every 14 days',
                'precautions': 'Avoid drift to non-target crops'
            }
        ],
        'organic_treatments': [
            {
                'method': 'Copper Soap Spray',
                'procedure': 'Mix copper soap @ 3ml/L water',
                'timing': 'Preventive applications during humid periods',
                'effectiveness': 'Organic copper formulation for disease control'
            }
        ],
        'prevention': [
            'Use certified disease-free seeds',
            'Treat seeds with fungicide',
            'Remove infected plant debris',
            'Avoid overhead irrigation',
            'Maintain proper plant nutrition',
            'Implement crop rotation',
            'Control weeds and alternate hosts'
        ],
        'cultural_practices': [
            'Plant in well-ventilated areas',
            'Avoid excessive nitrogen fertilization',
            'Regular field inspection',
            'Prompt removal of infected materials'
        ]
    },
    
    'Black Root Rot': {
        'urgency': 'high',
        'description': 'Soil-borne fungal disease causing black root lesions and stunted growth',
        'chemical_treatments': [
            {
                'product': 'Metalaxyl',
                'active_ingredient': 'Metalaxyl 35% WS',
                'dosage': '2g/kg seed',
                'application': 'Seed treatment before planting',
                'timing': 'Pre-planting seed treatment',
                'precautions': 'Store treated seeds in cool, dry place'
            }
        ],
        'organic_treatments': [
            {
                'method': 'Beneficial Microorganisms',
                'procedure': 'Apply mycorrhizal fungi inoculant @ 10g/kg seed',
                'timing': 'Seed treatment or transplant application',
                'effectiveness': 'Enhances root health and disease resistance'
            },
            {
                'method': 'Organic Matter Addition',
                'procedure': 'Incorporate compost @ 10-15 tons/ha',
                'timing': 'Before planting season',
                'effectiveness': 'Improves soil structure and microbial activity'
            }
        ],
        'prevention': [
            'Improve soil drainage',
            'Avoid overwatering',
            'Use raised beds in heavy soils',
            'Implement crop rotation with grasses',
            'Maintain soil pH between 6.0-7.0',
            'Avoid soil compaction',
            'Use pathogen-free planting material'
        ],
        'cultural_practices': [
            'Deep tillage to improve drainage',
            'Organic matter incorporation',
            'Controlled irrigation scheduling',
            'Regular root health monitoring'
        ]
    },
    
    'Powdery Mildew': {
        'urgency': 'low',
        'description': 'Fungal disease creating white powdery growth on leaves and stems',
        'chemical_treatments': [
            {
                'product': 'Sulfur',
                'active_ingredient': 'Wettable Sulfur 80% WP',
                'dosage': '3g/L water',
                'application': 'Foliar spray covering all plant surfaces',
                'timing': 'At first white powdery appearance, repeat every 10 days',
                'precautions': 'Avoid application during hot weather (>30°C)'
            },
            {
                'product': 'Myclobutanil',
                'active_ingredient': 'Myclobutanil 10% WP',
                'dosage': '1g/L water',
                'application': 'Foliar spray during cool, humid conditions',
                'timing': 'Preventive application before disease onset',
                'precautions': 'Rotate with different fungicide modes of action'
            }
        ],
        'organic_treatments': [
            {
                'method': 'Milk Spray',
                'procedure': 'Mix 1 part milk with 9 parts water',
                'timing': 'Weekly applications during humid weather',
                'effectiveness': 'Proteins in milk have antifungal properties'
            },
            {
                'method': 'Potassium Bicarbonate',
                'procedure': 'Apply potassium bicarbonate @ 5g/L water',
                'timing': 'Bi-weekly applications as preventive measure',
                'effectiveness': 'Alters leaf surface pH, inhibits fungal growth'
            }
        ],
        'prevention': [
            'Ensure good air circulation',
            'Avoid overhead watering',
            'Remove infected plant parts',
            'Plant in sunny locations',
            'Avoid excessive nitrogen fertilization',
            'Maintain proper plant spacing',
            'Monitor humidity levels'
        ],
        'cultural_practices': [
            'Pruning for better air flow',
            'Morning watering to allow drying',
            'Regular field sanitation',
            'Balanced fertilization program'
        ]
    },
    
    'Target Spot': {
        'urgency': 'medium',
        'description': 'Fungal disease producing circular spots with concentric rings',
        'chemical_treatments': [
            {
                'product': 'Tebuconazole',
                'active_ingredient': 'Tebuconazole 25.9% EC',
                'dosage': '1ml/L water',
                'application': 'Foliar spray with good coverage',
                'timing': 'At first spot appearance, repeat every 14 days',
                'precautions': 'Avoid application during flowering'
            }
        ],
        'organic_treatments': [
            {
                'method': 'Compost Tea',
                'procedure': 'Apply compost tea @ 100ml/L water',
                'timing': 'Weekly applications during growing season',
                'effectiveness': 'Beneficial microorganisms suppress disease'
            }
        ],
        'prevention': [
            'Remove infected plant debris',
            'Avoid overhead irrigation',
            'Ensure proper plant spacing',
            'Implement crop rotation',
            'Use disease-resistant varieties',
            'Maintain field sanitation',
            'Monitor weather conditions'
        ],
        'cultural_practices': [
            'Deep plowing to bury debris',
            'Balanced nutrition program',
            'Regular field monitoring',
            'Timely harvest to reduce inoculum'
        ]
    },
    
    'Healthy Plant': {
        'urgency': 'none',
        'description': 'Plant appears healthy with no visible disease symptoms',
        'chemical_treatments': [],
        'organic_treatments': [],
        'prevention': [
            'Continue regular monitoring',
            'Maintain good cultural practices',
            'Ensure balanced nutrition',
            'Proper irrigation management',
            'Regular field sanitation',
            'Monitor for early disease signs'
        ],
        'cultural_practices': [
            'Regular field inspection',
            'Preventive spray programs',
            'Soil health maintenance',
            'Integrated pest management'
        ]
    },
    
    'Healthy Leaf': {
        'urgency': 'none',
        'description': 'Leaf appears healthy with no visible disease symptoms',
        'chemical_treatments': [],
        'organic_treatments': [],
        'prevention': [
            'Continue monitoring for disease development',
            'Maintain optimal growing conditions',
            'Ensure proper plant nutrition',
            'Regular field sanitation',
            'Preventive disease management'
        ],
        'cultural_practices': [
            'Regular leaf inspection',
            'Proper irrigation practices',
            'Balanced fertilization',
            'Environmental monitoring'
        ]
    }
}

def get_treatment_info(disease_name):
    """Get comprehensive treatment information for a specific disease"""
    return TREATMENT_DATABASE.get(disease_name, {})

def get_urgency_level(disease_name):
    """Get urgency level for a specific disease"""
    treatment_info = TREATMENT_DATABASE.get(disease_name, {})
    return treatment_info.get('urgency', 'unknown')

def get_all_treatments_for_disease(disease_name):
    """Get all treatment options for a specific disease"""
    return TREATMENT_DATABASE.get(disease_name, {})