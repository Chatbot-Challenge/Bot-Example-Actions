from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import EventType , SlotSet
from rasa_sdk.types import DomainDict
from rasa_sdk.executor import CollectingDispatcher

class GameContext():
    _curent_room_name: str = ""
    _has_key: bool = False
    _number_tried: int = 0

    def __init__(
            self,
            tracker: Tracker,
            domain: DomainDict
        ):
        self._tracker = tracker
        self._domain = domain
        
    def compute_response(self) -> str:
        return f"hmmmm {self._tracker.latest_message['text']}"
    
    def compute_Events(self) ->  List[EventType]:
        return [SlotSet(key="data", value= {'oha': 5, 'has_key': self._has_key})]


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("Oha, stuff happens")

        context = GameContext(tracker=tracker, domain=domain)
        system_turn = context.compute_response() 
        dispatcher.utter_message(text=system_turn)

        return context.compute_Events()
