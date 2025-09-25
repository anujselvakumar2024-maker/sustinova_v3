"""
Custom Jorethang Farming AI Model - Advanced Agricultural Expert System
Enhanced for Eco-Intelligent Agriculture v6.0
"""
import json
import datetime
import random
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
import re

@dataclass
class CropRecommendation:
    crop_name: str
    planting_time: str
    harvest_time: str
    productivity: str
    market_price: str
    water_requirement: str
    management_tips: List[str]
    intercropping_options: List[str]

class JorethangFarmingAI:
    """
    Enhanced AI Model for Jorethang Eco-Intelligent Farming
    Location: Jorethang, South Sikkim (27.106960, 88.323318)
    Specialization: Sustainable agriculture, eco-friendly farming practices
    """

    def __init__(self):
        self.jorethang_data = self._initialize_knowledge_base()

    def _initialize_knowledge_base(self) -> Dict[str, Any]:
        return {
            "location": {
                "name": "Jorethang Valley",
                "district": "South Sikkim", 
                "coordinates": "27.106960, 88.323318",
                "altitude": "300-400m above sea level",
                "climate": "Sub-tropical valley climate with monsoon influence",
                "annual_rainfall": "1155mm distributed over 90 rainy days",
                "temperature_range": "Summer: 18-29°C | Winter: 10-15°C",
                "soil_type": "Well-drained coarse loamy soil, naturally acidic (pH 5.0-6.0)",
                "total_cultivated_area": "1,349 hectares of fertile valley land",
                "eco_advantages": [
                    "Natural valley protection from extreme weather",
                    "Rich biodiversity supporting beneficial insects",
                    "Organic matter-rich soil from forest decomposition",
                    "Natural water sources from mountain streams",
                    "Traditional eco-friendly farming practices"
                ]
            },
            "sustainable_practices": {
                "organic_farming": {
                    "benefits": "Premium market prices, soil health improvement, reduced input costs",
                    "certification": "Available through Sikkim Organic Mission",
                    "techniques": [
                        "Compost preparation using farm waste",
                        "Vermicomposting with local earthworms",
                        "Green manuring with leguminous crops",
                        "Integrated pest management (IPM)",
                        "Crop rotation for soil fertility"
                    ]
                },
                "water_conservation": {
                    "rainwater_harvesting": "Collect monsoon water in ponds and tanks",
                    "drip_irrigation": "60% water savings compared to flood irrigation",
                    "mulching": "Reduces water evaporation by 40-50%",
                    "terracing": "Prevents soil erosion and water runoff"
                },
                "biodiversity": {
                    "intercropping_benefits": "Natural pest control, soil improvement, income diversification",
                    "native_varieties": "Better adaptation to local climate and diseases",
                    "pollinator_plants": "Marigold, sunflower to attract beneficial insects"
                }
            },
            "major_crops": {
                "ginger": {
                    "scientific_name": "Zingiber officinale",
                    "area_coverage": "140 hectares (prime cash crop)",
                    "annual_production": "5,600 quintals",
                    "productivity": "40 quintals per hectare (excellent yield)",
                    "eco_practices": [
                        "Use farm yard manure (FYM) 40-60 tonnes/hectare",
                        "Neem cake application for natural pest control",
                        "Raised bed cultivation for drainage",
                        "Organic mulching with dried leaves",
                        "Companion planting with turmeric"
                    ],
                    "market_advantages": [
                        "Organic certification premium: 25-30% higher prices",
                        "Direct export potential to mainland India",
                        "Processing opportunities: dried ginger, powder, oil",
                        "Year-round storage capability when properly cured"
                    ]
                },
                "maize": {
                    "varieties": ["Local yellow corn", "Sweet corn", "Pop corn varieties"],
                    "area_coverage": "1,100 hectares (food security crop)",
                    "eco_benefits": [
                        "Excellent intercrop with legumes (nitrogen fixation)",
                        "Stalks used for compost preparation",
                        "Green fodder for livestock",
                        "Natural windbreak for other crops"
                    ],
                    "sustainable_techniques": [
                        "Seed treatment with neem oil",
                        "Integrated nutrient management",
                        "Crop residue management",
                        "Minimal tillage practices"
                    ]
                }
            },
            "climate_smart_farming": {
                "monsoon_management": [
                    "Drainage systems for excess water",
                    "Protected cultivation during heavy rains", 
                    "Fungal disease prevention in high humidity",
                    "Harvest timing to avoid rain damage"
                ],
                "drought_resilience": [
                    "Drought-tolerant crop varieties",
                    "Soil moisture conservation techniques",
                    "Efficient irrigation scheduling",
                    "Stress-resistant farming practices"
                ],
                "temperature_adaptation": [
                    "Cold protection for winter crops",
                    "Shade management in summer",
                    "Microclimate optimization",
                    "Season extension techniques"
                ]
            }
        }

    def get_comprehensive_answer(self, query: str, language: str = 'en') -> str:
        query_lower = query.lower()
        current_season = self._get_current_season()

        # Enhanced keyword matching
        if self._contains_keywords(query_lower, ["ginger", "adrak", "ada", "organic ginger"]):
            return self._get_ginger_expert_advice(language, current_season)
        elif self._contains_keywords(query_lower, ["maize", "corn", "makkai", "bhutta", "sweet corn"]):
            return self._get_maize_sustainable_advice(language, current_season)
        elif self._contains_keywords(query_lower, ["organic", "sustainable", "eco-friendly", "natural farming"]):
            return self._get_sustainable_farming_advice(language)
        elif self._contains_keywords(query_lower, ["weather", "climate", "rain", "monsoon", "temperature"]):
            return self._get_climate_advice(language, current_season)
        elif self._contains_keywords(query_lower, ["irrigation", "water", "drip", "sprinkler", "watering"]):
            return self._get_smart_irrigation_advice(language)
        elif self._contains_keywords(query_lower, ["soil", "fertility", "compost", "manure", "nutrients"]):
            return self._get_soil_health_advice(language)
        elif self._contains_keywords(query_lower, ["pest", "disease", "insects", "fungus", "organic control"]):
            return self._get_pest_management_advice(language)
        else:
            return self._get_comprehensive_farming_guide(language, current_season)

    def _contains_keywords(self, query: str, keywords: List[str]) -> bool:
        return any(keyword in query for keyword in keywords)

    def _get_current_season(self) -> str:
        month = datetime.datetime.now().month
        if 2 <= month <= 5:
            return "pre_monsoon"
        elif 6 <= month <= 9:
            return "monsoon"
        else:
            return "post_monsoon"

    def _get_ginger_expert_advice(self, language: str, season: str) -> str:
        advice = "🌿 **JORETHANG GINGER CULTIVATION - ECO-INTELLIGENT APPROACH**\n\n"
        advice += "**🌱 SUSTAINABLE GINGER FARMING:**\n"
        advice += "• **Organic Premium**: 25-30% higher market prices\n"
        advice += "• **Productivity**: 40 quintals/hectare (excellent yield)\n"
        advice += "• **Coverage**: 140 hectares in Jorethang valley\n\n"

        advice += "**🌍 ECO-FRIENDLY PRACTICES:**\n"
        advice += "• **Organic Input**: 40-60 tonnes FYM per hectare\n"
        advice += "• **Natural Pest Control**: Neem cake 250 kg/hectare\n"
        advice += "• **Water Smart**: Raised beds + organic mulching\n"
        advice += "• **Companion Crops**: Intercrop with turmeric & coriander\n\n"

        advice += "**📈 MARKET ADVANTAGES:**\n"
        advice += "• Direct export potential to mainland markets\n"
        advice += "• Processing: Fresh, dried, powder, essential oil\n"
        advice += "• Organic certification through Sikkim Organic Mission\n"
        advice += "• Year-round income with proper storage\n\n"

        if season == "pre_monsoon":
            advice += "**🎯 CURRENT SEASON ADVICE (Pre-Monsoon):**\n"
            advice += "Perfect planting time! Prepare raised beds, apply organic matter, and plant certified rhizomes."
        elif season == "monsoon":
            advice += "**🎯 CURRENT SEASON ADVICE (Monsoon):**\n"
            advice += "Monitor drainage, apply organic mulch, watch for fungal diseases, maintain soil moisture."
        else:
            advice += "**🎯 CURRENT SEASON ADVICE (Post-Monsoon):**\n"
            advice += "Harvest time! Proper curing, storage planning, and market preparation for premium prices."

        return advice

    def _get_sustainable_farming_advice(self, language: str) -> str:
        advice = "🌱 **JORETHANG ECO-INTELLIGENT FARMING GUIDE**\n\n"
        advice += "**🌍 SUSTAINABLE PRACTICES ACTIVE:**\n"
        advice += "• **Organic Certification**: Available through Sikkim Organic Mission\n"
        advice += "• **Premium Markets**: 25-30% higher prices for organic produce\n"
        advice += "• **Soil Health**: Natural composting & vermicomposting\n"
        advice += "• **Water Conservation**: Rainwater harvesting + drip irrigation\n\n"

        advice += "**🔬 NATURAL INPUTS:**\n"
        advice += "• **Compost**: Farm waste + kitchen scraps + cow dung\n"
        advice += "• **Vermicompost**: Local earthworms + organic matter\n"
        advice += "• **Green Manure**: Leguminous crops for nitrogen fixation\n"
        advice += "• **Neem Products**: Natural pest and disease control\n\n"

        advice += "**💧 WATER SMART TECHNIQUES:**\n"
        advice += "• **Drip Irrigation**: 60% water savings\n"
        advice += "• **Mulching**: 40-50% evaporation reduction\n"
        advice += "• **Rainwater Harvesting**: Monsoon water collection\n"
        advice += "• **Terracing**: Soil erosion prevention\n\n"

        advice += "**🦋 BIODIVERSITY BENEFITS:**\n"
        advice += "• **Intercropping**: Natural pest control + income diversification\n"
        advice += "• **Native Varieties**: Better climate adaptation\n"
        advice += "• **Pollinator Plants**: Marigold, sunflower for beneficial insects"

        return advice

    def _get_climate_advice(self, language: str, season: str) -> str:
        advice = "🌤️ **JORETHANG VALLEY CLIMATE INTELLIGENCE**\n\n"
        advice += "**📍 LOCATION ADVANTAGES:**\n"
        advice += "• **Climate Zone**: Sub-tropical valley with monsoon influence\n"
        advice += "• **Natural Protection**: Valley provides weather stability\n"
        advice += "• **Rainfall**: 1,155mm over 90 days (ideal for agriculture)\n"
        advice += "• **Temperature**: Summer 18-29°C | Winter 10-15°C\n\n"

        advice += "**🌧️ SEASONAL FARMING CALENDAR:**\n"
        advice += "• **Pre-Monsoon (Feb-May)**: Planting season for major crops\n"
        advice += "• **Monsoon (Jun-Sep)**: Growth period, drainage management\n"
        advice += "• **Post-Monsoon (Oct-Jan)**: Harvest, processing, storage\n\n"

        if season == "monsoon":
            advice += "**⚡ CURRENT MONSOON STRATEGY:**\n"
            advice += "• **Drainage**: Ensure water doesn't stagnate\n"
            advice += "• **Disease Watch**: High humidity fungal prevention\n"
            advice += "• **Soil Cover**: Maintain mulching for root protection\n"
            advice += "• **Harvest Planning**: Time crops before heavy rains"

        return advice

    def _get_smart_irrigation_advice(self, language: str) -> str:
        advice = "💧 **JORETHANG SMART IRRIGATION - ECO APPROACH**\n\n"
        advice += "**🎯 WATER EFFICIENCY TECHNIQUES:**\n"
        advice += "• **Drip Irrigation**: 60% water savings, precise delivery\n"
        advice += "• **Micro-Sprinklers**: Gentle water distribution\n"
        advice += "• **Scheduling**: Morning (6-8 AM) or evening (6-8 PM)\n"
        advice += "• **Soil Monitoring**: Moisture-based irrigation decisions\n\n"

        advice += "**🌱 CROP-SPECIFIC WATER NEEDS:**\n"
        advice += "• **Ginger**: High water during rhizome development (Jun-Aug)\n"
        advice += "• **Maize**: Critical during tasseling and grain filling\n"
        advice += "• **Vegetables**: Light, frequent irrigation\n"
        advice += "• **Organic Crops**: Consistent moisture without waterlogging\n\n"

        advice += "**💡 CONSERVATION STRATEGIES:**\n"
        advice += "• **Mulching**: Organic matter to retain soil moisture\n"
        advice += "• **Rainwater Collection**: Monsoon water in tanks/ponds\n"
        advice += "• **Terracing**: Prevent water runoff on slopes\n"
        advice += "• **Shade Management**: Reduce evaporation losses\n\n"

        advice += "**📊 SMART TECHNOLOGY:**\n"
        advice += "• **Soil Sensors**: Real-time moisture monitoring\n"
        advice += "• **Weather Integration**: Rain prediction for scheduling\n"
        advice += "• **Automated Systems**: Timer-based precision irrigation"

        return advice

    def _get_soil_health_advice(self, language: str) -> str:
        advice = "🌱 **JORETHANG SOIL HEALTH - ECO MANAGEMENT**\n\n"
        advice += "**🧪 SOIL PROFILE ANALYSIS:**\n"
        advice += "• **Type**: Well-drained coarse loamy soil\n"
        advice += "• **pH**: Naturally acidic (5.0-6.0) - needs lime\n"
        advice += "• **Organic Matter**: Medium to low - improvement needed\n"
        advice += "• **Drainage**: Good natural drainage in valley slopes\n\n"

        advice += "**🌿 ORGANIC SOIL IMPROVEMENT:**\n"
        advice += "• **Compost**: 10-15 tonnes per hectare annually\n"
        advice += "• **Vermicompost**: Local earthworms + organic waste\n"
        advice += "• **FYM**: Well-decomposed cattle manure\n"
        advice += "• **Green Manure**: Dhaincha, cowpea in fallow periods\n\n"

        advice += "**⚗️ NATURAL AMENDMENTS:**\n"
        advice += "• **Lime**: 500-800 kg/hectare to raise pH\n"
        advice += "• **Rock Phosphate**: Natural phosphorus source\n"
        advice += "• **Wood Ash**: Potassium source from local biomass\n"
        advice += "• **Bone Meal**: Organic phosphorus and calcium\n\n"

        advice += "**🔄 SUSTAINABLE PRACTICES:**\n"
        advice += "• **Crop Rotation**: Legumes for nitrogen fixation\n"
        advice += "• **Cover Crops**: Soil protection during off-season\n"
        advice += "• **Minimal Tillage**: Preserve soil structure\n"
        advice += "• **Living Mulch**: Permanent soil cover"

        return advice

    def _get_comprehensive_farming_guide(self, language: str, season: str) -> str:
        location_data = self.jorethang_data["location"]

        advice = "🌾 **JORETHANG ECO-INTELLIGENT FARMING SYSTEM**\n\n"
        advice += "**📍 VALLEY ADVANTAGES:**\n"
        advice += f"• **Location**: {location_data['name']}, {location_data['district']}\n"
        advice += f"• **Climate**: {location_data['climate']}\n"
        advice += f"• **Rainfall**: {location_data['annual_rainfall']}\n"
        advice += f"• **Area**: {location_data['total_cultivated_area']}\n\n"

        advice += "**🏆 PREMIUM CROP RECOMMENDATIONS:**\n"
        advice += "1. **Organic Ginger (140 ha)** - Export quality, premium prices\n"
        advice += "2. **Sweet Corn & Pop Corn** - Value-added varieties\n"
        advice += "3. **Organic Vegetables** - Year-round protected cultivation\n"
        advice += "4. **Medicinal Plants** - High-value niche crops\n\n"

        advice += "**🌍 ECO-INTELLIGENT FEATURES:**\n"
        advice += "• **Smart Irrigation**: Sensor-based water management\n"
        advice += "• **AI Recommendations**: Crop, weather, and market analysis\n"
        advice += "• **Organic Certification**: Premium market access\n"
        advice += "• **Climate Resilience**: Sustainable farming practices\n"
        advice += "• **Multi-language Support**: Local language assistance\n\n"

        advice += "**🤖 ASK ME ABOUT:**\n"
        advice += "• Sustainable organic farming techniques\n"
        advice += "• Smart irrigation and water conservation\n"
        advice += "• Climate-smart crop planning\n"
        advice += "• Natural pest and disease management\n"
        advice += "• Market analysis and premium pricing\n"
        advice += "• Soil health and fertility improvement"

        return advice

# Initialize the enhanced AI model
jorethang_ai = JorethangFarmingAI()

def get_ai_response(query: str, language: str = 'en') -> str:
    """Enhanced AI response for eco-intelligent farming"""
    try:
        return jorethang_ai.get_comprehensive_answer(query, language)
    except Exception as e:
        return f"🌱 I'm your Jorethang eco-farming expert! Ask me about sustainable agriculture, organic farming, smart irrigation, or climate-smart practices. Error details: {str(e)}"

# Enhanced testing
if __name__ == "__main__":
    print("🌱 Jorethang Eco-Intelligent AI Model v6.0 - Testing")
    print("Test response:", get_ai_response("How to grow organic ginger sustainably?"))
