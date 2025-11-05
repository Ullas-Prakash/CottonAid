"""
Pest Database for Cotton Disease Detection
Contains comprehensive disease-to-pest mappings and pest information
"""

# Comprehensive disease-to-pest mapping database
DISEASE_PEST_MAPPING = {
    'Fusarium Wilt': [
        {
            'pest_name': 'Fusarium oxysporum',
            'scientific_name': 'Fusarium oxysporum f. sp. vasinfectum',
            'pest_type': 'fungus',
            'confidence': 0.95,
            'lifecycle_info': 'Soil-borne fungus that survives in soil for many years as chlamydospores',
            'damage_description': 'Causes vascular wilt, yellowing, and eventual plant death'
        },
        {
            'pest_name': 'Root-knot nematodes',
            'scientific_name': 'Meloidogyne incognita',
            'pest_type': 'nematode',
            'confidence': 0.3,
            'lifecycle_info': 'Microscopic roundworms that attack plant roots',
            'damage_description': 'Creates entry wounds that facilitate Fusarium infection'
        }
    ],
    
    'Leaf Curl Disease': [
        {
            'pest_name': 'Silverleaf Whitefly',
            'scientific_name': 'Bemisia tabaci',
            'pest_type': 'insect',
            'confidence': 0.98,
            'lifecycle_info': 'Complete metamorphosis: egg, 4 nymphal stages, adult (21-25 days)',
            'damage_description': 'Vector for Cotton Leaf Curl Virus, causes leaf curling and stunting'
        }
    ],
    
    'Bacterial Blight': [
        {
            'pest_name': 'Bacterial Blight Pathogen',
            'scientific_name': 'Xanthomonas citri pv. malvacearum',
            'pest_type': 'bacteria',
            'confidence': 0.92,
            'lifecycle_info': 'Survives in infected plant debris and seeds',
            'damage_description': 'Causes angular leaf spots, stem cankers, and boll rot'
        }
    ],
    
    'Verticillium Wilt': [
        {
            'pest_name': 'Verticillium Fungus',
            'scientific_name': 'Verticillium dahliae',
            'pest_type': 'fungus',
            'confidence': 0.90,
            'lifecycle_info': 'Soil-borne fungus forming microsclerotia that survive in soil',
            'damage_description': 'Causes vascular discoloration, wilting, and defoliation'
        }
    ],
    
    'Alternaria Leaf Spot': [
        {
            'pest_name': 'Alternaria Fungus',
            'scientific_name': 'Alternaria macrospora',
            'pest_type': 'fungus',
            'confidence': 0.88,
            'lifecycle_info': 'Survives on plant debris, spreads via wind-borne conidia',
            'damage_description': 'Creates circular to irregular brown spots with concentric rings'
        }
    ],
    
    'Anthracnose': [
        {
            'pest_name': 'Colletotrichum Fungus',
            'scientific_name': 'Colletotrichum gossypii',
            'pest_type': 'fungus',
            'confidence': 0.85,
            'lifecycle_info': 'Survives in infected plant debris and seeds',
            'damage_description': 'Causes reddish-brown lesions on stems, leaves, and bolls'
        }
    ],
    
    'Black Root Rot': [
        {
            'pest_name': 'Thielaviopsis Fungus',
            'scientific_name': 'Thielaviopsis basicola',
            'pest_type': 'fungus',
            'confidence': 0.87,
            'lifecycle_info': 'Soil-borne fungus that produces chlamydospores',
            'damage_description': 'Causes black lesions on roots and stunted plant growth'
        }
    ],
    
    'Powdery Mildew': [
        {
            'pest_name': 'Powdery Mildew Fungus',
            'scientific_name': 'Erysiphe cichoracearum',
            'pest_type': 'fungus',
            'confidence': 0.93,
            'lifecycle_info': 'Obligate parasite that overwinters as cleistothecia',
            'damage_description': 'Creates white powdery growth on leaves and stems'
        }
    ],
    
    'Target Spot': [
        {
            'pest_name': 'Corynespora Fungus',
            'scientific_name': 'Corynespora cassiicola',
            'pest_type': 'fungus',
            'confidence': 0.89,
            'lifecycle_info': 'Survives in plant debris, spreads via wind and rain splash',
            'damage_description': 'Produces circular spots with concentric rings resembling targets'
        }
    ],
    
    'Healthy Plant': [],
    'Healthy Leaf': []
}

# Additional pest information database
PEST_DETAILS = {
    'Fusarium oxysporum': {
        'optimal_conditions': 'Warm temperatures (25-30°C), high soil moisture',
        'spread_method': 'Soil-borne, water movement, contaminated tools',
        'host_range': 'Cotton, tomato, watermelon, and other crops',
        'economic_impact': 'Major yield losses, can destroy entire fields'
    },
    
    'Bemisia tabaci': {
        'optimal_conditions': 'Warm temperatures (25-30°C), low humidity',
        'spread_method': 'Flying adults, wind dispersal',
        'host_range': 'Over 600 plant species including cotton, tomato, cucumber',
        'economic_impact': 'Direct feeding damage plus virus transmission'
    },
    
    'Xanthomonas citri pv. malvacearum': {
        'optimal_conditions': 'Warm, humid conditions with frequent rainfall',
        'spread_method': 'Wind-driven rain, contaminated seeds and tools',
        'host_range': 'Cotton and related Malvaceae family plants',
        'economic_impact': 'Significant yield and quality losses'
    },
    
    'Verticillium dahliae': {
        'optimal_conditions': 'Cool to moderate temperatures (20-25°C)',
        'spread_method': 'Soil-borne, irrigation water, farm equipment',
        'host_range': 'Over 200 plant species including cotton, potato, tomato',
        'economic_impact': 'Chronic yield losses, reduced fiber quality'
    },
    
    'Alternaria macrospora': {
        'optimal_conditions': 'Warm temperatures with high humidity',
        'spread_method': 'Wind-borne spores, rain splash',
        'host_range': 'Cotton and other Gossypium species',
        'economic_impact': 'Defoliation leading to reduced yield and quality'
    },
    
    'Colletotrichum gossypii': {
        'optimal_conditions': 'Warm, humid conditions',
        'spread_method': 'Rain splash, contaminated seeds',
        'host_range': 'Cotton, okra, and other Malvaceae',
        'economic_impact': 'Boll rot and seedling mortality'
    },
    
    'Thielaviopsis basicola': {
        'optimal_conditions': 'Cool temperatures (15-20°C), wet soils',
        'spread_method': 'Soil-borne, contaminated transplants',
        'host_range': 'Cotton, tobacco, beans, and other crops',
        'economic_impact': 'Stunted growth and reduced root system'
    },
    
    'Erysiphe cichoracearum': {
        'optimal_conditions': 'Moderate temperatures with high humidity',
        'spread_method': 'Wind-borne conidia',
        'host_range': 'Cotton, cucurbits, and many other plants',
        'economic_impact': 'Reduced photosynthesis and plant vigor'
    },
    
    'Corynespora cassiicola': {
        'optimal_conditions': 'Warm, humid conditions',
        'spread_method': 'Wind-borne conidia, rain splash',
        'host_range': 'Cotton, soybean, cucumber, and many others',
        'economic_impact': 'Defoliation and reduced yield'
    }
}

def get_pest_info(pest_name):
    """Get detailed information about a specific pest"""
    return PEST_DETAILS.get(pest_name, {})

def get_all_pests_for_disease(disease_name):
    """Get all pests associated with a specific disease"""
    return DISEASE_PEST_MAPPING.get(disease_name, [])