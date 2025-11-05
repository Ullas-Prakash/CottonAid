"""
Remedy Engine for Cotton Disease Management
Provides treatment recommendations based on disease and pest information
"""
from .treatment_database import TREATMENT_DATABASE, get_treatment_info, get_urgency_level
import datetime

class RemedyEngine:
    def __init__(self):
        self.treatment_db = TREATMENT_DATABASE
        
    def get_treatment_recommendations(self, disease_name, pest_info=None, disease_confidence=1.0):
        """
        Get comprehensive treatment recommendations for identified disease
        
        Args:
            disease_name (str): Name of the identified disease
            pest_info (list): List of predicted pests
            disease_confidence (float): Confidence score of disease prediction
            
        Returns:
            dict: Comprehensive treatment recommendations
        """
        if disease_name not in self.treatment_db:
            return self._get_default_recommendations()
        
        treatment_info = self.treatment_db[disease_name].copy()
        
        # Calculate urgency based on disease confidence and pest information
        urgency = self._calculate_urgency(disease_name, disease_confidence, pest_info)
        treatment_info['calculated_urgency'] = urgency
        
        # Add pest-specific recommendations if available
        if pest_info:
            treatment_info['pest_specific_treatments'] = self._get_pest_specific_treatments(pest_info)
        
        # Add timing recommendations
        treatment_info['application_timing'] = self._get_application_timing(disease_name, urgency)
        
        # Add cost-effectiveness analysis
        treatment_info['cost_analysis'] = self._analyze_treatment_costs(treatment_info)
        
        # Add environmental considerations
        treatment_info['environmental_impact'] = self._assess_environmental_impact(treatment_info)
        
        return treatment_info
    
    def _calculate_urgency(self, disease_name, disease_confidence, pest_info):
        """Calculate treatment urgency based on multiple factors"""
        base_urgency = get_urgency_level(disease_name)
        
        urgency_scores = {
            'none': 0,
            'low': 1,
            'medium': 2,
            'high': 3
        }
        
        base_score = urgency_scores.get(base_urgency, 1)
        
        # Adjust based on disease confidence
        if disease_confidence >= 0.9:
            confidence_modifier = 1.2
        elif disease_confidence >= 0.7:
            confidence_modifier = 1.0
        else:
            confidence_modifier = 0.8
        
        # Adjust based on pest information
        pest_modifier = 1.0
        if pest_info:
            high_confidence_pests = [p for p in pest_info if p.get('confidence', 0) >= 0.8]
            if high_confidence_pests:
                pest_modifier = 1.3
            elif any(p.get('confidence', 0) >= 0.6 for p in pest_info):
                pest_modifier = 1.1
        
        final_score = base_score * confidence_modifier * pest_modifier
        
        # Convert back to urgency level
        if final_score >= 3.5:
            return 'critical'
        elif final_score >= 2.5:
            return 'high'
        elif final_score >= 1.5:
            return 'medium'
        elif final_score >= 0.5:
            return 'low'
        else:
            return 'none'
    
    def _get_pest_specific_treatments(self, pest_info):
        """Get treatments specific to identified pests"""
        pest_treatments = []
        
        for pest in pest_info:
            pest_type = pest.get('pest_type', 'unknown')
            pest_name = pest.get('pest_name', 'Unknown')
            
            if pest_type == 'insect':
                pest_treatments.append({
                    'target': pest_name,
                    'treatment_type': 'Insecticide',
                    'recommendations': [
                        'Use systemic insecticides for sucking pests',
                        'Apply contact insecticides for chewing pests',
                        'Consider biological control agents',
                        'Implement integrated pest management'
                    ]
                })
            elif pest_type == 'fungus':
                pest_treatments.append({
                    'target': pest_name,
                    'treatment_type': 'Fungicide',
                    'recommendations': [
                        'Use preventive fungicide applications',
                        'Ensure good spray coverage',
                        'Rotate fungicide modes of action',
                        'Improve cultural practices'
                    ]
                })
            elif pest_type == 'bacteria':
                pest_treatments.append({
                    'target': pest_name,
                    'treatment_type': 'Bactericide',
                    'recommendations': [
                        'Use copper-based bactericides',
                        'Apply during cool, humid conditions',
                        'Implement sanitation measures',
                        'Use resistant varieties when available'
                    ]
                })
            elif pest_type == 'virus':
                pest_treatments.append({
                    'target': pest_name,
                    'treatment_type': 'Vector Control',
                    'recommendations': [
                        'Control insect vectors',
                        'Remove infected plants immediately',
                        'Use virus-resistant varieties',
                        'Implement quarantine measures'
                    ]
                })
        
        return pest_treatments
    
    def _get_application_timing(self, disease_name, urgency):
        """Get specific timing recommendations for treatments"""
        current_time = datetime.datetime.now()
        
        timing_recommendations = {
            'critical': {
                'immediate_action': 'Apply treatment within 24 hours',
                'follow_up': 'Monitor daily, retreat if necessary after 7 days',
                'best_time': 'Early morning or late evening to avoid heat stress'
            },
            'high': {
                'immediate_action': 'Apply treatment within 2-3 days',
                'follow_up': 'Monitor every 2-3 days, retreat after 10-14 days if needed',
                'best_time': 'Early morning or late evening'
            },
            'medium': {
                'immediate_action': 'Apply treatment within 1 week',
                'follow_up': 'Monitor weekly, retreat after 14-21 days if needed',
                'best_time': 'Morning hours when dew has dried'
            },
            'low': {
                'immediate_action': 'Consider treatment within 2 weeks',
                'follow_up': 'Monitor bi-weekly, apply preventive measures',
                'best_time': 'Any time during favorable weather'
            },
            'none': {
                'immediate_action': 'Continue monitoring',
                'follow_up': 'Maintain preventive practices',
                'best_time': 'N/A'
            }
        }
        
        base_timing = timing_recommendations.get(urgency, timing_recommendations['medium'])
        
        # Add seasonal considerations
        month = current_time.month
        if month in [6, 7, 8]:  # Summer months
            base_timing['seasonal_note'] = 'Avoid midday applications due to heat. Ensure adequate water for plant recovery.'
        elif month in [12, 1, 2]:  # Winter months
            base_timing['seasonal_note'] = 'Apply during warmer parts of the day. Allow time for drying before evening.'
        elif month in [3, 4, 5, 9, 10, 11]:  # Spring/Fall
            base_timing['seasonal_note'] = 'Optimal conditions for most treatments. Monitor weather forecasts.'
        
        return base_timing
    
    def _analyze_treatment_costs(self, treatment_info):
        """Analyze cost-effectiveness of different treatment options"""
        cost_analysis = {
            'chemical_treatments': {
                'cost_level': 'medium-high',
                'effectiveness': 'high',
                'notes': 'Higher upfront cost but quick results'
            },
            'organic_treatments': {
                'cost_level': 'low-medium',
                'effectiveness': 'medium',
                'notes': 'Lower cost, environmentally friendly, may require multiple applications'
            },
            'prevention': {
                'cost_level': 'low',
                'effectiveness': 'high',
                'notes': 'Most cost-effective long-term strategy'
            }
        }
        
        # Add specific cost recommendations
        chemical_count = len(treatment_info.get('chemical_treatments', []))
        organic_count = len(treatment_info.get('organic_treatments', []))
        
        if chemical_count > 0 and organic_count > 0:
            cost_analysis['recommendation'] = 'Consider integrated approach: start with organic methods, use chemicals if needed'
        elif chemical_count > 0:
            cost_analysis['recommendation'] = 'Chemical treatments available - use judiciously to prevent resistance'
        elif organic_count > 0:
            cost_analysis['recommendation'] = 'Organic treatments preferred - may require patience for results'
        else:
            cost_analysis['recommendation'] = 'Focus on prevention and cultural practices'
        
        return cost_analysis
    
    def _assess_environmental_impact(self, treatment_info):
        """Assess environmental impact of treatment options"""
        impact_assessment = {
            'chemical_treatments': {
                'environmental_risk': 'medium-high',
                'considerations': [
                    'Potential impact on beneficial insects',
                    'Risk of pesticide resistance development',
                    'Possible soil and water contamination',
                    'Follow label instructions strictly'
                ]
            },
            'organic_treatments': {
                'environmental_risk': 'low',
                'considerations': [
                    'Generally safe for beneficial organisms',
                    'Biodegradable and sustainable',
                    'May require more frequent applications',
                    'Support natural ecosystem balance'
                ]
            },
            'cultural_practices': {
                'environmental_risk': 'very low',
                'considerations': [
                    'Enhance soil health and biodiversity',
                    'Reduce dependency on external inputs',
                    'Sustainable long-term approach',
                    'Support integrated pest management'
                ]
            }
        }
        
        return impact_assessment
    
    def _get_default_recommendations(self):
        """Get default recommendations for unknown diseases"""
        return {
            'urgency': 'medium',
            'description': 'Unknown disease - general management recommended',
            'chemical_treatments': [],
            'organic_treatments': [
                {
                    'method': 'General Fungicide',
                    'procedure': 'Apply broad-spectrum organic fungicide',
                    'timing': 'Weekly applications until symptoms improve',
                    'effectiveness': 'Variable depending on actual disease'
                }
            ],
            'prevention': [
                'Improve plant hygiene',
                'Ensure proper nutrition',
                'Maintain optimal growing conditions',
                'Monitor for symptom changes',
                'Consult agricultural extension services'
            ],
            'cultural_practices': [
                'Regular field inspection',
                'Proper sanitation',
                'Balanced fertilization',
                'Adequate irrigation management'
            ],
            'application_timing': {
                'immediate_action': 'Implement general management practices',
                'follow_up': 'Monitor closely and seek expert diagnosis',
                'best_time': 'As needed based on weather conditions'
            }
        }
    
    def get_integrated_management_plan(self, disease_predictions, pest_predictions):
        """
        Create an integrated management plan for multiple diseases and pests
        
        Args:
            disease_predictions (list): List of disease predictions
            pest_predictions (list): List of pest predictions
            
        Returns:
            dict: Integrated management plan
        """
        if not disease_predictions:
            return self._get_default_recommendations()
        
        # Get primary disease (highest confidence)
        primary_disease = disease_predictions[0]['disease']
        primary_confidence = disease_predictions[0]['confidence']
        
        # Get comprehensive recommendations for primary disease
        primary_recommendations = self.get_treatment_recommendations(
            primary_disease, pest_predictions, primary_confidence
        )
        
        # Add considerations for secondary diseases
        secondary_diseases = disease_predictions[1:3]  # Top 3 total
        if secondary_diseases:
            primary_recommendations['secondary_considerations'] = []
            for disease_pred in secondary_diseases:
                if disease_pred['confidence'] >= 0.3:  # Only consider if reasonably confident
                    secondary_info = get_treatment_info(disease_pred['disease'])
                    primary_recommendations['secondary_considerations'].append({
                        'disease': disease_pred['disease'],
                        'confidence': disease_pred['confidence'],
                        'key_treatments': secondary_info.get('chemical_treatments', [])[:2],  # Top 2
                        'prevention': secondary_info.get('prevention', [])[:3]  # Top 3
                    })
        
        return primary_recommendations