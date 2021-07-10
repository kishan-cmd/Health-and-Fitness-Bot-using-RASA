# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

class ActionCarousel(Action):
    def name(self) -> Text:
        return "action_carousels"

    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "DIET 🥗",
                        "subtitle": "Hey 👋! I'm your Diet Assistant 🤖",
                        "image_url": "https://cdn.videoplasty.com/gif/vegan-food-scene-stock-gif-5600-384x216.gif",
                        "buttons": [
                            {
                                "title": "WEIGHT GAIN",
                                "payload": "/gain_weight",
                                "type": "postback"
                            },
                            {
                                "title": "WEIGHT LOSS",
                                "payload": "/loose_weight",
                                "type": "postback"
                            },
                            {
                                "title": "HEALTHY TIPS",
                                "payload": "/healthy_tips",
                                "type": "postback"
                            },
                            {
                                "title": "HELP",
                                "payload": "/help",
                                "type": "postback"
                            }                   
                        ]
                    },
                    {
                        "title": "SUPPLIMENTS 💊",
                        "subtitle": "Hey 😀, I'm your Suppliments Assistant💊",
                        "image_url": "https://media3.giphy.com/media/5nvMnYHb4ldlp7nWaY/200w.gif",
                        "buttons": [
                            {
                               "title": "Suppliments Information",
                               "payload": "/suppliments_info",
                                "type": "postback"
                            },
                            {
                                "title": "Shop for supplements online",
                                "payload": "/suppliments",
                                "type": "postback"
                            } 
                        ]
                    },
                    {
                        "title": "WORKOUTS ❚█══█❚",
                        "Subtitle": "Hey 👋, I'm your Gym Assistant 🤖" ,
                        "image_url": "https://mymodernmet.com/wp/wp-content/uploads/archive/yNkr5hUh4HG8YHmdhoUX_7dailymoves1.gif",
                        "buttons": [
                            {
                                "title": "HOME WORKOUTS",
                                "payload": "/home_workouts",
                                "type": "postback"
                            },
                            {
                                "title": "GYM WORKOUTS",
                                "payload": "/gym_workouts",
                                "type": "postback"
                            },
                            {
                                "title": "CROSS-FIT WORKOUTS",
                                "url": "https://www.youtube.com/channel/UCtcQ6TPwXAYgZ1Mcl3M1vng",
                                "type": "web_url"
                            },
                            {
                                "title": "WORKOUTS PLANS",
                                "payload": "/workout_plans",
                                "type": "postback"                                
                            },
                            { 
                                "title": "SET OF DUMBELLS",
                                "url": "https://www.verywellfit.com/best-dumbbells-4157486",
                                "type": "web_url"
                            }                            
                        
                        ]
                    },
                    {
                        "title": "Yoga",
                        "subtitle": "Hey 👋, I'm your Yoga Assistant 🧘.",
                        "image_url": "https://media0.giphy.com/media/DBbPjLMsQPruMkDcrd/200.gif",
                        "buttons": [
                            {
                               "title": "What is yoga 🤔",
                               "payload": "/yoga_information",
                                "type": "postback"
                            },
                            {
                                "title": "HISTORY OF YOGA 📓",
                                "payload": "/yoga_history",
                                "type": "postback"
                            },
                            {
                                "title": "TYPES OF YOGA 🧘‍♂️",
                                "payload": "/yoga_types",
                                "type": "postback"
                            },
                            {
                                "title": "BENIFITS OF YOGA 🥰",
                                "payload": "/yoga_benifits",
                                "type": "postback"
                            },
                            {
                                "title": "YOGA CHAKRAS 🤸‍♂️",
                                "payload": "/yoga_chakras",
                                "type": "postback"
                            }                           
                        ]
                    }
                ]
            }
        }
        dispatcher.utter_message(attachment=message)
        return []

class ActionAnytThing(Action):
    def name(self) -> Text:
        return "action_anyhting"

    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Is there anything else i can help with you 🧐",
                        "image_url": "https://media1.tenor.com/images/417b164404395c70a1bbd36b44c1ef10/tenor.gif?itemid=15839692",
                        "buttons": [
                            {
                                "title": "YES 👍",
                                "payload": "/yes",
                                "type": "postback"
                            },
                            {
                                "title": "NO 👎",
                                "payload": "/no",
                                "type": "postback"
                            }                           
                        ]
                    }
                ]
            }
        }
        dispatcher.utter_message(attachment=message)
        return []


