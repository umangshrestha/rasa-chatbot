from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime
from rasa_sdk.events import SlotSet


strftime_format = "%Y-%m-%d %H:%M:%S"


class ActionAskTime(Action):

    def name(self) -> Text:
        return "action_ask_time"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        print("Asking for the current time")
        current_time = datetime.now().strftime("%Y-%m-%d")
        dispatcher.utter_message(text=f"The current time is {current_time}")
        return []


class ActionStoreBirthYear(Action):
    def name(self):
        return "action_store_birthyear"

    def run(self, dispatcher, tracker, domain):
        year = next(tracker.get_latest_entity_values("year"), None)
        if year:
            dispatcher.utter_message(response="utter_ack_birth_year")
            return [SlotSet("year", year)]
        else:
            dispatcher.utter_message(response="utter_ask_birth_year")
            return []


class ActionCalculateAge(Action):
    def name(self) -> Text:
        return "action_calculate_age"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        year = tracker.get_slot("year")
        if year:
            age = datetime.now().year - int(year)
            dispatcher.utter_message(response="utter_age", age=age)
        else:
            dispatcher.utter_message(response="utter_ask_birth_year")

        return []
