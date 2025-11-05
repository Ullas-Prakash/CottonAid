"""
Pest Predictor Component
Predicts pests based on identified diseases with confidence scoring
"""
from .pest_database import DISEASE_PEST_MAPPING, PEST_DETAILS, get_pest_info, get_all_pests_for_disease

class PestPredictor:
    def __init__(self):
        self.pest_mapping = DISEASE_PEST_MAPPING
        self.pest_details = PEST_DETAILS
    
    def predict_pests(self, disease_name, disease_confidence=1.0):
        """
        Predict pests based on identified disease
        
        Args:
            disease_name (str): Name of the identified disease
            disease_confidence (float): Confidence score of disease prediction
            
        Returns:
            list: List of predicted pests with confidence scores
        """
        if disease_name not in self.pest_mapping:
            return []
        
        pests = self.pest_mapping[disease_name]
        
        # Adjust pest confidence based on disease confidence
        adjusted_pests = []
        for pest in pests:
            adjusted_pest = pest.copy()
            # Adjust confidence: pest_confidence * disease_confidence
            adjusted_pest['confidence'] = pest['confidence'] * disease_confidence
            
            # Add additional pest details
            pest_details = get_pest_info(pest['pest_name'])
            adjusted_pest.update(pest_details)
            
            adjusted_pests.append(adjusted_pest)
        
        # Sort by confidence (highest first)
        adjusted_pests.sort(key=lambda x: x['confidence'], reverse=True)
        
        return adjusted_pests
    
    def predict_multiple_diseases(self, disease_predictions):
        """
        Predict pests for multiple disease predictions
        
        Args:
            disease_predictions (list): List of disease predictions with confidence
            
        Returns:
            dict: Combined pest predictions with aggregated confidence
        """
        all_pests = {}
        
        for disease_pred in disease_predictions:
            disease_name = disease_pred['disease']
            disease_confidence = disease_pred['confidence']
            
            pests = self.predict_pests(disease_name, disease_confidence)
            
            for pest in pests:
                pest_name = pest['pest_name']
                
                if pest_name in all_pests:
                    # Aggregate confidence scores (take maximum)
                    if pest['confidence'] > all_pests[pest_name]['confidence']:
                        all_pests[pest_name] = pest
                else:
                    all_pests[pest_name] = pest
        
        # Convert to list and sort by confidence
        result = list(all_pests.values())
        result.sort(key=lambda x: x['confidence'], reverse=True)
        
        return result
    
    def get_pest_management_priority(self, pests):
        """
        Determine management priority based on pest characteristics
        
        Args:
            pests (list): List of predicted pests
            
        Returns:
            dict: Priority levels and recommendations
        """
        if not pests:
            return {'priority': 'none', 'action': 'Monitor plant health regularly'}
        
        highest_confidence = pests[0]['confidence']
        pest_types = [pest['pest_type'] for pest in pests]
        
        # Determine priority based on confidence and pest types
        if highest_confidence >= 0.8:
            priority = 'high'
            action = 'Immediate treatment required'
        elif highest_confidence >= 0.6:
            priority = 'medium'
            action = 'Treatment recommended within 1-2 days'
        else:
            priority = 'low'
            action = 'Monitor closely and consider preventive measures'
        
        # Adjust priority based on pest types
        if 'insect' in pest_types and highest_confidence >= 0.7:
            priority = 'high'
            action = 'Immediate insect control measures needed'
        elif 'fungus' in pest_types and highest_confidence >= 0.8:
            priority = 'high'
            action = 'Apply fungicide treatment immediately'
        
        return {
            'priority': priority,
            'action': action,
            'pest_types_present': list(set(pest_types)),
            'primary_pest': pests[0]['pest_name'] if pests else None
        }
    
    def get_seasonal_risk_assessment(self, pests, current_season='unknown'):
        """
        Assess seasonal risk factors for predicted pests
        
        Args:
            pests (list): List of predicted pests
            current_season (str): Current season (spring, summer, fall, winter)
            
        Returns:
            dict: Seasonal risk assessment
        """
        if not pests:
            return {'risk_level': 'low', 'recommendations': []}
        
        seasonal_factors = {
            'spring': {
                'high_risk_types': ['fungus', 'bacteria'],
                'conditions': 'Cool, wet conditions favor fungal and bacterial diseases'
            },
            'summer': {
                'high_risk_types': ['insect', 'virus'],
                'conditions': 'Hot, dry conditions favor insect pests and virus transmission'
            },
            'fall': {
                'high_risk_types': ['fungus'],
                'conditions': 'Moderate temperatures and humidity favor fungal diseases'
            },
            'winter': {
                'high_risk_types': ['fungus'],
                'conditions': 'Cool, wet conditions may promote soil-borne fungi'
            }
        }
        
        if current_season in seasonal_factors:
            high_risk_types = seasonal_factors[current_season]['high_risk_types']
            pest_types = [pest['pest_type'] for pest in pests]
            
            risk_pests = [pest for pest in pests if pest['pest_type'] in high_risk_types]
            
            if risk_pests:
                risk_level = 'high' if risk_pests[0]['confidence'] >= 0.7 else 'medium'
            else:
                risk_level = 'low'
            
            recommendations = [
                f"Current season ({current_season}) conditions: {seasonal_factors[current_season]['conditions']}",
                f"Monitor for {', '.join(high_risk_types)} pests closely"
            ]
        else:
            risk_level = 'medium'
            recommendations = ['Monitor all pest types as season is unknown']
        
        return {
            'risk_level': risk_level,
            'recommendations': recommendations,
            'seasonal_conditions': seasonal_factors.get(current_season, {}).get('conditions', 'Unknown')
        }