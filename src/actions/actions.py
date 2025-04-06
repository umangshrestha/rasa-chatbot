from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime


strftime_format = "%Y-%m-%d %H:%M:%S"


class ActionAskTime(Action):

    def name(self) -> Text:
        return "action_ask_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("Asking for the current time")
        current_time = datetime.now().strftime("%Y-%m-%d")
        dispatcher.utter_message(text=f"The current time is {current_time}")
        return []
